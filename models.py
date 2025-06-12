from pydantic import BaseModel
from typing import Optional

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
