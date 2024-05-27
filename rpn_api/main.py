from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rpn import rpn_eval


class RpnExpr(BaseModel):
    expr: str


class RpnExprResult(BaseModel):
    expr: str
    result: float


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/calculator", response_model=RpnExprResult)
def calculate(rpnExpr: RpnExpr):
    try:
        result = rpn_eval(rpnExpr.expr)
        return RpnExprResult(expr=rpnExpr.expr, result=result)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
