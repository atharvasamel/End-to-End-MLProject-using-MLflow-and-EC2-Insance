FROM python:3.8-slim-buster

RUN apt update && apt install -y awscli
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
