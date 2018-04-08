
### Make sure all software is installed..:

+ git
+ python3
+ pip3
+ virtualenv (optional)
+ virtualenvwrapper (optional)
+ Django 2.0.x
install virtualenv with pip3! Not pip. Otherwise virtualenv will use python2 as default, if python2 is on your machine.

### BEFORE DEVELOPMENT:
Start a new virtualenv, make sure you have all required software. (virtual env is optional but recommended, especially if you use Python outside of softie)
$ pip install -r requirements.txt
To get all the dependencies.

### TO DEPLOY (see it in browser)
Linux
$ ./deploy.sh
Windows
$ ./deployW.sh

If this doesn't work, do this:
  $ chmod +x deploy.sh
  $ ./deploy.sh
If that didn't work, ask Esmeralda.

### Making the report
In events/form_test.py, change conn to the absolute path of where your database is.

### ENDING DEVELOPMENT SESSION:
$ deactivate
  this turns off virtualenv
$ git add .
$ git commit -m "Add a detailed commit message!"
$ git push
