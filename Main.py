from flask import Flask, render_template, url_for,flash
from Predictor import predictor
import pandas as pd
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from DB import DBHelper

app = Flask(__name__)
app.config['SECRET_KEY'] = '93b55a3ff22021ee4af6fb93c76639f9'
upcoming= pd.read_csv('Upcoming-games.csv')
upcoming.drop(['url', 'Blue Side_link','Red Side_link','Score_link','Score'], axis='columns', inplace=True)
preditctions = []
for index, row in upcoming.iterrows() :
    preditction = {
        "date":row['date'],
        "Blue Side":row['Blue Side'],
        "Red Side":row['Red Side'],
        "result":"0 - 1" if (predictor(row['Blue Side'],row['Red Side'])=="1") else "1 - 0"
    }
    preditctions.append(preditction)
@app.route('/')
def home():
    return render_template('Home.html',preditctions=preditctions)
@app.route('/<name>',methods=['GET', 'POST'])
def user(name):
    Teams =pd.read_csv(name+".csv")
    Teams = Teams['Name']
    Choices =[]
    for row in Teams:
        choice=(row,row)
        Choices.append(choice)
    class predict(FlaskForm):
        blueSide=SelectField(u'Blue Side',choices=Choices)
        redSide=SelectField(u'Red Side',choices=Choices)
        submit = SubmitField('Submit')
    BlueSide = None
    RedSide = None
    form =predict()
    if form.validate_on_submit():
        BlueSide = form.blueSide.data
        RedSide = form.redSide.data
        result = "0 - 1" if (predictor(BlueSide,RedSide)=="1") else "1 - 0"
        if (predictor(BlueSide,RedSide)=="1"):
            flash(f'{RedSide} will win the match: {result}!',category='warning')
        else:
            flash(f'{BlueSide} will win the match: {result}!',category='warning')
    return render_template('Teams.html',name=name,form=form)

@app.route('/world',methods=['GET', 'POST'])
def world():
    Teams =pd.read_csv("Teams.csv")
    Teams = Teams['Name']
    Choices =[]
    for row in Teams:
        choice=(row,row)
        Choices.append(choice)
    class predict(FlaskForm):
        blueSide=SelectField(u'Blue Side',choices=Choices)
        redSide=SelectField(u'Red Side',choices=Choices)
        submit = SubmitField('Submit')
    BlueSide = None
    RedSide = None
    form =predict()
    if form.validate_on_submit():
        BlueSide = form.blueSide.data
        RedSide = form.redSide.data
        result = "0 - 1" if (predictor(BlueSide,RedSide)=="1") else "1 - 0"
        if (predictor(BlueSide,RedSide)=="1"):
            flash(f'{RedSide} will win the match: {result}!',category='warning')
        else:
            flash(f'{BlueSide} will win the match: {result}!',category='warning')
    return render_template('Teams.html',name="World Wide Predictions",form=form)

@app.route('/update',methods=['GET', 'POST'])
def update():
    Teams = pd.read_csv("Teams.csv")
    Teams = Teams['Name']
    Choices =[]
    for row in Teams:
        choice=(row,row)
        Choices.append(choice)
    class up(FlaskForm):
        blueSide=SelectField(u'Blue Side',choices=Choices)
        redSide=SelectField(u'Red Side',choices=Choices)
        score=SelectField(u'Score',choices=[("0","Blue side won"),("1","Red side won")])
        submit = SubmitField('Submit')
    db=DBHelper()
    BlueSide = None
    RedSide = None
    Score = None
    form =up()
    if form.validate_on_submit():
        BlueSide = form.blueSide.data
        RedSide = form.redSide.data
        Score = form.score.data
        db.insertar("INSERT INTO Games VALUES('" + BlueSide + "','" + RedSide +"','" + Score+"')")
        flash(f'Score successfully updated in to the database!',category='success')
    print(db.leer())
    return render_template('Update.html',name="Update results",form=form)