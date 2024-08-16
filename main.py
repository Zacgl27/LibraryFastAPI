'''
python -m venv venv - para el virtual enviroment
venv/Scripts/activate
pip install fastapi
pip install uvicorn
pip install pyjwt
pip install sqlalchemy
pip > freeze requirements.txt
'''

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import Base, engine
from middlewares.error_handler import ErrorHandler

from routers.customer import customer_router
from routers.employee import employee_router

app = FastAPI()
app.title = "Sanctuary"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(customer_router)
app.include_router(employee_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['Home'])
def read_root():
    return HTMLResponse('<h1>Welcome to Books Sanctuary</h1>')