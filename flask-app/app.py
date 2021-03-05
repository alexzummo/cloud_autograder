import subprocess
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))

      output = subprocess.check_output(["./autograde.py"])      
      return render_template('feedback.html', output=output)
		
if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")
