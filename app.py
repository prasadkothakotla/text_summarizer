from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration,T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# initializing app

app=FastAPI(title="Text Summarizer App", description="Text summarization using T5 transformer",version="1.0")

#model & tokenizer
MODEL_NAME = "Kothakotla/text-summarizer"

model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)

if torch.backends.mps.is_available():
  device = torch.device("mps")
elif torch.cuda.is_available():
  device = torch.device("cuda")
else:
  device = torch.device("cpu")
print("Device:",device)
model.to(device)

templates= Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

#input Schema
class DialogueInput(BaseModel):
  dialogue: str

#clean data
def clean_data(text):
  text=re.sub(r"\r\n"," ",text) #lines
  text=re.sub(r"\s+"," ",text) #spaces
  text=re.sub(r"<.*?>"," ",text) #html tags
  text=text.strip().lower()
  return text

#summarization function
#  Testing the core logic

def summarize_dialogue(dialogue: str)-> str :
  dialogue = clean_data(dialogue)
  
  #tokenize
  inputs=tokenizer(
      dialogue,
      padding="max_length",
      truncation=True,
      max_length=512,
      return_tensors="pt"
  ).to(device)
  #generate the summary => token ids
  model.to(device)
  targets = model.generate(
      input_ids = inputs["input_ids"],
      attention_mask = inputs["attention_mask"],
      max_length = 150,
      num_beams = 4,
      early_stopping = True
  )


  #token ids converting into summary/decode

  summary = tokenizer.decode(targets[0],skip_special_tokens=True)
  return summary

#api endpoints

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )



@app.post("/summarize")
async def summarize(dialogue_input: DialogueInput):
  summary = summarize_dialogue(dialogue_input.dialogue)
  return {"summary":summary}


