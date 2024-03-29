FROM python:3.9

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

#COPY ./main.py /app/
#COPY ./__init__.py /app/

COPY . .
EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
