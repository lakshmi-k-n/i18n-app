# i8n-app
Support for plugging in JSONfield editor to add translations of text. For this implementation, I have used `django-jsonform` to create a JSON based editor.  


## Installation  
Ensure PostgreSQL 11 or higher is installed in the system.  

`python -m venv env`

Install all the required dependencies

`pip install -r requirements.txt`

### Create Database

`sudo -u postgres psql`  
  
`CREATE DATABASE library;`  
`CREATE USER lib_user WITH PASSWORD 'pa$$word';`  
`GRANT ALL PRIVILEGES ON DATABASE library TO lib_user;`  

### Create .env file
- In the project directory create a file `.env`
- Refer .env-example file for more

 ### Run migrations and start server  
 `python manage.py runserver 0.0.0.0:8001`
