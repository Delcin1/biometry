git clone --recurse-submodules https://gitlab.com/DelcinNikita/biometry.git

If you already cloned and forgot to use --recurse-submodules you can run git submodule update --init

Make sure that you fulfill all the requirements: Python 3.8 or later with all requirements.txt dependencies installed, including torch>=1.7. To install, run:
pip install -r requirements.txt

Run tracking:
python track.py --source 0 --yolo_model yolov5\runs\train\exp\weights\best.pt

Run web service:
flask run
