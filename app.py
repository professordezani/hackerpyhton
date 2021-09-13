from flask import Flask, flash, request, redirect, url_for, render_template, session
# from werkzeug.utils import secure_filename
import os
import subprocess
import datetime
import pandas as pd
import csv

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'py'}

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        df = pd.read_csv('alunos_lp.csv', sep=';')
        df_search = df[df['Matricula'] == int(request.form['matricula'])]
        if len(df_search) > 0:
            session['user_matricula'] = str(df_search['Matricula'].values[0])
            session['user_nome'] = df_search['Nome'].values[0]
            return redirect(url_for('submit'))
        else:
            return render_template('login.html', message='Número de matrícula não encontrado.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_matricula', None)
    session.pop('user_nome', None)
    return redirect(url_for('login'))

@app.route('/ranking')
def ranking():
    df = pd.read_csv('respostas.csv')
    return render_template('ranking.html', lista=df.groupby(['matricula', 'exercicio']).max().sort_values('exercicio').values.tolist())

@app.route('/leaderboard')
def leaderboard():
    df = pd.read_csv('respostas.csv')
    return render_template('leaderboard.html', lista=df.groupby(['matricula', 'exercicio']).max().sort_values('nome').values.tolist())

@app.route('/submit', methods=['GET', 'POST'])
def submit():
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
            # filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], f"{session['user_matricula']}_{request.form['exercicio']}_{datetime.datetime.now().timestamp()}.py")
            print(path)
            file.save(path)


            command = f"python3 {path} < hello.txt"
            timeoutSeconds = 5
            try:
                output = subprocess.check_output(command, shell=True, timeout=timeoutSeconds, universal_newlines=True, stderr=subprocess.STDOUT, )
                print(output)
                if output == 'Hello World, Henrique Dezani':
                    with open('respostas.csv', 'at') as file_out:
                        escritor = csv.writer(file_out)
                        escritor.writerow([int(session['user_matricula']),session['user_nome'],datetime.datetime.now(),int(request.form['exercicio']),1,int(request.form['exercicio'])])
                    
                    return render_template('sucesso.html', nome=session['user_nome'], output=output)
                else:
                    with open('respostas.csv', 'at') as file_out:
                        escritor = csv.writer(file_out)
                        escritor.writerow([int(session['user_matricula']),session['user_nome'],datetime.datetime.now(),int(request.form['exercicio']),0,int(request.form['exercicio'])])
                    return render_template('falha.html', nome=session['user_nome'], output=output)

            except subprocess.CalledProcessError as ex:
                return render_template('erro.html', nome=session['user_nome'], output=str(ex.output))
            except subprocess.TimeoutExpired:
                return render_template('timeout.html', nome=session['user_nome'])

    df = pd.read_csv('respostas.csv')
    df_aluno = df[df['matricula'] == int(session['user_matricula'])].groupby(['exercicio']).max().sort_values('exercicio')
    return render_template('upload.html', nome=session['user_nome'], matricula=session['user_matricula'], lista=df_aluno.values.tolist(), total=sum(df_aluno['pontos']))

if __name__ == '__main__':
    app.run(debug=True) #, port=3001)