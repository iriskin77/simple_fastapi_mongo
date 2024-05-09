from bson.objectid import ObjectId
from students.schema import Student, student_helper
from settings import db


async def add_student(new_student: Student):
    print(new_student)
    student = await db.student_collection.insert_one(new_student)
    return str(student.inserted_id)


async def _get_student_by_id(id: str):
    print(id)
    student = await db.student_collection.find_one({"_id": ObjectId(id)})
    return student_helper(student)


async def _get_all_students():
    students = []
    async for student in db.student_collection.find():
        students.append(student_helper(student))
    return students


async def _delete_student_by_id(id: str):
    student_deleted = await db.student_collection.delete_one({"_id": ObjectId(id)})
    return student_deleted


async def _update_student(id: str, data_to_update: Student):
    data = data_to_update.dict(exclude_none=True)
    result = await db.student_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": data})
    return student_helper(result)

