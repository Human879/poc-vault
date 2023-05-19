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