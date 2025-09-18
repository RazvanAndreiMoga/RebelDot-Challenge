from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .db import get_db
from .crud import find_most_similar
from .schemas import QuestionRequest, AnswerResponse
from .deps import get_token
from .openai_utils import ask_openai

router = APIRouter()

@router.post("/ask-question", response_model=AnswerResponse)
def ask_question(payload: QuestionRequest, db: Session = Depends(get_db), token: str = Depends(get_token)):
    faq, score = find_most_similar(db, payload.user_question)

    if faq:
        return {
            "source": "local",
            "matched_question": faq.question,
            "answer": faq.answer
        }

    openai_answer = ask_openai(payload.user_question)
    return {
        "source": "openai",
        "matched_question": "N/A",
        "answer": openai_answer
    }
