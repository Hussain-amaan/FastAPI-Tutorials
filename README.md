# 🚀 FastAPI Learning Notes 



This repository contains my learning and practice of **FastAPI**, a modern Python framework for building high-performance APIs.

---

## 🧠 What is FastAPI?

**FastAPI** is a Python web framework used to build APIs quickly and efficiently.

### 🔑 Key Features:

* ⚡ High performance (built on Starlette & ASGI)
* 🧠 Automatic data validation using Pydantic
* 📄 Auto-generated API documentation (Swagger & ReDoc)
* 🧾 Uses Python type hints
* 🚀 Easy to learn and use

---

## 📌 Core Concepts Covered

### 🔹 1. Basic API

```python id="k1bq2l"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
```

---

### 🔹 2. Path Parameters

```python id="0vbbt0"
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

---

### 🔹 3. Query Parameters

```python id="cw8n74"
@app.get("/items/")
def get_items(limit: int = 10):
    return {"limit": limit}
```

---

### 🔹 4. Request Body (Pydantic)

```python id="u4rj4j"
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
```

---

### 🔹 5. Validation with Field

```python id="n2dsmn"
from pydantic import Field

age: int = Field(gt=0, lt=120)
```

---

### 🔹 6. Response Handling

* FastAPI automatically converts Python objects → JSON
* Uses Pydantic for serialization

---

### 🔹 7. CRUD Operations

| Operation | Method |
| --------- | ------ |
| Create    | POST   |
| Read      | GET    |
| Update    | PUT    |
| Delete    | DELETE |

---

### 🔹 8. Error Handling

```python id="nx7pxf"
from fastapi import HTTPException

if not found:
    raise HTTPException(status_code=404, detail="Item not found")
```

---

### 🔹 9. API Documentation

FastAPI automatically provides:

* Swagger UI → `/docs`
* ReDoc → `/redoc`

---

## ▶️ How to Run

### 1. Install dependencies

```bash id="f9r3u3"
pip install fastapi uvicorn
```

---

### 2. Run the server

```bash id="n8pnk1"
uvicorn main:app --reload
```

---

### 3. Open in browser

```id="6o0rli"
http://127.0.0.1:8000/docs
```



---

## 📈 What I Learned

* Building APIs using FastAPI
* Handling requests and responses
* Data validation with Pydantic
* Understanding REST principles
* Debugging backend errors

---

## 🚀 Why FastAPI?

* Faster than Flask in many cases
* Built-in validation (no extra libraries needed)
* Automatic API documentation
* Clean and readable code



---



## ⭐ Summary

FastAPI is a powerful and modern framework that simplifies API development using Python.
It combines **speed, validation, and simplicity**, making it ideal for real-world applications.

---
