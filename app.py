from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app=Flask(__name__)
app.config['SECRETE_KEY']='SeCreteEKey'
#app.config['UPLOAD_FOLDER'] = 'images'
ENV='prod'

if ENV=='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:qt123123...@localhost/autocomplete'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']='mysql://bad31ca552b4e5:24402813@us-cdbr-east-02.cleardb.com/heroku_5968cd3c50ec929'

app.config['SQLALCHMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
from routes import *

if __name__=='__main__':
    app.run()
