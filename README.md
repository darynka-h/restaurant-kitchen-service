# restaurant-kitchen-service

## What this project is about?
   This project can improve the communication between cooks on the professional 
   kitchen in restaurant or café.
   It is a management system, in which cooks can: 
   - create new dishes & dish-types using creation form with name of dish and image. 
   - see detail about other cook and see which dishes they are cooking. 
   - check detail page of every dish, find detail information 
   about every dish type 
   - check who is cooking particular dish on detail page of every dish.

![Screenshot from 2023-02-16 13-48-20](https://user-images.githubusercontent.com/107792308/219454853-36ec492d-b6b6-46e1-98d2-a3062f9805a3.png)
![Screenshot from 2023-02-16 13-48-32](https://user-images.githubusercontent.com/107792308/219454883-d413f322-f1de-410b-b95f-f5cfb91b06a1.png)


## how to install the project?

1. Run the command below in your terminal
   - `git clone git@github.com:darynka-h/restaurant-kitchen-service.git`
2.  Open the project folder in your IDE
3. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
   - python -m venv venv
   - venv\Scripts\activate (on Windows)
   - source venv/bin/activate (on macOS)
   - pip install -r requirements.txt
4. Don't forget to do migrations
   - `python manage.py migrate`
5. You can use following superuser (or create another one by yourself):
   - Login: hannochenko
   - Password: 123User1@3
6. Run your server using the command below
   - `python manage.py runserver`
7. In this project you can use environment variables.
   - Environment variables are variables which  you store outside of your program. 
   
   This variables can affect how your program runs. 
   For example, you can set environment variables that contain the key and secret for an API, but in my project I use
   only SECRET_KEY(example of it you can find in .env_sample). 
