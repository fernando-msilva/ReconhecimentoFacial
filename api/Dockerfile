FROM python:3.8-slim-buster

COPY ./src/config/* /

RUN chmod +x ./system_config.sh  \
  && /system_config.sh 

ENV LC_ALL en_US.UTF-8

COPY ./src/spyface/* /spyface/
COPY ./haarcascade_frontalface_default.xml /opt/ml/
COPY ./EigenClassifier.yml /opt/ml/

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get install -y libgl1-mesa-dev
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6
RUN apt-get install -y curl

CMD ["uvicorn", "spyface.main:app", "--host", "0.0.0.0", "--port","8080"]