from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    sql: str
    warning: Optional[str] = ""

class ExecuteResponse(BaseModel):
    sql: str
    rows: list