from fastapi import APIRouter
from pydantic import BaseModel
import requests
import mysql.connector

router = APIRouter()

# Conection with the database
db_connection = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="db_apifast"
)
db_cursor = db_connection.cursor()


class DigimonData(BaseModel):
    """
    Data Model to store into the BD
    """
    name: str
    img: str
    level: str


@router.get("/api/digimon")
def get_and_store_digimon_data():
    """
    Enpoint to get data from Digimon API and store into local BD
    """
    try:
        digimon_url = "https://digimon-api.vercel.app/api/digimon"
        response = requests.get(digimon_url)
        digimon_data = response.json()

        if digimon_data:
            for digimon in digimon_data:
                insert_query = "INSERT INTO digimon (name, img, level) VALUES (%s, %s, %s)"
                values = (digimon["name"], digimon["img"], digimon["level"])
                db_cursor.execute(insert_query, values)

            db_connection.commit()
            return {"message": "Digimon data stored correctly in the database"}
        else:
            return {"message": "No Digimon data was fetched from the API"}
    except Exception as e:
        return {"error": f"Error getting and storing Digimon data: {str(e)}"}


@router.get("/api/digimon/{id}")
def get_digimon_by_id(id: int):
    """
    Endpoint to get a specific data record by its ID
    """
    try:
        query = "SELECT * FROM digimon WHERE id = %s"
        values = (id,)
        db_cursor.execute(query, values)
        result = db_cursor.fetchone()
        if result:
            return {"id": result[0], "name": result[1], "img": result[2], "level": result[3]}
        else:
            return {"error": "The Digimon with that ID was not found"}
    except Exception as e:
        return {"error": f"Error getting and storing Digimon data: {str(e)}"}


@router.post("/api/digimon")
def add_digimon(digimon_data: DigimonData):
    """
    Endpoint to add a new Digimon to the database
    """
    try:
        insert_query = "INSERT INTO digimon (name, img, level) VALUES (%s, %s, %s)"
        values = (digimon_data.name, digimon_data.img, digimon_data.level)
        db_cursor.execute(insert_query, values)
        db_connection.commit()
        return {"message": "Digimon successfully added to database"}
    except Exception as e:
        return {"error": f"Error getting and storing Digimon data: {str(e)}"}


@router.on_event("shutdown")
def shutdown_event():
    db_cursor.close()
    db_connection.close()

