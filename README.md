# pat-fastapi
pihole-adlist-toggler with fastapi 

# What is this?
I will be developing a FastAPI to control my adlists on my piholes. This will allow me to now have to access the pihole gravity database functions without needing to login to two different admin panels.

# WELCOME TO ME LEARNING FastAPI!
If you pulled this version of the code I am very sorry that its garbage

## Resources in no particular order
> Developing a single paffe app with FastAPI and React

* [FastAPI Docs](https://fastapi.tiangolo.com/)
* [Possible help with the front end](https://testdriven.io/blog/fastapi-react/)
* 

# Notes for jordan
## pipenv and pipfiles
`pipenv update` will use the current pipfile and install all the required packages

## HTTPException
I can't easily write my HTTPExecption code in the main.py since all the database actions are performed in the class instead. I cant find a way to pass the error into the main.py from the class file. And not really sure if this is needed anyways since the comment will be largely hardcoded into the front end. 

To get proper HTTPException to work I would need to create a whole new main.py with a lot of the work already performed in gravitydatabase.py in there or find some way to see if sqlite3 row.cur results in 0 being a 404. 

I was getting some help with the `import_asyncio.py` and `import_asynciohtmlout.py` however I dont know how to implement it properly into the `main.py` code set. Well its in there I have no idea if it will really work or not.

## Async stdoutput
With the powers of ChatGPT I got a bunch of ideas on how to (attempt) at getting an async output of the stdout of running `/etc/.pihole/gravity.sh` at the moment we perform the command and wait (not using async) on the command to complete. This however taught me about routers and how they might be useful in the future.

But how does the async output work? I dont really understand it but we import the router from app_stdout.py and add a router_include. This isnt working as expected since the `_htmlout` is using the `/` and that is somehow redirecting to the not prefix `/stdout/` of the FastAPI App call. 
``` shell
INFO:     192.168.1.201:37402 - "GET /stdout/ HTTP/1.1" 200 OK
INFO:     192.168.1.201:37402 - "GET /output HTTP/1.1" 404 Not Found
```

It should neatly be `/stdout/output` but isn't working.

## What are we doing now?
With the majority of the pain behind us the API is working as expected.

* gets output from `/pat-fastapi/{adlist_comment}`
* gets output from `/pat-fastapi/enable/{adlist_comment}`
* gets output from `/pat-fastapi/disable/{adlist_comment}`
* gets output from `/pat-fastapi/update/`

I am unable to get the HTTPExceptions to work with my GravityDatabase class existing outside of the main.py. I think I want to keep these seperated anyways since there is a lot of logic built in to handle some operations I want to be done upon database creation. 

Having someone take a look at the code and give me some ideas or advise on how to add the exceptions would be neat but that could be refactoring the entire code base from scratch. That could be a lovely fork idea but outside of my scope. 

I have it running on both my PiHole installations and able to easily enable and disable my adlists. This gets used once a week or so when my wife needs access to the blocked adlists under `{adlist_comment}`. I have a cron setup that run a simple shell command that toggles the {adlist_comment} on and off according to a schedule (upcoming github repo!) its possible to rewrite that shell command to call this api now but its nice enough to keep seperate since I dont have a good way of keeping uvicorn running at startup. 

# TODO
* Frontend development
* automatic running of uvicorn
* intergration with crontab "adlist toggler"
* look into routers for code seperation if needed
    * Possible way to add more functions
* I did find a neat way to start parsing the output as a json which could complicate the async or make it easier?

## Uvicorn as a service
Installing uvicorn as a service and setup logging. 

``` makefile
# /etc/systemd/system/pat-fastapi.service
[Unit]
Description=My FastAPI Service
After=network.target

[Service]
User=root
WorkingDirectory=/home/jordan/Development/pat-fastapi/
ExecStart=/home/jordan/.local/share/virtualenvs/pat-fastapi-5QG9oBxx/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --log-config /home/jordan/Development/pat-fastapi/logging.conf
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Installing the service.

`sudo systemctl daemon-reload`

`sudo systemctl start pat-fastapi.service`

`sudo systemctl enable pat-fastapi.service`

Creating a logging configuration file for uvicorn to accept. This will log into `/var/log/pat-fastapi.log`

``` makefile
# pat-fastapi/logging.conf
[loggers]
keys=root

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=genericFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler,fileHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=genericFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=logging.handlers.RotatingFileHandler
level=DEBUG
formatter=genericFormatter
args=('/var/log/pat-fastapi.log', 'a', 10485760, 5)

[formatter_genericFormatter]
format=%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d - %(message)s
datefmt=%Y-%m-%d %H:%M:%S
```

`touch /var/log/pat-fastapi.log`