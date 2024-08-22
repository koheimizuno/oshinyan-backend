# 推しニャンサイト(Backend)

![Copy of Fullstack Twitter Clone (8)](https://oshinyan.love/ogp.webp)

推しニャンは『 お気に入りの看板猫が探せる！推せるサイト』 です

Features:

- django5.0
- djangorestframework
- django-cleanup
- django-resized
- django-modeladmin-reorder
- pillow
- psycopg2
- python-dateutil
- ElasticEmail
- whitenoise

### Prerequisites

**Python version 3.12**

### Cloning the repository

```shell
git clone https://github.com/weijiezhang-star/oshinyan-backend
```

### Configuration Virtual Environment

```shell
py -m venv [virtual environment folder name]
```

- Windows

```shell
[virtual environment folder name]\Scripts\activate
```

- Linux

```shell
source [virtual environment folder name]/bin/activate
```

### Install packages from requirements.txt

```shell
py -m pip install -r requirements.txt
```

### Setup .env file

```js
MAIL_API_KEY=
BACKEND_EMAIL=
DB_NAME=
DB_USER=
DB_PASSWORD=
RAPID_API=
ADDRESS_API=
```

### Migrate Datebase

```shell
py manage.py migrate
```

### Start the server

```shell
py manage.py runserver
```
