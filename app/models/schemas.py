from pydantic import BaseModel, validator
from typing import List, Union

class QuestionInput(BaseModel):
    questions: List[str]
    
    @validator("questions", each_item=True)
    def check_question_not_empty(cls, question):
        if not question.strip():
            raise ValueError("Empty questions are not allowed.")
        return question
    

class AnswerOutput(BaseModel):
    question: str
    answer: str
