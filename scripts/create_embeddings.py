from app.db import SessionLocal
from app.models import FAQ
from app.openai_utils import get_embedding

db = SessionLocal()
faqs = db.query(FAQ).all()

for faq in faqs:
    faq.embedding = get_embedding(faq.question)
    db.add(faq)

db.commit()
db.close()
