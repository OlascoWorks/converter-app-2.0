from flask import Blueprint, render_template, url_for, request, flash, redirect, jsonify
from flask_login import login_required, current_user
from . import db
from .models import User, Conversions
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    result = ''
    user = current_user
    if request.method == 'POST':
        unit1 = request.form.get('to-be-converted')
        unit2 = request.form.get('to-be-converted-to')
        value = request.form.get('value')

        try:
            if unit1 == unit2:
                result = f'{int(value)}{unit1}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
                print(new_conversion.date)
            elif unit1=='ml' and unit2=='cm':
                result = f'{int(value)/100}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='ml' and unit2=='m':
                result = f'{int(value)/1000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='ml' and unit2=='km':
                result = f'{int(value)/100000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='cm' and unit2=='ml':
                result = f'{int(value)*100}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='cm' and unit2=='m':
                result = f'{int(value)/100}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='cm' and unit2=='km':
                result = f'{int(value)/10000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='m' and unit2=='ml':
                result = f'{int(value)*1000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='m' and unit2=='cm':
                result = f'{int(value)*100}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='m' and unit2=='km':
                result = f'{int(value)/1000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='km' and unit2=='ml':
                result = f'{int(value)*100000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='km' and unit2=='cm':
                result = f'{int(value)*10000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='km' and unit2=='m':
                result = f'{int(value)*1000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='mg' and unit2=='g':
                result = f'{int(value)/100}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='mg' and unit2=='kg':
                result = f'{int(value)/10000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='g' and unit2=='mg':
                result = f'{int(value)*100}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='g' and unit2=='kg':
                result = f'{int(value)/1000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='kg' and unit2=='mg':
                result = f'{int(value)*10000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='kg' and unit2=='g':
                result = f'{int(value)*1000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='mg' and unit2=='g':
                result = f'{int(value)/100}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='ms' and unit2=='s':
                result = f'{int(value)/1000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='ms' and unit2=='mn':
                result = f'{int(value)/60000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='ms' and unit2=='hr':
                result = f'{int(value)/3600000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='s' and unit2=='ms':
                result = f'{int(value)*1000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='s' and unit2=='mn':
                result = f'{int(value)/60}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='s' and unit2=='hr':
                result = f'{int(value)/3600}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='mn' and unit2=='ms':
                result = f'{int(value)*60000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='mn' and unit2=='s':
                result = f'{int(value)*60}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='mn' and unit2=='hr':
                result = f'{int(value)/60}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='hr' and unit2=='ms':
                result = f'{int(value)*3600000}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='hr' and unit2=='s':
                result = f'{int(value)*3600}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='hr' and unit2=='mn':
                result = f'{int(value)*60}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='°c' and unit2=='°f':
                result = f'{(int(value)*1.8)+32}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='°c' and unit2=='k':
                result = f'{(int(value)+273.15)}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='°f' and unit2=='°c':
                result = f'{(int(value)-32)}*1.8{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='°f' and unit2=='k':
                result = f'{(((int(value)*-32)*5)/9)+273.15}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='k' and unit2=='°c':
                result = f'{(int(value)-273.15)}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            elif unit1=='k' and unit2=='°f':
                result = f'{((int(value)-273.15)*1.8)+32}{unit2}'
                new_conversion = Conversions(unit_1=unit1, unit_2=unit2, value=value, result=result, user_id=current_user.id)
                db.session.add(new_conversion)
                db.session.commit()
            else:
                result = ''
                flash('Please select your options and put in valid inputs', category='error')
        except ValueError:
            flash('Only numbers can be converted', category='error')
            redirect(url_for('views.home'))

    return render_template('home.html', user=current_user, result=result)

@views.route('/history')
@login_required
def history():
    return render_template('history.html', user=current_user)

@views.route('/delete-conversion', methods=['POST'])
def delete_conversion():
    conversion = json.loads(request.data)
    conversionId = conversion['conversionId']
    conversion = Conversions.query.get(conversionId)
    if conversion:
        if conversion.user_id == current_user.id:
            db.session.delete(conversion)
            db.session.commit()
            
    return redirect(url_for('views.history'))