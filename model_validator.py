from pydantic import BaseModel , EmailStr , AnyUrl , Field , model_validator
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


    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact_details:
            raise ValueError('Patient older than 60 should have emergency contact number')
        return self



   

patient_info={'name':'amaan','age' : '65' ,'email':'abc@icici.com' ,'linkdein': 'http://linkdein.com//123' ,'weight': 60.3 , 'bmi': 25.6 ,
              "contact_details": {"phone": "123456789 ","emergency":"12345678"} ,
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


insert_patient_data(patient1)


