FROM python:3.9.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py /app

EXPOSE 8080

CMD [ "python3", "./app.py" ]
