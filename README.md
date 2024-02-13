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

**devops-db**
- Mysql 8.2
- No exposed ports

**devops-api**
- Python API 
- Python 3.8
- Default port : 8000
- No exposed ports

**devops-nginx**
- Nginx 3.18
- Reverse proxy 80 -> devops-api:8000
- Port 80 exposed

**devops-newman**
- Newman 6
- No exposed ports