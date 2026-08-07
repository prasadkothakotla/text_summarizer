# 📝 AI Text Summarizer using T5 Transformer

An AI-powered **Text Summarization** web application built using **FastAPI**, **PyTorch**, and **Hugging Face Transformers**. The application uses a **fine-tuned T5 Transformer** model to generate concise and meaningful summaries from long text passages.

---

## 📸 Application Screenshot
![Text Summarizer](images/homepage.png)
---

## 🚀 Features

* 🤖 Fine-tuned **T5 Transformer** for abstractive text summarization
* ⚡ High-performance **FastAPI** backend
* 🌐 Responsive web interface using HTML, CSS, and JavaScript
* 🧹 Automatic text preprocessing before summarization
* 📄 REST API support for integration with other applications
* 💡 Clean and beginner-friendly project structure

---

## 🛠️ Tech Stack

| Category      | Technology                     |
| ------------- | ------------------------------ |
| Language      | Python                         |
| Backend       | FastAPI                        |
| Deep Learning | PyTorch                        |
| NLP           | Hugging Face Transformers (T5) |
| Frontend      | HTML, CSS, JavaScript          |
| API Server    | Uvicorn                        |

---

## 📁 Project Structure

```text
text_summarizer/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── images/
│   └── screenshot.png
├── saved_summarizer/      (Ignored from Git)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/prasadkothakotla/text_summarizer.git
cd text_summarizer
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
python -m uvicorn app:app --reload
```

Open your browser and visit:

```
http://127.0.0.1:8000
```

---

## 📡 API Endpoint

### POST `/summarize`

### Request

```json
{
  "dialogue": "Enter your text here..."
}
```

### Response

```json
{
  "summary": "Generated summary..."
}
```

---

## 💻 Example

### Input

```
Artificial Intelligence is transforming industries by automating tasks,
improving decision-making, and enhancing customer experiences.
```

### Output

```
Artificial Intelligence is transforming industries through automation,
improved decision-making, and better customer experiences.
```

---

## ✨ Future Improvements

* 📄 PDF summarization
* 📑 DOCX summarization
* 🌍 Multi-language support
* 🎚️ Adjustable summary length
* ☁️ Cloud deployment (Render/Railway/AWS)
* 🔑 User authentication
* 📊 Summary history

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Prasad Kothakotla**

* GitHub: https://github.com/prasadkothakotla

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub. It helps others discover the project and motivates future improvements.
