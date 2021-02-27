# Onidevs Challenge 
- Participant: Joao Victor Ferreira

## Requirements for build/execute:
- [Docker](https://docs.docker.com/get-docker/) (Lastest Version)
- [Docker-Compose](https://docs.docker.com/compose/install/) (Lastest Version) 

## How to build

After have `Docker` and `Docker-Compose` installed, use the command below to build the project instance and the requirements:

```
docker-compose build
```

After the Docker environment finish the project building, run the following command for the first execution:

```
docker-compose up
```

If you don`t want an runtime console of Django envroiment, you can use the flag ``-d`` for run on silent mode (without console logging). Like this example below:

```
docker-compose up -d
```

## Python Packages that i used

This packages are automatically builded by docker, you can see their names on the file ``requirements.txt``.

- [Django](https://www.djangoproject.com/) **(required)**
- [Django Admin](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/) **(required)**
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html) **(required)**
- [simplejson](https://pypi.org/project/simplejson/) **(optinally added for fix decimal issues when parsing to json/str)**