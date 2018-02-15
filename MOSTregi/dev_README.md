
### Make sure all software is installed..:

+ git
+ python3
+ pip3
+ virtualenv
+ virtualenvwrapper
+ Django 2.0.x

install virtualenv with pip3! Not pip. Otherwise virtualenv will use python2 as default.

### BEFORE DEVELOPMENT:
Start a new virtualenv, make sure you have all required software.
$ pip install -r requirements.txt
To get all the dependecies.

### TO START:
Begin the virtual environemnt:
$ workon MOSTregi
  workon is syntax provided by virtualenvwrapper
  workon will activate virtualenv for the MOSTregi project

Begin coding.

### TO DEPLOY (see it in browser)
$ ./deploy.sh
  If this doesn't work, do this:
$ chmod +x deploy.sh
$ ./deploy.sh
  If that didn't work, ask Esmeralda.

### ENDING DEVELOPMENT SESSION:
$ deactivate
  this turns off virtualenv
$ cd ..
  Move back to PinotNoir folder.
$ git add .
$ git commit -m "Add a detailed commit message!"
$ git push

