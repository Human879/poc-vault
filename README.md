# poc-vault


## Initials steps

### Pull vault docker image from DockerHub
```
docker pull vault
```

### Run that container on port 8200:8200
```
docker run -p 8200:8200 -e 'VAULT_DEV_ROOT_TOKEN_ID=dev-only-token' vault
```

In init.sh you can see pipenv commands can be used for this project

### Don't forget to enter to the venv
```
pipenv shell
```

### Just the first time
```
pipenv install flask
pipenv install hvac
```

### Run the application
```
pipenv run dev
```