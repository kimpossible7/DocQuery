from fastapi import FastAPI
from app.routers import question_answer

app = FastAPI()
app.include_router(question_answer.router)
