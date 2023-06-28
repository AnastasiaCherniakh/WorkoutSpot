from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Training, WaterIntake, Weight
from datetime import datetime
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/')
def landing():
    return render_template('landing.html')


@views.route('/add-training', methods=['GET', 'POST'])
def add_training():
    if request.method == 'POST':
        category = request.form.get('category')
        note = request.form.get('note')
        date_old = request.form.get('date')
        date_new = datetime.strptime(date_old, '%Y-%m-%d')
        date = date_new

        new_training = Training(category=category, note=note, date=date, user_id = current_user.id)
        db.session.add(new_training)
        db.session.commit()
    return render_template('add_training.html')


@views.route('/add-water', methods=['GET', 'POST'])
def add_water():
    if request.method == 'POST':
        cup = request.form.get('cup')

        new_water = WaterIntake(cup=cup, user_id=current_user.id)
        db.session.add(new_water)
        db.session.commit()
    return render_template('add_water.html')


@views.route('/update-weight', methods=['GET', 'POST'])
def update_weight():
    if request.method == 'POST':
        weight = request.form.get('weight')

        new_weight = Weight(weight=weight, user_id=current_user.id)
        db.session.add(new_weight)
        db.session.commit()
    return render_template('add_weight.html')

@views.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)


@views.route('/trainings')
@login_required
def trainings():
    return render_template('trainings.html', user=current_user)


@views.route('/stats')
def stats():
    cup_a_day = db.session.query(db.func.sum(WaterIntake.cup), WaterIntake.date).group_by(WaterIntake.date).order_by(WaterIntake.date).all()

    weight_a_date = db.session.query(db.func.sum(Weight.weight), Weight.date).group_by(Weight.date).order_by(Weight.date).all()

    training_a_date = db.session.query(db.func.sum(Training.amount), Training.category).group_by(
        Training.category).order_by(Training.category).all()

    cups = []
    dates_label = []
    for cup, date in cup_a_day:
        dates_label.append(date.strftime("%d-%m-%Y"))
        cups.append(cup)

    weights = []
    dates_label2 = []
    for weight, date in weight_a_date:
        dates_label2.append(date.strftime("%d-%m-%Y"))
        weights.append(weight)

    trainings = []
    dates_label3 = []
    for training, category in training_a_date:
        dates_label3.append(category)
        trainings.append(training)
    return render_template('stats.html', cups=json.dumps(cups), dates_label=json.dumps(dates_label), dates_label2=json.dumps(dates_label2), weight=json.dumps(weights), dates_label3=json.dumps(dates_label3), training=json.dumps(trainings))
@views.route('/inspiration')
def inspiration():
    return render_template('inspiration.html')
