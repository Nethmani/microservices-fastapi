# gateway/main.py

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import httpx
import jwt
import time
from typing import Optional

app = FastAPI(title="API Gateway", version="2.0.0")

# ------------------------------
# SERVICE CONFIGURATION
# ------------------------------

SERVICES = {
    "student": "http://localhost:8001",
    "course": "http://localhost:8002"
}

# ------------------------------
# JWT CONFIGURATION
# ------------------------------

JWT_SECRET = "supersecretkey"
JWT_ALGORITHM = "HS256"

security = HTTPBearer()

def create_token(username: str):
    payload = {"sub": username}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

# ------------------------------
# LOGIN ROUTE
# ------------------------------

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/auth/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin123":
        token = create_token(data.username)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# ------------------------------
# REQUEST LOGGING MIDDLEWARE
# ------------------------------

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = round((time.time() - start_time) * 1000, 2)
    print(f"{request.method} {request.url.path} -> {response.status_code} ({duration}ms)")
    return response

# ------------------------------
# FORWARD REQUEST FUNCTION
# ------------------------------

async def forward_request(service: str, path: str, method: str, json_data=None):
    if service not in SERVICES:
        raise HTTPException(status_code=404, detail="Service not found")

    url = f"{SERVICES[service]}{path}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(method, url, json=json_data)

            try:
                data = response.json() if response.text else None
            except:
                data = {"raw_response": response.text}

            if response.status_code >= 400:
                return JSONResponse(
                    status_code=response.status_code,
                    content={
                        "service": service,
                        "path": path,
                        "error": data
                    }
                )

            return JSONResponse(status_code=response.status_code, content=data)

        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Service unavailable")

# ------------------------------
# ROOT
# ------------------------------

@app.get("/")
def read_root():
    return {"message": "API Gateway is running with JWT + Logging"}

# =====================================================
# STUDENT ROUTES (SECURED)
# =====================================================

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    course: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    course: Optional[str] = None

@app.get("/gateway/students")
async def get_all_students(user=Depends(verify_token)):
    return await forward_request("student", "/api/students", "GET")

@app.get("/gateway/students/{student_id}")
async def get_student(student_id: int, user=Depends(verify_token)):
    return await forward_request("student", f"/api/students/{student_id}", "GET")

@app.post("/gateway/students")
async def create_student(student: StudentCreate, user=Depends(verify_token)):
    return await forward_request(
        "student",
        "/api/students",
        "POST",
        json_data=student.dict()
    )

@app.put("/gateway/students/{student_id}")
async def update_student(student_id: int, student: StudentUpdate, user=Depends(verify_token)):
    return await forward_request(
        "student",
        f"/api/students/{student_id}",
        "PUT",
        json_data=student.dict(exclude_unset=True)
    )

@app.delete("/gateway/students/{student_id}")
async def delete_student(student_id: int, user=Depends(verify_token)):
    return await forward_request("student", f"/api/students/{student_id}", "DELETE")

# =====================================================
# COURSE ROUTES (SECURED)
# =====================================================

class CourseCreate(BaseModel):
    title: str
    code: str
    credits: int

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None

@app.get("/gateway/courses")
async def get_all_courses(user=Depends(verify_token)):
    return await forward_request("course", "/api/courses", "GET")

@app.get("/gateway/courses/{course_id}")
async def get_course(course_id: int, user=Depends(verify_token)):
    return await forward_request("course", f"/api/courses/{course_id}", "GET")

@app.post("/gateway/courses")
async def create_course(course: CourseCreate, user=Depends(verify_token)):
    return await forward_request("course", "/api/courses", "POST", json_data=course.dict())

@app.put("/gateway/courses/{course_id}")
async def update_course(course_id: int, course: CourseUpdate, user=Depends(verify_token)):
    return await forward_request(
        "course",
        f"/api/courses/{course_id}",
        "PUT",
        json_data=course.dict(exclude_unset=True)
    )

@app.delete("/gateway/courses/{course_id}")
async def delete_course(course_id: int, user=Depends(verify_token)):
    return await forward_request("course", f"/api/courses/{course_id}", "DELETE")
