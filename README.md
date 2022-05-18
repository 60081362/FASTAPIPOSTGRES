# FASTAPIPOSTGRES
The application allows you to send and recieve data in JSON via POST\GET request.<br/>
Consists of database and web application, both working in docker containers.<br/>
Allows write and read JSON data in postgres database with routes.<br/>
You can check FastAPI project documentation [here](http://0.0.0.0:8888/docs#/) after the app&db are running.<br/>

## Getting Started
### Requirements for the app:
- Docker<br/>
- Docker Compose<br/>
- Posts 8888 and 54321 are opened<br/>
- Source code from [github](https://github.com/60081362/FASTAPIPOSTGRES)<br/>

### Installing
##### A step by step that tell you how to get an application running<br/>
- Go  to the directory with app via console<br/>
- Create .env file with your database credentials in format bellow:.<br/>
   - ***POSTGRES_USER=YOUR_POSTGRES_USER***
   - ***POSTGRES_PASSWORD=YOUR_POSTGRES_PASSWORD***
   - ***POSTGRES_DB=YOUR_POSTGRES_DATATBASE***
   - ***POSTGRES_HOST=YOUR_POSTGRES_HOST***
- Enter the "docker-compose up" command<br/>
- Wait message "Uvicorn running on etc." in your console<br/>

### How-To use
- Go to [link](http://0.0.0.0:8888/docs#/) in your browser<br/>
#### Here you can choose method and try it out<br/>
- **GET localhost:8888/interns** *"Get all items in db"*<br/>
- **GET localhost:8888/intern/{id}** *"Get item by id in db"*<br/>
- **POST localhost:8888/intern** *"Create an item in db"*<br/>
You can also try it with postman\insomnia. GET method also return you data in browser