## How to start

```
 git clone https://github.com/Alirvah/havrila-backend.git
 
 cd havrila-backend
 python3 -m venv env
 source env/bin/activate
 pip install -r req.txt 
 ./manage.py migrate
 ./manage.py runserver

 or 

 zappa init
 zappa deploy dev
 zappa update
 zappa status

```

