from pydantic import BaseModel


# class Contact(BaseModel):
#     email : str
#     phone : int
# class Address(BaseModel):
#     city : str

class Customer(BaseModel):
    name : str
    role : str
    address : str
    contact : str
    # contact : Contact 

