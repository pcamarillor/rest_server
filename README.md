# REST server by using Python

REST server example on python. This server uses the Flask microframework to support the HTTP taks. 

## Server setup
To install `Flask`, we are going to use `virtualenv` tool. If you have not installed `virtualenv` you can use `pip` as follows:

```
$ [sudo] pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-15.1.0-py2.py3-none-any.whl (1.8MB)
    100% |████████████████████████████████| 1.8MB 589kB/s 
Installing collected packages: virtualenv
Successfully installed virtualenv-15.1.0
```

Create the workspace directory and then initialize `Flask`

```
$ mkdir python_rest_example
$ cd python_rest_example/
$ virtualenv flask
New python executable in /Users/pcamarillor/Code/python_rest_example/flask/bin/python
Installing setuptools, pip, wheel...done.
```

Once initialized `Flask` **install** the entire library into the workspace directory:

```
$ flask/bin/pip install flask
Collecting flask
  Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 1.3MB/s 
Collecting Jinja2>=2.4 (from flask)
  Downloading Jinja2-2.10-py2.py3-none-any.whl (126kB)
    100% |████████████████████████████████| 133kB 2.2MB/s 
Collecting Werkzeug>=0.7 (from flask)
  Downloading Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
    100% |████████████████████████████████| 327kB 2.1MB/s 
Collecting click>=2.0 (from flask)
  Downloading click-6.7-py2.py3-none-any.whl (71kB)
    100% |████████████████████████████████| 71kB 5.5MB/s 
Collecting itsdangerous>=0.21 (from flask)
  Downloading itsdangerous-0.24.tar.gz (46kB)
    100% |████████████████████████████████| 51kB 6.1MB/s 
Collecting MarkupSafe>=0.23 (from Jinja2>=2.4->flask)
  Downloading MarkupSafe-1.0.tar.gz
Building wheels for collected packages: itsdangerous, MarkupSafe
  Running setup.py bdist_wheel for itsdangerous ... done
  Stored in directory: /Users/pcamarillor/Library/Caches/pip/wheels/fc/a8/66/24d655233c757e178d45dea2de22a04c6d92766abfb741129a
  Running setup.py bdist_wheel for MarkupSafe ... done
  Stored in directory: /Users/pcamarillor/Library/Caches/pip/wheels/88/a7/30/e39a54a87bcbe25308fa3ca64e8ddc75d9b3e5afa21ee32d57
Successfully built itsdangerous MarkupSafe
Installing collected packages: MarkupSafe, Jinja2, Werkzeug, click, itsdangerous, flask
Successfully installed Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 flask-0.12.2 itsdangerous-0.24

```

Now, you are able to run the REST sever:

```
$ ./server.py
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 142-801-933
```
