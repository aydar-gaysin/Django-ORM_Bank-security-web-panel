# Bank security web-panel

Django based web-interface to database with fake generated passcards and bank storage visit data. 
Its purpose is to display the list of visitors and give assessment of the suspiciousness of their bank storage visit.

Main page receives from datebase list of all storage visitor's passcards. It gives the link to users who are currently
inside bank storage.
Names are interactive and clickable.  By clicking you can see all visits date and duration to storage
by selected person.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
Fork the repo. Copy files to your project directory. Move to this directory

Fill in ***Variables*** in .env file:
```
DB_HOST=***Database host URL***
DB_PORT=***Database connection porl***
DB_NAME=***Database name***
DB_USER=***Database username***
DB_PASSWORD=*** Database user password***
DEBUG=***Django debug state True or False***
```
### How to run

Start web-server by typing in terminal window:
```
python manage.py runserver 0.0.0.0:8000
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).