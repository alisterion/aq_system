from src.student.schemas import StudentBase, CreateStudent, UpdateStudent
from typing import Optional

from sqlalchemy.orm import Session
from db.base_class import Base
from crud.base import CRUDBase

from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship


class Student(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, unique=True, index=True)
    group = Column(String, unique=True, index=True)
    created = Column(TIMESTAMP)

    __tablename__ = "students"


class CRUDStudent(CRUDBase[Student, CreateStudent, UpdateStudent]):
    def create(self, db_session: Session, *, obj_in: CreateStudent) -> Student:
        db_obj = Student(
            name=obj_in.name,
            last_name=obj_in.last_name,
            group=obj_in.group
        )
        db_session.add(db_obj)
        db_session.commit()
        db_session.refresh(db_obj)
        return db_obj


student = CRUDStudent(Student)
