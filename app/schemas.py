from pydantic import BaseModel

class QuestionRequest(BaseModel):
    user_question: str

class AnswerResponse(BaseModel):
    source: str
    matched_question: str
    answer: str
