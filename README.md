# Devops
>  - STEVENOT Léo
>  - PONCET Nathan

# Installation
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