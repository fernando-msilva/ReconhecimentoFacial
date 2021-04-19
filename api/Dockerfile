FROM python:3.8-slim-buster

COPY ./requirements.txt requirements.txt
COPY ./src/config/* /

RUN chmod +x ./system_config.sh  \
  && /system_config.sh 

ENV LC_ALL en_US.UTF-8

COPY ./src/py/* ./src/main/main.py /app/
COPY ./haarcascade_frontalface_default.xml /opt/ml/
COPY ./EigenClassifier.yml /opt/ml/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port","8080"]