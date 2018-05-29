# affinity

# SETUP
python3 -m venv venv  
source venv/bin/activate  
pip install flask  
export FLASK_APP=timbers.py  
flask run   

# Notes:
Form handling:    
This will use the extention Flask-WTF for web forms    
source venv/bin/activate      
pip install flask-wtf  
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-login
pip install flask-mail
pip install pyjwt

# Stuff:  
1: DB frontend: Flask-SQLAlchemy - Flask-friendly ORM wrapper to SQLAlchemy  
2: DB backend: SQLite  
3: flask-migrate   ( https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database )   
4: To design the database: http://ondras.zarovi.cz/sql/demo/   
5: flask db init ( This will generate the 'migrations' folder which I will now check into github )   
5.5: flask db migrate ( Later on this command will be useful to change the shape of the db )   
6: flask db upgrade ( This will detect that there is no sqlite db laying around and create one named 'app.db')   
7: pip install flask-login ( for password hashes )    
...later...   
A:flask db migrate -m "new fields in user model"   
B:flask db upgrade ( steps A and B to tell DB to update itself )   
...Debug mode: Stop the server and "export FLASK_DEBUG=1" ( 'set' for windows ) and restart - now in verbose debug mode    

# flask run  
source venv/bin/activate  
pip install flask    <---  Maybe need to do this step also?   
export FLASK_APP=timbers.py  
flask run   ( For REPL )

# Branch strategy  
master will be the reference branch
dev will be the sandbox branch  
Other branchs as needed  


# Tutorial I am reading about FLASK 
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world  

# Example db usage: 
flask shell
>>> from app import db
>>> from app.models import User, Post
>>> u = User(username='john', email='john@example.com')
>>> db.session.add(u)
>>> db.session.commit()
>>> u = User(username='susan', email='susan@example.com')
>>> db.session.add(u)
>>> db.session.commit()
>>> users = User.query.all()
>>> users
[<User john>, <User susan>]
>>> u = User.query.get(1)
>>> u
<User john>
>>> 
