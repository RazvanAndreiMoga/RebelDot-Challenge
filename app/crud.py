from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import FAQ
from .openai_utils import get_embedding
import numpy as np

def add_faq(db: Session, question: str, answer: str):
    emb = get_embedding(question)
    faq = FAQ(question=question, answer=answer, embedding=emb)
    db.add(faq)
    db.commit()
    db.refresh(faq)
    return faq

def get_all_faqs(db: Session):
    return db.query(FAQ).all()

def find_most_similar(db: Session, query: str, threshold: float = 0.8):
    query_emb = get_embedding(query)
    faqs = get_all_faqs(db)

    best_match, best_score = None, -1
    for faq in faqs:
        if faq.embedding is None:
            continue
        score = cosine_similarity(query_emb, faq.embedding)
        if score > best_score:
            best_match, best_score = faq, score

    if best_score >= threshold:
        return best_match, best_score
    return None, best_score

def cosine_similarity(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
