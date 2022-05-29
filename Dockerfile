# create docker image for our app docker build --tag biometry .
# run app: docker-compose up
FROM python:3.8

ENV LD_LIBRARY_PATH=/usr/local/lib

ENV QT_DEBUG_PLUGINS=1

COPY . .

RUN apt-get update && \
    apt-get install ffmpeg libsm6 libxext6 libqt5gui5 libopencv-dev -y && \
    pip install opencv-python-headless && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
