from fastapi import FastAPI, WebSocket
from api.config import DATABASE_URL
import mysql.connector


app = FastAPI()

# WebSocket to view data similar to first endpoint
@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Welcome to the WebSocket!")

    try:
        # Conection with the database
        db_connection = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root",
            database="db_apifast"
        )
        db_cursor = db_connection.cursor()

        query = "SELECT * FROM data"
        db_cursor.execute(query)
        results = db_cursor.fetchall()
        for row in results:
            await websocket.send_text(f"ID: {row[0]}, Data: {row[1]}")

    finally:
        if db_cursor:
            db_cursor.close()
        if db_connection:
            db_connection.close()
