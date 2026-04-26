# fastapi_notes.py

"""
===============================
FASTAPI + PYDANTIC NOTES
===============================

1. WHAT IS FASTAPI?
-------------------
- FastAPI is a modern Python web framework to build APIs.
- Uses type hints for validation.
- Works with Pydantic for data validation.

--------------------------------

2. BASIC APP
-------------------
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

--------------------------------

3. PATH PARAMETERS
-------------------
@app.get("/patient/{patient_id}")
def get_patient(patient_id: str):
    return {"id": patient_id}

--------------------------------

4. QUERY PARAMETERS
-------------------
@app.get("/sort")
def sort_patient(sort_by: str, order: str = "asc"):
    return {"sort_by": sort_by, "order": order}

--------------------------------

5. PYDANTIC MODEL
-------------------
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

--------------------------------

6. FIELD VALIDATION
-------------------
from pydantic import Field

age: int = Field(gt=0, lt=120)

--------------------------------

7. LITERAL (FIXED VALUES)
-------------------
from typing import Literal

gender: Literal["Male", "Female", "Others"]

--------------------------------

8. COMPUTED FIELDS
-------------------
from pydantic import computed_field

@computed_field
@property
def bmi(self):
    return self.weight / (self.height ** 2)

--------------------------------

9. CRUD OPERATIONS
-------------------
CREATE → POST
READ   → GET
UPDATE → PUT
DELETE → DELETE

--------------------------------

10. POST (CREATE)
-------------------
@app.post("/create")
def create_patient(patient: Patient):
    return {"message": "Created"}

--------------------------------

11. GET (READ)
-------------------
@app.get("/view")
def view():
    return data

--------------------------------

12. PUT (UPDATE)
-------------------
@app.put("/edit/{patient_id}")
def update_patient(patient_id: str):
    return {"message": "Updated"}

--------------------------------

13. DELETE
-------------------
@app.delete("/patient/{patient_id}")
def delete_patient(patient_id: str):
    return {"message": "Deleted"}

--------------------------------

14. JSON HANDLING
-------------------
import json

def load_data():
    with open("patients.json") as f:
        return json.load(f)

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)

--------------------------------

15. IMPORTANT CONCEPTS
-------------------
- Pydantic validates data automatically
- Data types must match exactly
- Literal is case-sensitive
- Use model_dump() for serialization
- Computed fields auto-calculate values

--------------------------------

16. COMMON ERRORS (YOU FACED)
-------------------
- Dict[str] → should be Dict[str, type]
- Wrong file name (.id instead of .json)
- Case mismatch ("female" vs "Female")
- Typo in Field(default)
- Missing () in function calls

--------------------------------

17. BEST PRACTICES
-------------------
- Use lowercase field names (age, gender)
- Keep models consistent
- Validate inputs properly
- Use proper status codes (200, 201, 404)

--------------------------------

END OF NOTES
"""