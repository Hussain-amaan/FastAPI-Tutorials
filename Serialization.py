from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Amaan", age=22)

# Dict
print(user.model_dump())

# JSON
print(user.model_dump_json())