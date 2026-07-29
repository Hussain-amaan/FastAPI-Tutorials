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


    @field_validator("email")
    @classmethod
    def email_validator(cls,value):

        Valid_domains=["icici.com" , "hdfc.com "]

        domain_name= value.split('@')[-1]


        if domain_name not in Valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
    

    @field_validator("name")
    @classmethod
    def name_validator(cls,value):
        return value.upper()

patient_info={'name':'amaan','age' : '30' ,'email':'abc@icici.com' ,'linkdein': 'http://linkdein.com//123' ,'weight': 60.3 , 'bmi': 25.6 ,
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


insert_patient_data(patient1)


