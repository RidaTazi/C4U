import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from MoneyDetect import getMoneyValue
import requests
from ColorDetect import DominantColors


UPLOAD_FOLDER = '/home/Arty0091/mysite/Uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/money', methods=['POST'])
def moneyDetect():
    # return "Money detect"
    if request.method == 'POST':
        if len(request.files)==0:
            return "Empty request body"
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "Request not OK"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return "No file uploaded"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            value=getMoneyValue(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("-----money------"+ value)
            return value
    else:
    	return "Method not supported"

@app.route('/color', methods=['POST'])
def colorDetect():
    if request.method == 'POST':
        if len(request.files)==0:
            return "Empty request body"
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "Request not OK"
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return "No file uploaded"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            myImage=os.path.join(app.config['UPLOAD_FOLDER'], filename)
            dc = DominantColors(myImage, 5)
            colors = dc.dominantColors()
            (a,b,c)=colors[0]
            color='%02x%02x%02x' % (a,b,c)
            print("-----color------"+ color)
            return color


if __name__ == '__main__':
    app.run()