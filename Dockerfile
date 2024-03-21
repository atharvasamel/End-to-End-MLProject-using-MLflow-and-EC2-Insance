FROM python:3.8-slim-buster

RUN opt update -y && opt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD [ "python3", "app.py" ]