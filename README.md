# apiDjango

```
$ git clone https://github.com/and2carvalho/apiShiplay.git
$ cd apiShiplay
$ pipenv shell
$ pipenv install -r requirements
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver 

```
ou 

```
$ git clone https://github.com/and2carvalho/apiShiplay.git
$ docker build . -t "shipay-api"
$ docker run --publish 8000:8000 --detach shipay-api

```

***Referência API:***
* https://documenter.getpostman.com/view/9741587/TVCjwkUQ