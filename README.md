

# 📊 Enterprise AI Analytics & RAG Platform

An AI-powered analytics platform that converts natural language questions into SQL queries, executes them on uploaded business datasets, and generates interactive visualizations with actionable business insights.

---

## 📸 Application Preview

![Enterprise AI Analytics & RAG Platform](project-overview.png)

---

## 🌐 Live Demo

**Try the application here:**

https://ai-enterprise-analytics-rag.streamlit.app/

## 🎥 Demo Video

Watch the complete working demo here:

https://youtu.be/SJxwuIP8Jlg

## ✨ Features

- Upload CSV and Excel datasets
- AI-powered Natural Language to SQL
- Dynamic SQLite Query Execution
- Interactive Plotly Charts
- KPI Dashboard
- Business Insights
- CSV Export
- PDF Report Export
- Live Deployment
---

## 🛠 Tech Stack

- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- OpenRouter API
- SQL
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

User
↓
Streamlit UI
↓
OpenRouter LLM
↓
SQL Generator
↓
SQLite Database
↓
Plotly Visualization
↓
Business Insights
↓
PDF / CSV Export

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

## 📸 Screenshots

Coming Soon

---

## 🔮 Future Enhancements

- GPT-powered SQL generation
- Multi-table querying
- Authentication
- Dashboard export
- PDF report generation
- RAG document search

---

## 👨‍💻 Author

**Ajeet Yadav**

LinkedIn:
(Add your LinkedIn)

GitHub:
https://github.com/ajeetsm2010
