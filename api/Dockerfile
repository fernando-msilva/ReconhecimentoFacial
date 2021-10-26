FROM  fernandogbi/spyface-base AS dev
COPY ./src/config /
RUN chmod +x ./system_config.sh  \
  && /system_config.sh 
ENV LC_ALL en_US.UTF-8
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["uvicorn", "spyface.main:app", "--host", "0.0.0.0", "--port","8080"]
EXPOSE 8080

FROM dev as prod
COPY ./src/spyface /spyface/