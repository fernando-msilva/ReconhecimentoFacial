FROM python:3.8-slim-buster
WORKDIR /spyface
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN apt-get update && apt-get install libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6 -y
COPY ./src .
VOLUME [ "/spyface/storage/imagens" ]
CMD [ "python", "-u", "Testagem.py" ]