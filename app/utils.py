from fastapi import HTTPException
from .db import db
from .llm import generate_sql

ALLOWED_TABLES = ["users", "orders", "products"]  # whitelist

async def detect_table(question: str) -> str:
    rows = await db.fetch_all("""
        SELECT table_name FROM information_schema.tables
        WHERE table_schema='public'
    """)
    tables = [r["table_name"] for r in rows if r["table_name"] in ALLOWED_TABLES]

    for t in tables:
        if t.lower() in question.lower():
            return t
    # fallback: pick first allowed table
    if tables:
        return tables[0]
    raise HTTPException(400, "No allowed table found in question.")

async def get_schema_for_question(question: str) -> dict:
    table = await detect_table(question)
    cols = await db.fetch_all("""
        SELECT column_name FROM information_schema.columns
        WHERE table_name = :table
        ORDER BY ordinal_position
    """, values={"table": table})
    return {"table_name": table, "columns": [r["column_name"] for r in cols]}

def generate_sql_from_question(question: str, schema: dict) -> str:
    prompt = f"""
    You are a SQL generator.
    Table: {schema['table_name']}
    Columns: {', '.join(schema['columns'])}
    Only generate valid SELECT SQL query for this question:
    {question}
    """
    sql = generate_sql(prompt)
    if not sql.lower().startswith("select"):
        sql = "SELECT * FROM " + schema['table_name'] + " LIMIT 100;"
    return sql