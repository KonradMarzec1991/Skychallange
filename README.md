# Simple exams system management

Simple Django REST project for creating/modyfing exams and its for lecturer/student

#### Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

#### Installing

1) Create folder on your disk
```
mkdir name_of_folder
```

2) Create virtual environment in folder/ run virtual environment
```
virtualenv -p python3 .
source bin/activate
```

3) Clone repository to given folder , get in folder and install requirements.txt
```
git clone https://github.com/KonradMarzec1991/Skychallange.git
pip install -r requirements.txt
```

4) Run server on 'http://127.0.0.1:8000/'
```
python manage.py runserver 
```

You will see all available methods in project.

#### ...or....

1) Create folder on your disk, clone repository and run with docker
```
mkdir name_of_folder
git clone https://github.com/KonradMarzec1991/Skychallange.git
(sudo) docker-compose up -a
```
