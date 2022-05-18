import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-am-god-of-dota'
    UPLOAD_EXTENSIONS = ['.mp4', '.mov', '.avi', '.mkv', '.flv']
    UPLOAD_PATH = 'uploads'
    VIDEO_PATH = 'runs/track/exp'

