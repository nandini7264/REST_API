from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


#storing data in a list for runtime use only
assignments_db = []


#base model to create new assignments(PUT)
class create_assignment(BaseModel):
    teacher_id: str
    student_id: str
    lesson_id: str


#base model of the newly created assignment(GET)
class Assignment(BaseModel):
    teacher_id: str
    student_id: str
    lesson_id: str
    completed: bool = False


#assign a lesson to a student(POST)
@app.post("/assignments/", response_model=Assignment)
def assign_lesson(data: create_assignment):
    for a in assignments_db:
        if a.student_id == data.student_id and a.lesson_id == data.lesson_id:	#if assignment already exits-raise exception
            raise HTTPException(detail="This lesson is already assigned to this student.")
    
    new_assignment = Assignment(						#else create new assignment
        teacher_id=data.teacher_id,
        student_id=data.student_id,
        lesson_id=data.lesson_id,
        completed=False
    )
    assignments_db.append(new_assignment)					#append new assignment in the list
    return new_assignment


#get all incomplete assignments for a student
@app.get("/students/{student_id}/assignments/incomplete/", response_model=List[Assignment])	#this will return the list of all
												#incomplete assignments
def get_incomplete_assignments(student_id: str):
    return [a for a in assignments_db if a.student_id == student_id and not a.completed]


#mark an assignment as completed
@app.patch("/assignments/{lesson_id}/{student_id}/complete/")
def mark_assignment_complete(lesson_id: str, student_id: str):
    for a in assignments_db:
        if a.student_id == student_id and a.lesson_id == lesson_id:		#searching assignment using student_id and lesson_id
            a.completed = True
            return {"message": "Assignment marked as completed"}
    raise HTTPException(detail="Assignment not found")				#if the ids dont match we raise exception
 
