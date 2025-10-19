from fastapi import APIRouter
from pydantic import BaseModel, Field
from typing import Literal

from calc import plus, minus, multiply, divide, safe_div

router = APIRouter()

class CalcRequest(BaseModel):
    a: float = Field(..., example=10)
    b: float = Field(..., example=2)

class CalcResponse(BaseModel):
    result: float = Field(..., example=5.0)

@router.post("/plus", response_model=CalcResponse)
def do_plus(req: CalcRequest):
    return {"result": plus(req.a, req.b)}

@router.post("/minus", response_model=CalcResponse)
def do_minus(req: CalcRequest):
    return {"result": minus(req.a, req.b)}

@router.post("/multiply", response_model=CalcResponse)
def do_multiply(req: CalcRequest):
    return {"result": multiply(req.a, req.b)}

@router.post("/divide", response_model=CalcResponse)
def do_divide(req: CalcRequest):
    if req.b == 0:
        raise ZeroDivisionError()
    return {"result": divide(req.a, req.b)}

@router.post("/safe-div", response_model=CalcResponse)
def do_safe_div(req: CalcRequest):
    if req.b == 0:
        raise ZeroDivisionError()
    return {"result": safe_div(req.a, req.b)}
