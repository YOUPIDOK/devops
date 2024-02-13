# Devops
>  - STEVENOT Léo
>  - PONCET Nathan

## Installation
```shell
ansible-playbook ansible/build.yml -i ansible/inventories/integration  
```

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

## Containers
- devops-nginx
- devops-db
- devops-api
- devops-newman