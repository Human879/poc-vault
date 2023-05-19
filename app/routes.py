from app import app
from app.vault_connect import vault_connect
from flask import Flask, render_template, request, redirect, session, abort

app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html'), 404

@app.route('/welcome')
def welcome():
    # Vérifier si l'utilisateur est connecté
    if not session.get('logged_in'):
        # Retourner une réponse 404 (Not Found) si l'utilisateur n'est pas connecté
        abort(404)
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Vérifier les informations d'identification avec Vault
        if credentials_are_valid(username, password):
            
            # Enregistrer l'état de connexion dans la session
            session['logged_in'] = True

            # Redirection vers une nouvelle page après une authentification réussie
            print('----------------- ✅ Successful authentication ✅ -----------------')
            return redirect('/welcome')
        
        else:
            print('----------------- ❌ Failure: user/mdp incorrects ❌ -----------------')
            return render_template('error-login.html')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    print('----------------- ❌ Disconected ❌ -----------------')
    return redirect('/login')

def credentials_are_valid(username, password):
    # Implémentez ici la logique pour interagir avec Vault et vérifier les informations d'identification
    # Utilisez la fonction vault_connect() pour obtenir l'instance de Client Vault

    vault_client = vault_connect()

    # Récupérez les informations d'identification depuis Vault
    response = vault_client.secrets.kv.v2.read_secret_version('users')

    if response and 'data' in response['data']:
        credentials = response['data']['data']
        if credentials.get('username') == username and credentials.get('password') == password:
            return True

    return False
