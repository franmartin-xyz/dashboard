from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import and_, text
from pydantic import BaseModel
from fastapi import HTTPException, status

# Get the automapped classes from backend
from backend import Base, QualificationQuestion, ClientInfo, ProcessResponse

# Pydantic models for request validation

class QualificationQuestionBase(BaseModel):
    question_text: str
    phase_id: int
    is_active: bool = True

class QualificationQuestionCreate(QualificationQuestionBase):
    pass

class QualificationQuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    phase_id: Optional[int] = None
    is_active: Optional[bool] = None

class ClientInfoBase(BaseModel):
    company_name: str
    website_url: str
    industry: str
    contact_first_name: str
    contact_last_name: str
    contact_email: str
    number_employees: int
    number_clients: int
    sells_product: bool
    sells_service: bool
    description: str

class ClientInfoCreate(ClientInfoBase):
    pass

class ClientInfoUpdate(BaseModel):
    company_name: Optional[str] = None
    website_url: Optional[str] = None
    industry: Optional[str] = None
    contact_first_name: Optional[str] = None
    contact_last_name: Optional[str] = None
    contact_email: Optional[str] = None
    number_employees: Optional[int] = None
    number_clients: Optional[int] = None
    sells_product: Optional[bool] = None
    sells_service: Optional[bool] = None
    description: Optional[str] = None

class ProcessResponseBase(BaseModel):
    session_id: str
    question: str
    answer: str

class ProcessResponseCreate(ProcessResponseBase):
    pass

class ProcessResponseUpdate(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None

class CRUDManager:
    def __init__(self, db: Session):
        self.db = db

    # Qualification Questions CRUD
    def get_qualification_question(self, question_id: int):
        return self.db.query(QualificationQuestion).filter(
            QualificationQuestion.id == question_id
        ).first()

    def get_qualification_questions(self, skip: int = 0, limit: int = 100):
        return self.db.query(QualificationQuestion).offset(skip).limit(limit).all()

    def create_qualification_question(self, question: QualificationQuestionCreate):
        db_question = QualificationQuestion(**question.dict())
        self.db.add(db_question)
        self.db.commit()
        self.db.refresh(db_question)
        return db_question

    def update_qualification_question(self, question_id: int, question: QualificationQuestionUpdate):
        db_question = self.get_qualification_question(question_id)
        if not db_question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        update_data = question.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_question, key, value)
        
        self.db.commit()
        self.db.refresh(db_question)
        return db_question

    def delete_qualification_question(self, question_id: int):
        db_question = self.get_qualification_question(question_id)
        if not db_question:
            raise HTTPException(status_code=404, detail="Question not found")
        
        self.db.delete(db_question)
        self.db.commit()
        return {"message": "Question deleted successfully"}

    # Client Info CRUD
    def get_client_info(self, client_id: int):
        return self.db.query(ClientInfo).filter(
            ClientInfo.id == client_id
        ).first()

    def get_client_infos(self, skip: int = 0, limit: int = 100):
        return self.db.query(ClientInfo).offset(skip).limit(limit).all()

    def create_client_info(self, client_info: ClientInfoCreate):
        db_client = ClientInfo(**client_info.dict())
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def update_client_info(self, client_id: int, client_info: ClientInfoUpdate):
        db_client = self.get_client_info(client_id)
        if not db_client:
            raise HTTPException(status_code=404, detail="Client info not found")
        
        update_data = client_info.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_client, key, value)
        
        self.db.commit()
        self.db.refresh(db_client)
        return db_client

    def delete_client_info(self, client_id: int):
        db_client = self.get_client_info(client_id)
        if not db_client:
            raise HTTPException(status_code=404, detail="Client info not found")
        
        self.db.delete(db_client)
        self.db.commit()
        return {"message": "Client info deleted successfully"}

    # Process Responses CRUD
    def get_process_response(self, response_id: int):
        return self.db.query(ProcessResponse).filter(
            ProcessResponse.id == response_id
        ).first()

    def get_process_responses(self, session_id: Optional[str] = None, skip: int = 0, limit: int = 100):
        query = self.db.query(ProcessResponse)
        if session_id:
            query = query.filter(ProcessResponse.session_id == session_id)
        return query.offset(skip).limit(limit).all()

    def create_process_response(self, response: ProcessResponseCreate):
        db_response = ProcessResponse(**response.dict())
        self.db.add(db_response)
        self.db.commit()
        self.db.refresh(db_response)
        return db_response

    def update_process_response(self, response_id: int, response: ProcessResponseUpdate):
        db_response = self.get_process_response(response_id)
        if not db_response:
            raise HTTPException(status_code=404, detail="Response not found")
        
        update_data = response.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_response, key, value)
        
        self.db.commit()
        self.db.refresh(db_response)
        return db_response

    def delete_process_response(self, response_id: int):
        db_response = self.get_process_response(response_id)
        if not db_response:
            raise HTTPException(status_code=404, detail="Response not found")
        
        self.db.delete(db_response)
        self.db.commit()
        return {"message": "Response deleted successfully"}