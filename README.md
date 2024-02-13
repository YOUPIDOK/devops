# Devops
>  - STEVENOT Léo
>  - PONCET Nathan

## Installation
### With ansible
```shell
ansible-playbook ansible/build.yml -i ansible/inventories/integration  
```
### With docker

**Config environement variables**
```shell
cp .env.example .env
```

**Create network**
```shell
docker network create devops-network
```

**Build**
```shell
docker compose build
```

**Start**
```shell
docker compose up -d
```

## Containers create in "devops-network"
- devops-nginx 
- devops-db
- devops-api
- devops-newman