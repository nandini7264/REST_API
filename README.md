# 🎓 Assignment Management API (FastAPI)

---

## 📑 Table of Contents

- [📌 Project Overview](#-project-overview)
- [🎯 Features](#-features)
- [⚙️ System Architecture](#️-system-architecture)
- [📦 Data Models](#-data-models)
- [🌐 API Endpoints](#-api-endpoints)
- [🚀 Setup & Run](#-setup--run)
- [📌 Limitations](#-limitations)
- [📁 Project Structure](#-project-structure)
- [📌 Conclusion](#-conclusion)

---

## 📌 Project Overview

This project is a RESTful API built using FastAPI to manage lesson assignments between teachers and students.  
It supports assigning lessons, retrieving incomplete assignments, and marking assignments as completed.

All data is stored in-memory during runtime.

---

## 🎯 Features

- Assign lessons to students
- Prevent duplicate lesson assignments
- Retrieve incomplete assignments per student
- Mark assignments as completed
- Input validation using Pydantic
- Structured API responses using response models

---

## ⚙️ System Architecture

```
FastAPI Application
        │
        ▼
Pydantic Models (Validation Layer)
        │
        ▼
In-Memory Storage (assignments_db list)
        │
        ▼
REST API Endpoints
```

Data Flow:

```
Client Request
    │
    ▼
Validation (Pydantic Model)
    │
    ▼
Business Logic
    │
    ▼
Update / Retrieve from assignments_db
    │
    ▼
JSON Response
```

---

## 📦 Data Models

### 1️⃣ create_assignment (Request Model)

Used for creating new assignments.

| Field       | Type |
|------------|------|
| teacher_id | str  |
| student_id | str  |
| lesson_id  | str  |

---

### 2️⃣ Assignment (Response Model)

Represents stored assignment data.

| Field       | Type    |
|------------|----------|
| teacher_id | str      |
| student_id | str      |
| lesson_id  | str      |
| completed  | bool     |

Default value for `completed` is `False`.

---

## 🌐 API Endpoints

### 🔹 POST `/assignments/`

Assign a lesson to a student.

- Prevents duplicate assignments for the same student and lesson
- Returns the created assignment object

---

### 🔹 GET `/students/{student_id}/assignments/incomplete/`

Retrieve all incomplete assignments for a student.

- Filters assignments by:
  - Matching `student_id`
  - `completed == False`

Returns a list of assignments.

---

### 🔹 PATCH `/assignments/{lesson_id}/{student_id}/complete/`

Mark an assignment as completed.

- Searches using:
  - `lesson_id`
  - `student_id`
- Updates `completed` to `True`
- Returns confirmation message

Raises HTTPException if assignment is not found.

---

## 🚀 Setup & Run

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

Interactive API documentation is available via Swagger UI.

---

## 📌 Limitations

- Data is stored in-memory (not persistent)
- No database integration
- No authentication or role validation
- Data resets when server restarts

---

## 📁 Project Structure

```
assignment-management-api/
│
├── main.py
└── README.md
```

---

### 📸 Deployment Screenshots

#### Render Dashboard
![Render Dashboard](Screenshots/Screenshot%20from%202025-05-14%2020-48-25.png)


#### Successful API Response
![API Response](Screenshots/Screenshot%20from%202025-05-14%2020-56-14.png)

---

## 📌 Conclusion

This project demonstrates:

- RESTful API development using FastAPI
- Input validation with Pydantic
- Path parameter handling
- Error handling with HTTPException
- In-memory data modeling
- Basic CRUD-style backend logic
