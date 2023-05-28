from re import sub
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

host_path = 'https://5000-fatecriopre-projetotest-kwlhmc5067m.ws-us98.gitpod.io/'

exercicios = {
    1: {
        "outputs": [
            "True\n", 
            "False\n", 
            "True\n",
            "True\n", 
            "True\n", ]
    },
    2: {
        "outputs": [
        "[12, 6, 3, 10, 5, 16, 8, 4, 2, 1]\n",
        "[5, 16, 8, 4, 2, 1]\n",
        "[18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]\n",
        "[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]\n",
        "[1]\n"]
    },
    3: {
        "outputs": [
            "[2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]\n",
            "[1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]\n",
            "[7.0, 5.0, 3.0, 5.0, 5.0]\n",
            "[7.0, 6.5, 6.0, 5.5, 5.0, 5.5, 5.0]\n",
            "[10.0]\n"
        ]
    }
}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        df = pd.read_csv('alunos_lp.csv', sep=';')
        df_search = df[df['Matricula'] == int(request.form['matricula'])]
        if len(df_search) > 0:
            session['user_matricula'] = str(df_search['Matricula'].values[0])
            session['user_nome'] = df_search['Nome'].values[0]
            return redirect(f'{host_path}/submit')
        else:
            return render_template('login.html', message='Número de matrícula não encontrado.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_matricula', None)
    session.pop('user_nome', None)
    return redirect(f'{host_path}/')

@app.route('/dashboard')
def ranking():
    df = pd.read_csv('respostas.csv')
    return render_template('dashboard.html', lista=df.groupby(['matricula', 'exercicio']).max().sort_values('exercicio').values.tolist())

@app.route('/leaderboard')
def leaderboard():
    df = pd.read_csv('respostas.csv')
    df_max = df.groupby(['matricula', 'exercicio']).max()
    print(df_max.head())
    df_sum = df_max.groupby(['nome']).sum()
    print(df_sum)
    return render_template('leaderboard.html', lista=df_sum.sort_values('pontos', ascending=False))

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
            # print(path)
            file.save(path)

            outputs = []
            expecteds = []
            corrects = []

            for i in range(5):

                command = f"python3 {path} < exercicio{int(request.form['exercicio'])}-{i}.txt"

                # command = f"python3 {path} "

                # for param in exercicios[int(request.form['exercicio'])]["inputs"]:
                #     command += f"<<< {param} <<< 'Dezani'"

                # print(command)
                timeoutSeconds = 5
                
                try:
                    output = subprocess.check_output(command, shell=True, timeout=timeoutSeconds, universal_newlines=True, stderr=subprocess.STDOUT)
                    # print(output)
                    outputs.append(output)

                    answer = exercicios[int(request.form['exercicio'])]["outputs"][i]
                    # print(answer)
                    expecteds.append(answer)                    
                    
                    if output == str(answer):
                        corrects.append(True)
                    else:
                        corrects.append(False)
                
                except subprocess.CalledProcessError as ex:
                    return render_template('erro.html', nome=session['user_nome'], output=str(ex.output))
                except subprocess.TimeoutExpired:
                    return render_template('timeout.html', nome=session['user_nome'])

            if sum(corrects) == 5:
                with open('respostas.csv', 'at') as file_out:
                    escritor = csv.writer(file_out)
                    escritor.writerow([int(session['user_matricula']),session['user_nome'],datetime.datetime.now(),int(request.form['exercicio']),1,int(request.form['exercicio'])])
            
                # print(corrects)
                return render_template('sucesso.html', nome=session['user_nome'], outputs=outputs, expecteds=expecteds, corrects=corrects)

            else:
                with open('respostas.csv', 'at') as file_out:
                    escritor = csv.writer(file_out)
                    escritor.writerow([int(session['user_matricula']),session['user_nome'],datetime.datetime.now(),int(request.form['exercicio']),0,int(request.form['exercicio'])])
                
                # print(corrects)
                return render_template('falha.html', nome=session['user_nome'], outputs=outputs, expecteds=expecteds, corrects=corrects)


    df = pd.read_csv('respostas.csv')
    df_aluno = df[df['matricula'] == int(session['user_matricula'])].groupby(['exercicio']).max().sort_values('exercicio')
    return render_template('upload.html', nome=session['user_nome'], matricula=session['user_matricula'], lista=df_aluno.values.tolist(), total=sum(df_aluno['pontos']))

if __name__ == '__main__':
    app.run()
    
