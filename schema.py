from pydantic import BaseModel,EmailStr

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    message:str

class ContactReasponse(BaseModel):
    id:int


    class config:
        orm_mode= True    