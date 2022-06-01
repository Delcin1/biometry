# create docker image for our app docker build --tag biometry .
<<<<<<< HEAD
# run app: docker compose up
FROM ubuntu:latest
=======
# run app: docker-compose up
FROM python:3.8
>>>>>>> a08247c4e6106cac0e0f1baa2542de4e44784005

ENV LD_LIBRARY_PATH=/usr/local/lib
<<<<<<< HEAD
COPY --from=jrottenberg/ffmpeg /usr/local /usr/local/
RUN apt install -y python3-pip
RUN alias python=python3
#RUN apt-get install -y libqt5gui5 && \
    #rm -rf /var/lib/apt/lists/*
ENV QT_DEBUG_PLUGINS=1

COPY . .
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
=======

ENV QT_DEBUG_PLUGINS=1

COPY . .

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6 libqt5gui5 libopencv-dev -y && \
    pip install opencv-python-headless && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

>>>>>>> a08247c4e6106cac0e0f1baa2542de4e44784005
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
