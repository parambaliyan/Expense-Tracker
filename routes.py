from flask import render_template, request, redirect, url_for
from . import db
from .models import Expense
from datetime import datetime

@app.route('/')
def index():
    expenses = Expense.query.all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        category = request.form['category']
        date = request.form['date']
        
        new_expense = Expense(name=name, amount=amount, category=category, date=datetime.strptime(date, '%Y-%m-%d'))
        db.session.add(new_expense)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_expense.html')