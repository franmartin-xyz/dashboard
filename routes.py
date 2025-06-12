from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from . import crud, models
from .crud import CRUDManager
from .backend import get_db

router = APIRouter()

# Initialize CRUD manager
@router.on_event("startup")
async def init_crud_manager():
    db = next(get_db())
    crud.crud_manager = CRUDManager(db)

# Qualification Questions Routes
@router.get("/qualification-questions/{question_id}", response_model=models.QualificationQuestionBase)
async def read_qualification_question(question_id: int, db: Session = Depends(get_db)):
    return crud.crud_manager.get_qualification_question(question_id)

@router.get("/qualification-questions/", response_model=List[models.QualificationQuestionBase])
async def read_qualification_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.crud_manager.get_qualification_questions(skip=skip, limit=limit)

@router.post("/qualification-questions/", response_model=models.QualificationQuestionBase)
async def create_qualification_question(question: models.QualificationQuestionCreate, db: Session = Depends(get_db)):
    return crud.crud_manager.create_qualification_question(question)

@router.put("/qualification-questions/{question_id}", response_model=models.QualificationQuestionBase)
async def update_qualification_question(question_id: int, question: models.QualificationQuestionUpdate, db: Session = Depends(get_db)):
    return crud.crud_manager.update_qualification_question(question_id, question)

@router.delete("/qualification-questions/{question_id}")
async def delete_qualification_question(question_id: int, db: Session = Depends(get_db)):
    return crud.crud_manager.delete_qualification_question(question_id)

# Client Info Routes
@router.get("/client-info/{client_id}", response_model=models.ClientInfoBase)
async def read_client_info(client_id: int, db: Session = Depends(get_db)):
    return crud.crud_manager.get_client_info(client_id)

@router.get("/client-info/", response_model=List[models.ClientInfoBase])
async def read_client_infos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.crud_manager.get_client_infos(skip=skip, limit=limit)

@router.post("/client-info/", response_model=models.ClientInfoBase)
async def create_client_info(client_info: models.ClientInfoCreate, db: Session = Depends(get_db)):
    return crud.crud_manager.create_client_info(client_info)

@router.put("/client-info/{client_id}", response_model=models.ClientInfoBase)
async def update_client_info(client_id: int, client_info: models.ClientInfoUpdate, db: Session = Depends(get_db)):
    return crud.crud_manager.update_client_info(client_id, client_info)

@router.delete("/client-info/{client_id}")
async def delete_client_info(client_id: int, db: Session = Depends(get_db)):
    return crud.crud_manager.delete_client_info(client_id)

# Process Responses Routes
@router.get("/process-responses/{response_id}", response_model=models.ProcessResponseBase)
async def read_process_response(response_id: int, db: Session = Depends(get_db)):
    return crud.crud_manager.get_process_response(response_id)

@router.get("/process-responses/", response_model=List[models.ProcessResponseBase])
async def read_process_responses(session_id: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.crud_manager.get_process_responses(session_id=session_id, skip=skip, limit=limit)

@router.post("/process-responses/", response_model=models.ProcessResponseBase)
async def create_process_response(response: models.ProcessResponseCreate, db: Session = Depends(get_db)):
    return crud.crud_manager.create_process_response(response)

@router.put("/process-responses/{response_id}", response_model=models.ProcessResponseBase)
async def update_process_response(response_id: int, response: models.ProcessResponseUpdate, db: Session = Depends(get_db)):
    return crud.crud_manager.update_process_response(response_id, response)

@router.delete("/process-responses/{response_id}")
async def delete_process_response(response_id: int, db: Session = Depends(get_db)):
    return crud.crud_manager.delete_process_response(response_id)
