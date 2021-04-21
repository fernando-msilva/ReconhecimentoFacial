FROM python:3.8-slim-buster as dev
COPY ./src/config/* /
RUN chmod +x ./system_config.sh  \
  && /system_config.sh 
ENV LC_ALL en_US.UTF-8
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["uvicorn", "spyface.main:app", "--host", "0.0.0.0", "--port","8080"]
EXPOSE 8080

FROM dev as prod
COPY ./src/spyface/* /spyface/
COPY ./haarcascade_frontalface_default.xml /opt/ml/
COPY ./EigenClassifier.yml /opt/ml/