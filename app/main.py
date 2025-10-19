from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .routers import calc
import pkg_resources

app = FastAPI(title="abrecko__demo API", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calc.router, prefix="/calc")

@app.get("/health")
def health():
    return {"status": "ok", "version": app.version}


@app.exception_handler(ZeroDivisionError)
def zero_division_handler(request, exc: ZeroDivisionError):
    return JSONResponse(status_code=400, content={"detail": "Cannot divide by zero"})
