# Develop a simple contact form application with input fields for Name, Email, and Message. The submitted data should be securely stored in a database.


from fastapi import FastAPI,Depends
from schema import ContactCreate, ContactReasponse
from database import engine, sessionLocal
from sqlalchemy.orm  import Session
import models
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "contact form")
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close   
@app.post("/contacts", response_model=ContactReasponse)
def submit_contact(contact:ContactCreate, db:Session = Depends(get_db)):

    new_contact = models.Contact(name = contact.name,
                                 email = contact.email,
                                 message=contact.message)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact


@app.get("/contacts", response_model=list[ContactReasponse])

def submit_contact(db:Session = Depends(get_db)):

    return db.query(models.Contact).all()
