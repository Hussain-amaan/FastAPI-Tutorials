from pydantic import BaseModel , EmailStr , AnyUrl , Field , field_validator
from typing import List , Dict , Optional , Annotated

class patient(BaseModel):

    name: str
    age: int
    email: EmailStr
    linkdein: AnyUrl
    weight: float
    bmi: float
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]
    married: bool



patient_info={'name':'nitish','age' : '30' ,'email':'abc@gmail.com' ,'linkdein': 'http://linkdein.com//123' ,'weight': 60.3 , 'bmi': 25.6 ,
              "contact_details": {"phone": "123456789 "},
               'married':True }  

patient1= patient(**patient_info)   

def insert_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkdein)
    print(patient.weight)
    print(patient.bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('inserted')

def update_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('UPDATED')
 


insert_patient_data(patient1)


