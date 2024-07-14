import os
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
# Use an absolute path to ensure the database is created in the correct location
basedir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

class Todo(db.Model):
    ID = db.Column(db.Integer, primary_key = True)
    CONTENT = db.Column(db.String(200), nullable= False)
    COMPLETED = db.Column(db.Boolean, default=True)
    DATE_CREATED = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.ID


@app.route('/')
def index():
    return render_template('index.html')

if (__name__) == "__main__":
    
    app.run(debug=True, port=8000,host='0.0.0.0')