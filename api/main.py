import mysql.connector
from fastapi import FastAPI

from .config import DATABASE_URL
from .endpoints import router as digimon_router

#from .websocket import websocket_endpoint

app = FastAPI()

# Conection with the database
db_connection = mysql.connector.connect(
    host=DATABASE_URL['host'],
    user=DATABASE_URL['root'],
    password=DATABASE_URL['root'],
    database=DATABASE_URL['db_apifast']
)

app.include_router(digimon_router)

# Close the conection with the db
@app.on_event("shutdown")
def shutdown_event():
    db_connection.close()
