from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE-URI']= "sqlite:////todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    created_date=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/About')
def About():
    return 'This is about page'

@app.route('/Contact')
def Contact():
    return 'This is Contact page'

if __name__ == "__main__":
    app.run(debug=True)
