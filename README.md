# restaurant-kitchen-service

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
   - `eche python manage.py migrate`
5. Run your server using the command below
   - `python manage.py runserver`
## What this project is about?
This project can improve the communication between cooks on the professional 
kitchen in restaurant or café. It is a management system, in which cooks can 
create new dishes & dish-types using creation form with name of dish and image.
Cook can see detail about other cook and see which dishes they are cooking. 
There are detail page for every dish, 
Cook can find detail information about every dish and who is cooking it on detail page of every dish. 

![Screenshot from 2023-02-16 13-51-03.png](..%2F..%2FPictures%2FScreenshot%20from%202023-02-16%2013-51-03.png)
![Screenshot from 2023-02-16 13-51-12.png](..%2F..%2FPictures%2FScreenshot%20from%202023-02-16%2013-51-12.png)