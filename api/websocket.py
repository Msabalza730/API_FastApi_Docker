from fastapi import WebSocket
from .config import DATABASE_URL
import mysql.connector

# WebSocket to view data similar to first endpoint
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

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


    db_cursor.close()
    db_connection.close()
