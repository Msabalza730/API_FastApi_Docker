# API_FastApi_Docker
Creation of API with FastAPI, MySQL and Docker

## How to run my project

- Clone this project using  http:
    - git clone https://github.com/Msabalza730/API_FastApi_Docker.git

- Create a virtual env (Windows)
```python
    - python -m venv env
    - cd env
    - .\Scripts\activate
    - cd ..
```

## Run the app with docker: 

1. Create a Mysql container:
    - docker-compose up -d mysql
    - check if it working: docker ps

2. Enter to Mysql an create the digimon table:
    - docker exec -it api_fastapi_docker-mysql-1 mysql -u root -p
    - into mysql:
    ```sql
        >> Enter password
        >> USE db_apifast
        >> CREATE TABLE digimon (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            img VARCHAR(255) NOT NULL,
            level VARCHAR(255) NOT NULL
        );
    ```

3. Run the app:
    - docker-compose up --build
    - go to: http://localhost:8000/api/digimon

