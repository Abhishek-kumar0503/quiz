# Quiz Web Application

This is a web-based quiz application built with Django. Users can participate in quizzes, answer multiple-choice questions, and view a summary of their results at the end of the quiz.

## Features

- Start a new quiz session
- Answer Single-choice questions
- View a summary of correct and incorrect answers after completing the quiz
- Admin interface to add new quiz questions

## Set-up

> To get started...

  ### Step 1
  
  - 🍴 Fork this repo!
  
  ### Step 2
  
  - 👯 Clone this repo to your local machine.
    ```sh
    git clone https://github.com/Abhishek-kumar0503/quiz.git
    ```
  
  ### Step 3
  
  - 🧑‍💻 Install virtual Environment
    
    ```sh
      pip install virtualenv
    ```
    ```sh
      cd env/Scripts/
      activate
    ```
    
  ### Step 4
  
  - 🕵️ Install requirement if not installed
    ```sh
      pip install -r requirements.txt
    ```
  ### Step 5
  
  - 🚣‍♂️ Go to the manage.py file directory 
  ``` sh
    cd quiz
  ```
  - Run the migrate and migration and create super Admin
    ```sh
      python manage.py makemigrations
      python manage.py migrate
      python manage.py createsuperuser
    ```
  
  ### Step 6
  
  - 😊😄😃 Run the Server
  ``` sh
    python manage.py runserver
  ```
  ### Step 6

  - If you want to add question go to admin panel and add question

    
  ```sh
    http://127.0.0.1:8000/admin/
  ```
