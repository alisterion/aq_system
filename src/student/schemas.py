from typing import Optional

from pydantic import BaseModel

from schemas.response import ResponseBase


class StudentBase(BaseModel):
    name: str
    last_name: str
    group: str


class StudentInDb(StudentBase):
    id: int = None
    created: str = None

    class Config:
        orm_mode = True


class CreateStudent(StudentInDb):
    lang: int


class UpdateStudent(StudentInDb):
    lang: int


class StudentResponse(ResponseBase):
    student: StudentInDb
    category: Optional[str]
