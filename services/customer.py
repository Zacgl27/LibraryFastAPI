from models.customer import Customer as CustomerModel
from schemas.customer import Customer

class CustomerService():

    def __init__(self, db) -> dict:
        self.db = db

    def get_customers(self):
        result = self.db.query(CustomerModel).all()
        return result
    
    def get_customer(self, customer_id):
        result = self.db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()
        return result
    
    def create_customer(self, customer: Customer):
        new_customer = CustomerModel(**customer.model_dump())
        self.db.add(new_customer)
        self.db.commit()
        return new_customer
    
    def update_customer(self, customer_id: int, data: Customer):
        try:            
            customer = self.db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).first()
            customer.customer_id = data.customer_id
            customer.customer_name = data.customer_name
            customer.customer_last_name = data.customer_last_name
            customer.customer_email = data.customer_email
            customer.customer_password = data.customer_password
            customer.customer_address = data.customer_address
            self.db.commit()
        except Exception as e:
            return {"g": f"error{e}"}
        finally:
            self.db.close()
    
    def delete_customer(self, customer_id: int):
        self.db.query(CustomerModel).filter(CustomerModel.customer_id == customer_id).delete()
        self.db.commit()
        return  