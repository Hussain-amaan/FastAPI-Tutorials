from pydantic import BaseModel , EmailStr , AnyUrl , Field , computed_field
from typing import List , Dict , Optional , Annotated

class patient(BaseModel):

    name: str
    age: int
    height:float # mtr
    weight: float # kg 
    bmi: float
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]
    married: bool



@computed_field
@property
def bmi(self) -> float:
    bmi=round(self.weight/(self.height**2),2)

    return bmi



patient_info={'name':'nitish','age' : '30' ,'height':1.65,'weight': 55 , 'bmi': 25.6 ,
              "contact_details": {"phone": "123456789 "},
               'married':True }  

patient1= patient(**patient_info)   

def insert_patient_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print('bmi',patient.bmi)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.married)
    print('inserted')




insert_patient_data(patient1)


