from fastapi import APIRouter
from fastapi import Path, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.customer import Customer as CustomerModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.customer import CustomerService
from schemas.customer import Customer

customer_router = APIRouter()

#---------------------------------------- Create customer ----------------------------------------#
@customer_router.post('/create_customer', tags=['customer'], response_model=dict)
def create_customer(customer: Customer) -> dict:
    db = Session()
    CustomerService(db).create_customer(customer)
    return JSONResponse(status_code=201, content={"message": "The customer was added"})

#---------------------------------------- Get customers ----------------------------------------#
@customer_router.get('/get_customers', tags=['customer'], response_model=List[Customer], dependencies=[Depends(JWTBearer())])
def get_customers() -> List[Customer]:
    db = Session()
    result = CustomerService(db).get_customers()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#---------------------------------------- Get customer ----------------------------------------#
@customer_router.get('/get_customer/{customer_id}', tags=['customer'], response_model=Customer)
def get_customer(customer_id: int) -> Customer:
    db = Session()
    result = CustomerService(db).get_customer(customer_id)
    if not result:
        return JSONResponse(status_code=404, content={'message': f'Could not find the customer with id: {customer_id}'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#---------------------------------------- Update customer ----------------------------------------#

@customer_router.put('/update_customer/{customer_id}', tags=['customer'], response_model=dict)
def update_customer(customer_id: int, customer: Customer) -> dict:
    try:
        db = Session()
        result = CustomerService(db).get_customer(customer_id)
        if not result:
            return JSONResponse(status_code=404, content={'message': 'Could not find the customer'})
        CustomerService(db).update_customer(customer_id, customer)
        return {"message": "The customer was updated"}
    except Exception as e:
        return JSONResponse(content={"message": str(e)})

#---------------------------------------- Delete customer ----------------------------------------#
@customer_router.delete('/delete_customer/{customer_id}', tags=['customer'], response_model=dict)
def delete_customer(customer_id: int) -> dict:
    try:
        db = Session()
        result : CustomerModel = db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()
        if not result:
            return JSONResponse(status_code=404, content={'message': f'Could not find the customer'})
        CustomerService(db).delete_customer(customer_id)
        return JSONResponse(status_code=200, content={"message": "The customer was deleted"})
    except Exception as e:
        return JSONResponse(content={"message": str(e)})