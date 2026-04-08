from fastapi import FastAPI, HTTPException
from .models import QueryRequest, QueryResponse, ExecuteResponse
from .db import db
from .utils import get_schema_for_question, generate_sql_from_question

app = FastAPI(title="Free AI-to-SQL Agent")

@app.on_event("startup")
async def startup():
    await db.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()

@app.post("/generate-sql", response_model=QueryResponse)
async def generate_sql_route(payload: QueryRequest):
    try:
        schema = await get_schema_for_question(payload.question)
        sql = generate_sql_from_question(payload.question, schema)
        return QueryResponse(sql=sql)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/execute-sql", response_model=ExecuteResponse)
async def execute_sql_route(payload: QueryRequest):
    try:
        schema = await get_schema_for_question(payload.question)
        sql = generate_sql_from_question(payload.question, schema)
        rows = await db.fetch_all(sql)
        return ExecuteResponse(sql=sql, rows=[dict(r) for r in rows])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {str(e)}")
    
@app.get("/")
def home():
    return {"message": "DBagent is running"}
