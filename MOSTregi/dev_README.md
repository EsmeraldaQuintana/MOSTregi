
### Make sure all software is installed..:

+ git
+ python3
+ pip3
+ virtualenv
+ virtualenvwrapper
+ Django 2.0.x
+ postgresql v9.5.11 or better

install virtualenv with pip3! Not pip. Otherwise virtualenv will use python2 as default.

### INSTALLING POSTGRESQL:
I used this tutorial: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

### BEFORE DEVELOPMENT:
Start a new virtualenv, make sure you have all required software.
$ pip install -r requirements.txt
To get all the dependencies.


### TO DEPLOY (see it in browser)
$ ./deploy.sh

If this doesn't work, do this:
  $ chmod +x deploy.sh
  $ ./deploy.sh
    If that didn't work, ask Esmeralda.

### ENDING DEVELOPMENT SESSION:
$ deactivate
  this turns off virtualenv
$ git add .
$ git commit -m "Add a detailed commit message!"
$ git push

