from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rpn import rpn_eval

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.responses import StreamingResponse
import pandas as pd
from io import StringIO

DATABASE_URL = "postgresql://postgres:password@db/postgres"

def get_engine():
    return create_engine(DATABASE_URL)

engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class db_RpnExpr(Base):
    __tablename__ = "rpn_expressions"
    id = Column(Integer, primary_key=True, index=True)
    expr = Column(String, index=True)
    result = Column(Float)

Base.metadata.create_all(bind=engine)

class RpnExpr(BaseModel):
    expr: str

class RpnExprResult(BaseModel):
    expr: str
    result: float

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/export/csv")
def export_data():
    db = SessionLocal()
    data = db.query(db_RpnExpr).all()
    df = pd.DataFrame([{
        "id": item.id,
        "expr": item.expr,
        "result": item.result
    } for item in data])
    stream = StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=rpn_expressions.csv"
    return response

@app.post("/calculator", response_model=RpnExprResult)
def calculate(rpnExpr: RpnExpr):
    try:
        result = rpn_eval(rpnExpr.expr)
        db = SessionLocal()
        db_expr = db_RpnExpr(expr=rpnExpr.expr, result=result)
        db.add(db_expr)
        db.commit()
        db.refresh(db_expr)
        return RpnExprResult(expr=rpnExpr.expr, result=result)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
