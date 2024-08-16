from models.employee import Employee as EmployeeModel
from schemas.employee import Employee

class EmployeeService():
    def __init__(self, db) -> None:
        self.db = db

    def get_employees(self):
        result = self.db.query(EmployeeModel).all()
        return result
    
    def get_employee(self, employee_id):
        result = self.db.query(EmployeeModel).filter(EmployeeModel.employee_id == employee_id).first()
        return result
    
    def create_employee(self, employee: Employee):
        new_employee = EmployeeModel(**employee.model_dump())
        self.db.add(new_employee)
        self.db.commit()
        return new_employee
    
    def update_employee(self, employee_id: int, data: Employee):
        try:
            employee = self.db.query(EmployeeModel).filter(EmployeeModel.employee_id == employee_id).first()
            employee.employee_id = data.employee_id
            employee.employee_name = data.employee_name
            employee.employee_last_name = data.employee_last_name
            employee.employee_email = data.employee_email
            employee.employee_password = data.employee_password
            employee.job_position = data.job_position
            employee.salary = data.salary
            self.db.commit()
        except Exception as e:
            return {"message":str(e)}
        finally:
            self.db.close()

    def delete_employee(self, employee_id: int):
        self.db.query(EmployeeModel).filter(EmployeeModel.employee_id == employee_id).delete()
        self.db.commit()
        return