from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, BackgroundTasks, Body
from fastapi.encoders import jsonable_encoder

from .schema import Student
from students.service import add_student, _get_student_by_id, _get_all_students, _delete_student_by_id, _update_student


router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: Student = Body(...)):
    student = jsonable_encoder(student)
    new_student_id = await add_student(student)
    return new_student_id


@router.get("/{id}")
async def get_student_by_id(id: str):
    student = await _get_student_by_id(id=id)
    print(student)
    #res = jsonable_encoder(student)
    return student


@router.get("/")
async def get_all_students():
    students = await _get_all_students()
    return students


@router.delete("/")
async def delete_user(id: str):
    res = await _delete_student_by_id(id=id)
    return True


@router.patch("/{id}")
async def update_user(id: str, data: Student):
    res = await _update_student(id=id, data_to_update=data)
    return res
