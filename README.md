FASTAPIPOSTGRES
The application allows you to send and recieve data in JSON via POST\GET requestю
Consists of database and web application, both working in docker containers.
Allows write and read JSON data in postgres database with routes.
You can check FastAPI project documentation here http://0.0.0.0:8888/docs#/ after the app&db are running 

Getting Started
Requirements for the app
Docker version 20.10.15
Docker Compose version 2.5.0
Open ports 8888 and 54321
Source code from github

Installing
A step by step that tell you how to get an application running
Go  to the directory with app via console
Enter the "docker-compose up" command
Wait message "Uvicorn running on etc." in your console

How-To use
Go to http://0.0.0.0:8888/docs#/ in your browser
Here you can choose method and try it out
GET localhost:8888/interns "Get all items in db"
GET localhost:8888/intern/{id} "Get item by id in db"
POST localhost:8888/intern "Create an item in db"
You can also try it with postman\insomnia
GET method also return you data in browser