import os

from dotenv import load_dotenv
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.models.schemas import QuestionInput, AnswerOutput
from app.services.qa_service import QuestionAnsweringService
from app.utils.rate_limiter import rate_limiter
from app.utils.file_loader import load_document

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

router = APIRouter()


@router.post("/question-answer/", response_model=list[AnswerOutput], dependencies=[Depends(rate_limiter)])
async def question_answer(questions: QuestionInput, document: UploadFile = File(...)):
    try:
        # Load document content
        doc_text = await load_document(document)
        
        # Get answers
        qas = QuestionAnsweringService(doc_text, openai_api_key)
        answers = qas.answer_questions(questions.questions)
        return answers
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
