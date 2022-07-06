# FamPay
### Clone the repository
- $ git clone git@github.com:Harshith-19/FamPay.git
### Install the requirements
- $ pip install -r requirements.txt
### Install the redis-server
- $ sudo apt install redis-server
### Start the server
- $ redis-server
### Run the migrations
- $ python3 manage.py makemigrations
- $ python3 manage.py migrate
### Run the below commands in 3 different terminals
- $ python3 manage.py runserver
- $ celery -A Fampay worker --loglevel=info
- $ celery -A Fampay beat -l info