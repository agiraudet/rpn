FROM python:3.10-slim

WORKDIR /app

COPY main.py rpn.py /app/

RUN pip install fastapi uvicorn pydantic psycopg2-binary pandas SQLAlchemy fastapi-cors

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
