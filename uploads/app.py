from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import subprocess, shlex
import sys
import traceback
# import datetime
import tempfile


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'py'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
         # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(path)
            file.save(path)


            command = f"python3 {path} < hello.txt"
            timeoutSeconds = 5
            try:
                output = subprocess.check_output(command, shell=True, timeout=timeoutSeconds, universal_newlines=True, stderr=subprocess.STDOUT, )
                print(output)
                if output == 'Hello World, Henrique Dezani':
                    print('Sucesso')
                    return f'<html><body>Sucesso<br/>Output: <pre>Hello World, Henrique Dezani</pre> Expected <pre>{output}</pre></body></html>'
                else:
                    print('Falha')
            except subprocess.CalledProcessError as ex:
                return f'<html><body>Erro de execução: <pre>{str(ex.output)}</pre></body></html>'
            except subprocess.TimeoutExpired:
                return f'<html><body><pre>Timeout em {timeoutSeconds} segundos.</pre></body></html>'

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run(debug=True, port=3001)