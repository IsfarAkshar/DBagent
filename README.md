
# 📘 DBagent Agent (FastAPI + PostgreSQL + OpenRouter)

## 🚀 Overview

This project is an **AI-powered SQL agent** that converts natural language queries into SQL and executes them on a PostgreSQL database.

👉 Example:

```
Input:  "show all users"
Output: SELECT * FROM users;
```

---

## 🎯 Features

* 🔹 Natural Language → SQL conversion
* 🔹 FastAPI backend
* 🔹 PostgreSQL database integration
* 🔹 AI-powered query generation (OpenRouter)
* 🔹 Swagger UI for testing
* 🔹 Error handling & validation

---

## 🧱 Project Structure

```
DBagent-main/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── db.py
│   ├── models.py
│   ├── utils.py
│   └── llm.py
│
├── .env
├── requirements.txt
└── create_tables.py
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/ai-sql-agent.git
cd ai-sql-agent
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

Or manually:

```
pip install fastapi uvicorn sqlalchemy databases asyncpg python-dotenv openai
```

---

## 🗄️ Database Setup (PostgreSQL)

### Create Database

```sql
CREATE DATABASE ai_sql_db;
```

---

### Create Table

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
);

INSERT INTO users (name, email)
VALUES 
('John Doe', 'john@example.com'),
('Alice', 'alice@example.com'),
('Rahim', 'rahim@gmail.com');
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/ai_sql_db
OPENROUTER_API_KEY=your_api_key_here
```

---

## 🤖 AI Setup (OpenRouter)

1. Go to 👉 [https://openrouter.ai](https://openrouter.ai)
2. Create an account
3. Generate API key
4. Add it to `.env`

---

## ▶️ Run the App

```
python -m uvicorn app.main:app
```

---

## 🌐 API Documentation

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Request

```json
{
  "question": "show all users"
}
```

---

## 📤 Example Response

```json
{
  "sql": "SELECT * FROM users LIMIT 100;",
  "rows": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com"
    }
  ]
}
```

---

## ⚠️ Common Errors & Fixes

| Error                  | Fix                        |
| ---------------------- | -------------------------- |
| uvicorn not recognized | use `python -m uvicorn`    |
| DATABASE_URL None      | check `.env`               |
| connection refused     | remove `--reload`          |
| validation error       | fix JSON format            |
| API key invalid        | use correct OpenRouter key |

---

## 🧠 How It Works

```
User Question
     ↓
AI Model (OpenRouter)
     ↓
SQL Query
     ↓
PostgreSQL Database
     ↓
Result Returned
```

---

## 📌 Technologies Used

* FastAPI
* PostgreSQL
* OpenRouter (LLM)
* SQLAlchemy
* Databases (async)

---

## 🎓 Learning Outcomes

* API development with FastAPI
* AI integration in backend
* Database querying with SQL
* Debugging real-world errors

---

## 📄 License

This project is for educational purposes.

---

## 🙌 Acknowledgements

* FastAPI Documentation
* PostgreSQL
* OpenRouter API


