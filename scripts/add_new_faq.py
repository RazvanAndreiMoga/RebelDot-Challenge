from app.db import SessionLocal
from app.models import FAQ
from app.openai_utils import get_embedding

db = SessionLocal()

question = "How do I update my billing information?"
answer = "Navigate to account settings, then select 'Billing' to update your payment details."

emb = get_embedding(question)
faq = FAQ(question=question, answer=answer, embedding=emb)
db.add(faq)
db.commit()
db.close()
