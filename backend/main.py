# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from query import get_answer  # from the updated query.py
import traceback

app = FastAPI(title="Personal AI Chat")

# Allow frontend to communicate with backend
origins = [
    "http://localhost:3000",  # React dev server
    "http://127.0.0.1:3000"
]

app.add_middleware(

    
        CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your React app later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Personal AI Chat API is running."}

@app.post("/ask")
def chat_endpoint(payload: dict):
    """
    payload: { "question": "Your question here" }
    """
    question = payload.get("question")
    if not question:
        raise HTTPException(status_code=400, detail="Question is required.")
    
    try:
        answer = get_answer(question)
        return {"answer": answer}
    except Exception as e:
        print("\n--- ERROR IN /ask ---")
        traceback.print_exc()
        print("--------------------\n")
        raise HTTPException(status_code=500, detail=str(e))
