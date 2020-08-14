from app import app, db
from flask import render_template,request,url_for, Response, jsonify, json
from wtforms import StringField, TextField, Form
from wtforms.validators import DataRequired, Length

class SearchForm(Form):
    output=StringField('Output', validators=[DataRequired(),Length(max=250)],render_kw={"placeholder": "input"})

class Output(db.Model):
    __tablename__ = 'output'

    starting_phrase = db.Column(db.String(250), primary_key=True)
    following_word = db.Column(db.String(250))
    count = db.Column(db.Integer)

    def as_dict(self):
        return {'output': self.starting_phrase+' '+self.following_word}

@app.route('/', methods=['GET', 'POST'])
def index():
    form=SearchForm(request.form)
    return render_template('index.html', form=form)

@app.route('/output',methods=['GET'])
def outputdic():
    res = Output.query.order_by(Output.count.desc())
    list_output = [r.as_dict() for r in res]
    return jsonify(list_output)

@app.route('/process', methods=['POST'])
def process():
    output = request.form['output']
    if output:
        return jsonify({'output':output})
    return jsonify({'error': 'missing data..'})
