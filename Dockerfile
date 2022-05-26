FROM python:3.9.5-slim-buster

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run", "--host=127.0.0.1", "--port=5000"]