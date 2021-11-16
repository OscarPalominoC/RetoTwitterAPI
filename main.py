# FastAPI
from fastapi import FastAPI
from fastapi import status

# Models
from Models.models import User, UserLogin

app = FastAPI()

@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"],
    summary="Home of the webpage."
    )
def home():
    """
# Home

This is the project's landing page.
    """
    return {"API Twitter":"Funcionando"}