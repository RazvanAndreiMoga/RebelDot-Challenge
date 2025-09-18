from fastapi import FastAPI, Header, HTTPException, Depends
from pydantic import BaseModel
from app.db import SessionLocal
from app.models import FAQ
from app.utils import find_best_local_match
from sqlalchemy.orm import Session

app = FastAPI()

# Simple token auth
def get_token(x_token: str = Header(...)):
    if x_token != "supersecret":
        raise HTTPException(status_code=401, detail="Invalid token")
    return x_token

class QuestionRequest(BaseModel):
    user_question: str

@app.post("/ask-question")
def ask_question(request: QuestionRequest, token: str = Depends(get_token)):
    try:
        db: Session = SessionLocal()
        faqs = db.query(FAQ).all()

        # Find best match using string similarity
        best_faq = find_best_local_match(request.user_question, faqs)

        if best_faq:
            return {
                "source": "local",
                "matched_question": best_faq.question,
                "answer": best_faq.answer
            }
        else:
            # fallback text if no match
            return {
                "source": "openai",
                "matched_question": "N/A",
                "answer": "Could not find a close match locally. OpenAI fallback is not configured or key is missing."
            }

    except Exception as e:
        return {"error": str(e)}
