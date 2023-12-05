# takeaway 
​Major dependencies 
```
python3
postgresql
```
​
```
Run the following in the terminal:

pip3 install flask 
pip3 install flask-sqlalchemy
pip3 install python-dotenv
pip3 install flask-migrate
pip3 install psycopg2
​createdb takeaway
​
```
​
​
in app.py 
change the postgres user
```
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<your_postgres_user>@localhost:5432/setlist_app"
```
​
Making the thing run :) 
```
flask db upgrade 
flask seed
flask run 
```

In your browser go to localhost:4999 and add /home

Collapse





