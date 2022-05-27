# create docker image for our app docker build --tag biometry .
# run app: docker compose up
FROM python:3.8

RUN apt-get update
#RUN apt-get install ffmpeg libsm6 libxext6  -y
#RUN apt-get install libssl1.0.0 libssl-dev\
#RUN nano /etc/apt/sources.list
#RUN add deb http://security.ubuntu.com/ubuntu bionic-security main
#RUN apt update && apt-cache policy libssl1.0-dev
#RUN apt-get install libssl1.0.0 libssl-dev
#RUN cd /lib/x86_64-linux-gnu
#RUN ln -s libssl.so.1.0.0 libssl.so.10
#RUN ln -s libcrypto.so.1.0.0 libcrypto.so.10
ENV LD_LIBRARY_PATH=/usr/local/lib
COPY --from=jrottenberg/ffmpeg /usr/local /usr/local/

RUN apt-get install -y libqt5gui5 && \
    rm -rf /var/lib/apt/lists/*
ENV QT_DEBUG_PLUGINS=1

COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]