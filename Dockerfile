FROM python:3.9-slim

WORKDIR /FASTAPIPOSTGRES

ENV PYTHONUNBUFFEDER=1

COPY . /FASTAPIPOSTGRES

RUN pip install -r requirements.txt

EXPOSE 8080

CMD  ["python", "main.py"]