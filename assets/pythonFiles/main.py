import os
import sys
from shutil import rmtree
from flask import Flask, request

def detectorMain(url):

    path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(path)
    detectar(url)

def detectar(url):
    os.system('python detect.py --weights best.pt --conf 0.3 --source ' + url + ' --save-txt')

def convertir():
    url = "detector/runs/detect/exp/labels/label.txt"
    os.system('python convertir.py ' + url)

def reestablecer():
    dir = 'detector/runs/detect'
    rmtree(dir)

app = Flask(__name__)

@app.route('/detector', methods=['GET', 'POST'])
def detector():
    # Obtener valores
    url = request.form.get('value')
    reestablecer()
    detectorMain(url)
    convertir()

    return "detectada la imagen"
    
if __name__ == "__main__":
    app.run(debug = True, port = 5000)
