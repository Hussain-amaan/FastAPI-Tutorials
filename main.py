from fastapi import FastAPI , Path , HTTPException , Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from typing import Annotated , Literal , Optional

import json


app=FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description=(" ID of the Patinet"),examples=['P001'])]
    name: Annotated[str,Field(...,description=("Enter the name of Patient"))]
    city:Annotated[str,Field(...,description=("Enter the City Name"))]
    age:Annotated[int,Field(gt=0,lt=120,description=("Enter the age of Patient"))]
    gender:Annotated[Literal['male','female','Others'],Field(...,description=("Enter the Gender of Patient"))]
    height:Annotated[float,Field(...,gt=0,description=("Enter Height of Patient in Mtrs"))]
    weight:Annotated[float,Field(...,gt=0,description=("Enter weight of Patient in Kgs "))]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi=round(self.weight/(self.height**2))
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'underweight'
        elif self.bmi < 25:
            return 'normal'
        elif self.bmi <30:
            return 'normal'

        else :
            return 'obese' 
 
class patientUpdate(BaseModel):
    name: Annotated[Optional[str],Field(default=None)]
    city:Annotated[Optional[str],Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male','female','Others']], Field(default=None)]
    
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]



@app.put("/edit/{patient_id}")
def update_patient(patient_id:str,patient_update:patientUpdate):

    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail="patient not found")
    
    existing_patient_info=data[patient_id]

    updated_patient_info=patient_update.model_dump(exclude_unset=True)

    for key,value in updated_patient_info.items():
        existing_patient_info[key]=value

    # existing_patient_info->pydantic object->updated bmi + verdict -> pydantic object -> dict
    
    existing_patient_info['id']=patient_id
    patient_pydantic_object = Patient(**existing_patient_info)
    
    existing_patient_info=patient_pydantic_object.model_dump(exclude='id')

    # add this dict to data 

    data[patient_id]= existing_patient_info

    # save data 

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'Patient updated'})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):

    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail='patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200,content={'message':'patient deleted'})
                        




def load_data():
    with open("patients.json","r") as f:
        data = json.load(f)

        return data
    

def save_data(data):
    with open("patients.json","w") as f:
        json.dump(data,f)


@app.get("/")
def hello():
    return{'message':'Patient Manageent System API'}

@app.get("/about")
def about():
    return{'message':'A fully Functional API to manage patients record'}


@app.get("/view")
def view():
    data=load_data()

    return data 



@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path (..., description="ID of the patients in the DB ", examples= " P001")):
    # load patients
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")


@app.get("/sort")
def sort_patient(sort_by : str=Query(..., description="sort on the basis of height , weight or bmi"), 
                 order : str= Query("asc" , description="sort in ascending or descending  orders")):
    
    valid_fields=["height","weight","bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid field . select  from{valid_fields}")
    
    if order not in ["asc","desc"]:
        raise HTTPException(status_code=400 , detail="select between asc or desc")
    

    data=load_data()
    

    sort_order= True if order=="desc" else False

    sorted_data = sorted(data.values() , key=lambda x: x.get(sort_by,0),reverse=sort_order)

    return sorted_data

@app.post('/create')
def create_patient(patient:Patient):

    data=load_data()
 # check paatient exists or not 
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')
    
    # new patient add to data base
    data[patient.id]=patient.model_dump(exclude=['id'])
    
 # save into json file 
    save_data(data)


    return JSONResponse(status_code=201,content={"message":"Patient created successfully"})




   
