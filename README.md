# ⚙️ Microservices Architecture with API Gateway (FastAPI)

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4051B5?style=for-the-badge&logo=gunicorn&logoColor=white)
![HTTPx](https://img.shields.io/badge/HTTPx-HTTP_Client-FF6B6B?style=for-the-badge)

> A clean, beginner-friendly demonstration of the **API Gateway Pattern** using Python FastAPI — built for IT4020 Modern Topics in IT.

---

## 📋 Project Overview

This project demonstrates a simple **Microservices Architecture** where an API Gateway acts as the single entry point and forwards requests to downstream services.

| Detail | Info |
|---|---|
| 🎓 Course | IT4020 – Modern Topics in IT |
| 📅 Academic Year | Year 4 \| Semester 1 \| Practical 3 |
| 🔌 Gateway Port | `8000` |
| 🎓 Student Service Port | `8001` |
| 📚 Course Service Port | `8002` |

---

## 🏗️ System Architecture

```
Client (Browser / App)
        │
        ▼
┌───────────────────┐
│   API Gateway     │  :8000
│   (gateway/)      │
└────────┬──────────┘
         │  HTTP Forward (HTTPx)
    ┌────┴────┐
    │         │
    ▼         ▼
┌──────────┐  ┌──────────────┐
│ Student  │  │   Course     │
│ Service  │  │   Service    │
│  :8001   │  │    :8002     │
└──────────┘  └──────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Role |
|---|---|
| **FastAPI** | Web framework for building REST APIs |
| **Uvicorn** | ASGI server to run FastAPI apps |
| **HTTPx** | Async HTTP client for request forwarding |
| **Pydantic** | Data validation and serialization |

---

## 📁 Project Structure

```
microservices-fastapi/
│
├── gateway/
│   └── main.py              ← API Gateway (Port 8000)
│
├── student-service/
│   ├── main.py              ← FastAPI App Entry Point
│   ├── models.py            ← Pydantic Models
│   ├── service.py           ← Business Logic Layer
│   └── data_service.py      ← In-Memory Data Store
│
├── course-service/
│   ├── main.py              ← FastAPI App Entry Point
│   ├── models.py            ← Pydantic Models
│   ├── service.py           ← Business Logic Layer
│   └── data_service.py      ← In-Memory Data Store
│
├── venv/                    ← Virtual Environment (not committed)
├── requirements.txt         ← Python Dependencies
└── README.md                ← You are here
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Services

### Terminal 1 — Start Student Microservice

```bash
cd student-service
uvicorn main:app --reload --port 8001
```

📄 Swagger UI → [http://localhost:8001/docs](http://localhost:8001/docs)

### Terminal 2 — Start Course Microservice

```bash
cd course-service
uvicorn main:app --reload --port 8002
```

📄 Swagger UI → [http://localhost:8002/docs](http://localhost:8002/docs)

### Terminal 3 — Start API Gateway

```bash
cd gateway
uvicorn main:app --reload --port 8000
```

📄 Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testing the API

### 🎓 Student Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/gateway/students` | List all students *(via Gateway)* |
| `GET` | `/api/students` | Direct access to Student Service |
| `POST` | `/gateway/students` | Create a new student record |
| `PUT` | `/gateway/students/{id}` | Update an existing student |
| `DELETE` | `/gateway/students/{id}` | Delete a student record |

### 📚 Course Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/gateway/courses` | List all courses *(via Gateway)* |
| `GET` | `/api/courses` | Direct access to Course Service |
| `POST` | `/gateway/courses` | Create a new course record |
| `PUT` | `/gateway/courses/{id}` | Update an existing course |
| `DELETE` | `/gateway/courses/{id}` | Delete a course record |

> ✅ All endpoints can be tested interactively via **Swagger UI**

---

## 💡 Key Concepts

- **API Gateway Pattern** — Single entry point that routes requests to internal services
- **Microservices Architecture** — Services are independently developed and deployed
- **Request Forwarding** — The gateway uses HTTPx to proxy requests asynchronously
- **RESTful CRUD APIs** — Full Create, Read, Update, Delete operations over HTTP
- **Independent Service Deployment** — Each service runs on its own port and process

---

## 🙈 .gitignore

Make sure your repo includes this `.gitignore`:

```
venv/
__pycache__/
*.pyc
.env
*.egg-info/
```

---

<div align="center">
  <sub>Built for academic purposes — IT4020 Modern Topics in IT</sub>
</div>
