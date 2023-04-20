# pat-fastapi
pihole-adlist-toggler with fastapi 

# WELCOME TO ME LEARNING GITHUB!
If you pulled this version of the code I am very sorry that its garbage

# Notes for jordan
## pipenv and pipfiles
`pipenv update` will use the current pipfile and install all the required packages

## HTTPException
I can't easily write my HTTPExecption code in the main.py since all the database actions are performed in the class instead. I cant find a way to pass the error into the main.py from the class file. And not really sure if this is needed anyways since the comment will be largely hardcoded into the front end. 

To get proper HTTPException to work I would need to create a whole new main.py with a lot of the work already performed in gravitydatabase.py in there or find some way to see if sqlite3 row.cur results in 0 being a 404. 