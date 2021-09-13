# from flask import Flask
# import os
# import subprocess, shlex
# import sys
# import traceback
# # import datetime

# app = Flask(__name__)
# # https://docs.python.org/3/library/subprocess.html#module-subprocess
# @app.route('/')
# def hello():
#     # os.system("python3 /Users/dezani/Developments/fatec/lp/hackerroom/hackerpython/hello.py < hello.txt")
#     command = "python3 hello.py < hello.txt"
#     timeoutSeconds = 5
#     try:
#         # start = datetime.datetime.now()
#         output = subprocess.check_output(command, shell=True, timeout=timeoutSeconds, universal_newlines=True, stderr=subprocess.STDOUT, )
#         # end = datetime.datetime.now()
#         # total = end - start
#         print(output)
#         if output == 'Hello World, Henrique Dezani':
#             print('Sucesso')
#             return f'<html><body>Sucesso<br/>Output: <pre>Hello World, Henrique Dezani</pre> Expected <pre>{output}</pre></body></html>'
#             # return f'<html><body>Sucesso em {total.microseconds} {total.microseconds/1000} microseconds<br/>Output: <pre>Hello World, Henrique Dezani</pre> Expected <pre>{output}</pre></body></html>'
#         else:
#             print('Falha')
#     except subprocess.CalledProcessError as ex:
#         return f'<html><body>Erro de execução: <pre>{str(ex.output)}</pre></body></html>'
#     except subprocess.TimeoutExpired:
#         return f'<html><body><pre>Timeout em {timeoutSeconds} segundos.</pre></body></html>'

#     return 'Hello World'

# if __name__ == '__main__':
#     app.run(debug=True, port=3001)