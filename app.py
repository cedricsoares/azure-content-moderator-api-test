import helper
from helper import *
from flask import Flask, request, Response, render_template, redirect
from flask_nav import Nav
from flask_nav.elements import *
import json
import os.path
import requests
from pprint import pprint
import time
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
nav = Nav(app)

nav.register_element('top', Navbar(
    'navigation',
    View('Accueil', 'index'),
    View('Liste des commentaires', 'comments')
    ))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comment/new', methods=['POST'])
def add_comment():
    # Get comment from the POST body
    if request.method == "POST":
        req = request.form.to_dict()
        comment = req["comment"]
        url = os.getenv('ENDPOINT-URL')
        
        headers = {
                    'Content-Type' : 'text/plain',
                    'Ocp-Apim-Subscription-Key': os.getenv('OCP-APIM-SUBSCRIPTION-KEY'),
                  }

        params = {
                'autocorrect': 'True ',
                'PII': 'False',
                'classify': 'False',
                'language': 'fra'
                 }
        
        r_moderation = requests.post(url, comment.encode('utf8'), 
                                    params=params, headers=headers, )
        response_moderation = r_moderation.json()
        
        if  response_moderation['Terms'] !=  None :
            res_data = helper.add_to_db(comment, status='inappropriate')
            return Response("Votre commentaire n'as pas été publié car il contient des propos inapprorpriés ou pouvant heurter la sensibilité des lectrice.teur.s")

        #return Response("Votre commentaire a été enregistré.")    

        res_data = helper.add_to_db(comment, status='appropriate')

        if res_data is None:
            response = Response("{'error': 'comment not added - " + comment + "'}", status=400 , mimetype='application/json')
            return response

        response = Response(json.dumps(res_data), mimetype='application/json')

        return Response("Votre commentaire a été enregistré.")

@app.route('/comments')
def comments():
    data = display_content()
    return render_template('comments.html', data=data)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
   