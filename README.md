# REST_API

##Assignment Management API

This is a RESTful API built using FASTAPI to manage assignments for students at V-School.
The API allows assigning lessons to students, retrieving incomplete assignments and marking completed assignments.
Tested them using Postman Agent as well as Swagger UI.

- Creae new asisgnments (POST /assignments/) : Teachers assign lessons to students
- Get incomplete assignments (GET /students/{student_id}/assignments/incomplete/) : Returns a list of all the incomplete assignments of a student
- Mark when an assignment is completed (PATCH /assignments/{lesson_id}/{student_id}/complete/) : Mark a specific assignment as completed.
