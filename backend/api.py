from fastapi import FastAPI
from pydantic import BaseModel
from query import get_answer  # You need to wrap your existing query code in this function

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(req: QueryRequest):
    question = req.question
    answer = get_answer(question)  # This calls your TinyLlama + Pinecone code
    return {"answer": answer}
