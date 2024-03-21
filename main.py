import mysql.connector
from fastapi import FastAPI
from typing import Dict
from api.config import DATABASE_URL
from api.endpoints import router as digimon_router

from api.websocket import websocket_endpoint

app = FastAPI()

@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Welcome to my Digimon FastAPI App"}

# Conection with the database
db_connection = mysql.connector.connect(
    host=DATABASE_URL['host'],
    user=DATABASE_URL['user'],  
    password=DATABASE_URL['password'],
    database=DATABASE_URL['database']
)

app.include_router(digimon_router)

# WebSocket endpoint
app.add_websocket_route("/ws", websocket_endpoint)

@app.get("/api/digimon")
def get_data() -> Dict[str, str]:
    return {"message": "Hello, Digimon data!"}

# Close the conection with the db
@app.on_event("shutdown")
def shutdown_event():
    db_connection.close()
