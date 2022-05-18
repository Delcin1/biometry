import os, shutil
from flask import render_template, request, redirect, url_for, abort, send_from_directory
from werkzeug.utils import secure_filename

from app import app

import track

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)


@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename)) # Валуевич: изменил относительный путь на абсолютный
        os.system(f'python track.py --source uploads/'+filename+' --yolo_model yolov5/runs/train/exp/weights/best.pt --save-vid --save-txt')
        #track.teachpython(f'uploads/'+filename) # вместо верхней строчки лучше использовать эту функцию (смотри track.py)
        os.system(f'ffmpeg -y -i runs/track/exp/video.mp4 -c:v h264 runs/track/exp/output.mp4')
        return redirect(url_for('video'))
    return redirect(url_for('index'))


@app.route('/static/<filename>')
def upload(filename):
    return send_from_directory(os.path.abspath(app.config['VIDEO_PATH']), filename)


@app.route('/video', methods=["GET", "POST"])
def video():
    if request.method == "POST":
        shutil.rmtree('runs/track/exp', ignore_errors=True)
        return redirect("/")
    return render_template('video.html')




