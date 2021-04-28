# jobsity_finchat

This project was developed with Python 3.8, Django 3.2, SQLite and Redis in a Ubuntu 20.04 machine.

FinChat is intended to be a real-time chat application. It relies on the technology of web sockets
to have real time updates on each browser, and uses Redis as message broker. A bot was added to
response queries from users that request a quote for a stock through a simple command in the chat
as ```/stock=aapl.us```. The app allows registered users to create chatrooms and join any of the existing rooms.

## Local Start

0. Setting Redis on your machine:
  - If you already have Redis running on your machine just be sure it is on port 6379 and go to the step 1.
  - Having Docker on your machine the easiest way to start Redis is:
 
    ```$ docker run -p 6379:6379 -d redis:5```

    and that's it, you have Redis listening on port 6379.

1. Clone the repo
  ```
  $ git clone https://github.com/RodrigoSierraV/jobsity_finchat.git
  $ cd jobsity_finchat/
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv venv
  $ source venv/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

4. Migrate:
  ```
  (venv) $ python manage.py migrate
  ```

5. Run the app:
  ```
  (venv) $ python manage.py runserver
  ```

6. In your browser go to:
  ```
  http://127.0.0.1:8000/users/login/
  ```
