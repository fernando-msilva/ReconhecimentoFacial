FROM  fernandogbi/spyface-base AS dev
WORKDIR /spyface
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN apt-get update && apt-get install libgl1-mesa-dev libglib2.0-0 libsm6 libxrender1 libxext6 -y
VOLUME [ "/spyface/storage/imagens" ]
CMD [ "python", "-u", "Testagem.py" ]

FROM dev AS prod
COPY ./src /spyface