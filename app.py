from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
CORS(app)
class URLs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return '<URLs %r>' % self.long_url

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/results', methods=['GET','POST'])
def results():
    if request.method=='POST':
        user_url=request.form['url']
        db.session.add(URLs(long_url=user_url))
        db.session.commit()
        check = URLs.query.all()
        id = URLs.query.filter_by(long_url=user_url).first().id
        newURL = f'http://127.0.0.1:5000/{id}'
        return render_template('results.html', user_url=user_url, new_url=newURL)
    else:
        return render_template('results.html', user_url='somestring')


if __name__ == '__main__':
    app.run(debug=True)
