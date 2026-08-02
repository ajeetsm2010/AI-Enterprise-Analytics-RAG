<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-FF4B4B?logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-7B61FF)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly)

[![Live Demo](https://img.shields.io/badge/🚀-Live_Demo-success)](https://ai-enterprise-analytics-rag.streamlit.app/)
[![YouTube Demo](https://img.shields.io/badge/🎥-Demo-red)](https://youtu.be/SJxwuIP8Jlg)

</p>

<h1 align="center">📊 Enterprise AI Analytics & RAG Platform</h1>

<p align="center">
AI-powered analytics platform that converts natural language into SQL queries, executes them on uploaded business datasets, and generates interactive dashboards with business insights.
</p>

An AI-powered analytics platform that converts natural language questions into SQL queries, executes them on uploaded business datasets, and generates interactive visualizations with actionable business insights.

---

## 📸 Application Preview

<p align="center">
<img src="project-overview.png" width="900">
</p>

---

## 🌐 Live Demo

**Try the application here:**

https://ai-enterprise-analytics-rag.streamlit.app/

## 🎥 Demo Video

Watch the complete working demo here:

https://youtu.be/SJxwuIP8Jlg

## ✨ Features

- Upload CSV, XLSX and XLS datasets
- Natural Language to SQL using DeepSeek AI
- Automatic SQLite database creation
- AI-generated SQL queries
- Interactive Plotly dashboards
- KPI summary cards
- Dynamic business insights
- CSV export
- PDF report export
- Live deployment on Streamlit Cloud

## 🛠 Tech Stack

- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- OpenRouter API
- DeepSeek Chat
- LangChain
- FAISS
- Git & GitHub
---

## 📂 Project Structure

```
AI-Enterprise-Analytics-RAG/
│
├── app.py
├── requirements.txt
├── llm/
│   └── sql_generator.py
├── sql/
│   └── sql_engine.py
├── rag/
│   ├── loader.py
│   ├── retriever.py
│   └── vectorstore.py
├── documents/
└── README.md
```

---

## 🏗️ Architecture

```text
            User Question
                  │
                  ▼
           Streamlit UI
                  │
                  ▼
       OpenRouter (DeepSeek)
                  │
                  ▼
          SQL Generator
                  │
                  ▼
          SQLite Database
                  │
                  ▼
      Plotly Visualizations
                  │
                  ▼
        Business Insights
                  │
                  ▼
        CSV / PDF Export
```

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/ajeetsm2010/AI-Enterprise-Analytics-RAG.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
OPENROUTER_API_KEY=your_api_key_here
```

Run

```bash
streamlit run app.py
```

---

## 📊 Workflow

1. Upload a business dataset
2. Ask a question in natural language
3. AI generates SQL
4. SQL executes on SQLite
5. Interactive chart is generated
6. Business insights are displayed

---

## 💬 Sample Questions

- Which store has the highest capacity?
- Which store has the lowest capacity?
- Count total stores.
- List all cities.
- Show top stores by capacity.

---


## 🔮 Future Enhancements

- Multi-table SQL support
- Conversational memory
- Authentication & user login
- Dashboard sharing
- Advanced RAG document search
- Cloud database support
---

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Ajeet Yadav**

GitHub: https://github.com/ajeetsm2010

Live App:
https://ai-enterprise-analytics-rag.streamlit.app/

Demo Video:
https://youtu.be/SJxwuIP8Jlg


https://github.com/ajeetsm2010
