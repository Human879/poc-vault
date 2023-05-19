import hvac

def vault_connect():
    # Configuration de Vault
    vault_client = hvac.Client(url='http://0.0.0.0:8200')
    vault_client.token = 'dev-only-token'
    return vault_client


# Create a User 
def create_user(username, password):
    # Obtenir l'instance de Client Vault
    vault_client = vault_connect()

    secret_data = {'username': username, 'password': password}

    create_response = vault_client.secrets.kv.v2.create_or_update_secret(
        path='users',
        secret=secret_data
    )

    if 'errors' not in create_response:
        print('Utilisateur créé avec succès dans Vault.')
    else:
        print('Erreur lors de la création de l\'utilisateur dans Vault:', create_response['errors'])

# Appel de la fonction pour créer un utilisateur et un mot de passe
create_user('john.doe', 'secretpassword')
