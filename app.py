import os
from qa import *
from flask import Flask, request, render_template, redirect, url_for



project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'app/templates')
static_path = os.path.join(project_root, 'app/static')
app = Flask(__name__, template_folder= 'Template')
context_set = ""

@app.route('/', methods = ['POST', 'GET'])
def index():
   if request.method == 'GET':
      return render_template('index.html')


@app.route('/qa', methods = ['POST', 'GET'])
def rasa_reponse():
   if request.method == 'GET':
      a = run(str(request.args.get('text')))
      return a
        

application = app