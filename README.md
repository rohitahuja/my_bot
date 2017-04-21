# Django Messenger Bot Template

A project starter template for Django 1.11 that is production ready for creating a Facebook Messenger bot deployed to Heroku. Created by Bytesize.

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Base application for developing a Facebook Messenger bot with all the helpful utilities.
- Uses Python 2.7.

## How to Use

Before we begin, please ensure that you have:

- Created a Facebook page you can connect your bot to (i.e. My Bot)
- A Heroku account and the heroku client installed and logged into on your terminal:

    ```
    brew install heroku
    heroku login
    ```

### Seting up your Environment

Install Django and virtualenv:

    $ pip install django
    $ pip install virtualenv

### Creating your Project

Using this template to create a new Django app is easy:

    $ django-admin.py startproject --template=https://github.com/rohitahuja/hcs-bot-template/archive/master.zip --name=Procfile my_bot

You can replace ``my_bot`` with your desired project name.

### Setting up your Project

Enter your project folder:

    $ cd my_bot

Create your virtual environment and activate it:

    $ virtualenv venv
    $ source ./venv/bin/activate

Install dependencies:
    
    $ pip install -r requirements.txt

### Understanding the Code

- ``hcs_bot/urls.py → webhook/``
    - We’ve created a ``webhook/`` endpoint here that our Messenger Bot will hit when it receives a message
    - When our webhook/ endpoint is hit, it calls the ``webhook()`` function in ``bot/views.py``
- ``bot/views.py → webhook()``
    - Calls ``handle_entries()``, which is the main message handling function 
- ``bot/message.py → handle_entries()``
    - Iterates over and calls ``handle_message()`` on each message object
- ``bot/message.py → handle_message()``
    - Creates the response to the received message and sends it by calling ``send_message()``
- ``bot/message.py → send_message()``
    - Structures the response and makes the post request to the Messenger API

### Hacking on the Code:

Hack! Hack! Hack!

### Creating your bot

- Create your messenger bot on https://developers.facebook.com/  
    - Make an account if you don’t have one already
    - Set the Display Name to “My Bot” or whatever you want to call it, and set the Contact Email to your email
    - Set the Category to “Apps for Messenger”
- Go to Messenger on the left sidebar:
    - Under "Token Generation", generate a token for the page you created and set the variable ``page_access_token`` at the top of ``message.py`` to it

### Pushing to production

Initialize version control for the project:

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

Create a Heroku project:

    $ heroku create
    $ git push heroku master

### Hooking up your bot

- Go back to https://developers.facebook.com/
- On the left sidebar, add the product Webhooks and go to it
    - Create a New Subscription with the Callback URL as ``http://<your-heroku-subdomain>.herokuapp.com/webhook/`` and the Verify Token as ``johnharvard``. For Fields, check ONLY ``message``.
- Go to the Messenger tab
    - Under "Webhooks", subscribe the webhook we just created to the page you created.

### Try out your bot!

Try it!
