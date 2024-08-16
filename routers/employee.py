from fastapi import APIRouter
from fastapi import Path, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder

from models.employee import Employee as EmployeeModel
from services.employee import EmployeeService
from schemas.employee import Employee

employee_router = APIRouter()

#---------------------------------------- Create employee ----------------------------------------#
    
@employee_router.post('/create_employee', tags=['employee'], response_model=dict)
def create_employee(employee : Employee) -> dict:
    try:
        db = Session()
        EmployeeService(db).create_employee(employee)
        return JSONResponse(status_code=201, content={"message": "Employee created successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

#---------------------------------------- Get employees ----------------------------------------#

@employee_router.get('/get_employees', tags=['employee'], response_model=List[Employee], status_code=200)
def get_employees() -> List[Employee]:
    try:
        db = Session()
        result = EmployeeService(db).get_employees()
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    
#---------------------------------------- Get employee ----------------------------------------#

@employee_router.get('/get_employee/{employee_id}', tags=['employee'], response_model=Employee)
def get_employee(employee_id : int) -> Employee:
    try:
        db = Session()
        result = EmployeeService(db).get_employee(employee_id)
        if not result:
            return JSONResponse(status_code=404, content={"message": "Employee not found"})
        return JSONResponse(status_code=200, content=jsonable_encoder(result))
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
    
#---------------------------------------- Update employee ----------------------------------------#

@employee_router.put('/update_employee/{employee_id}', tags=['employee'], response_model=dict)
def update_employee(employee_id : int, employee : Employee) -> dict:
    try:
        db = Session()
        result = EmployeeService(db).get_employee(employee_id)
        if not result:
            return JSONResponse(status_code=404, content={"message": "Employee not found"})
        EmployeeService(db).update_employee(employee_id, employee)
        return JSONResponse(content={"message": "Employee updated successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

#---------------------------------------- Delete customer ----------------------------------------#

@employee_router.delete('/delete_employee/{employee_id}', tags=['employee'], response_model=dict)
def delete_employee(employee_id : int) -> dict:
    try:
        db = Session()
        result : EmployeeModel = db.query(EmployeeModel).filter(EmployeeModel.employee_id == employee_id).first()
        if not result:
            return JSONResponse(status_code=404, content={"message": "Employee not found"})
        EmployeeService(db).delete_employee(employee_id)
        return JSONResponse(content={"message": "Employee deleted successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})