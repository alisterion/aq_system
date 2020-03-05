from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.student import models
from src.student.models import CreateStudent
from src.student.schemas import StudentResponse
from utils.db import get_db

router = APIRouter()


@router.post("/createstudent", response_model=StudentResponse, tags=["student"])
def create_student(
        student_in: CreateStudent,
        db: Session = Depends(get_db)
):
    student = models.student.create(db, obj_in=student_in)

    return StudentResponse(student=student)
