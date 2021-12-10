from flask import Flask, render_template, request, redirect, url_for
import os
from pymongo import MongoClient
uri = os.environ.get('MONGODB_URI', 'mongodb+srv://brendan:Amazing7@Cluster0.cbl9h.mongodb.net/Cluster0?retryWrites=true&w=majority')
client = MongoClient(uri)
db = client.shoelist
app = Flask(__name__)

shoes = db.shoes



@app.route('/shoes')
def shoes_index():
    '''Show all shoes.'''
    return render_template('shoes_index.html', shoes=shoes.find())

@app.route('/shoes/new')
def shoes_recent():
    return render_template('shoes_new.html')

@app.route('/totals')
def cart():
  return render_template('cart.html', shoes=shoes.find())

@app.route('/totals/new', methods=['POST'])
def shoes_new():
  return render_template('add_shoe.html')

# Yeezys        
@app.route('/yeezys')
def Yeezy():
  return render_template('Yeezy.html', shoes=shoes.find())

# Off White
@app.route('/offwhite')
def off_white():
  return render_template('offwhite.html', shoes=shoes.find())

# Air Jordan
@app.route('/airjordan')
def air_jordan():
  return render_template('airjordan.html', shoes=shoes.find())

# High Fashion
@app.route('/highfashion')
def high_fashion():
  return render_template('highfashion.html', shoes=shoes.find())

# Menu
@app.route('/menu')
def menu():
  return render_template('menu.html', shoes=shoes.find())

@app.route('/menu/yeezys')
def add_yeezy():
  return render_template('yeezy.html', shoes=shoes.find())

@app.route('/menu/offwhite')
def add_offwhite():
  return render_template('offwhite.html', shoes=shoes.find())

@app.route('/menu/airjordan')
def add_highfashion():
  return render_template('airjordan.html', shoes=shoes.find())    

@app.route('/menu/highfashion')
def add_high_fashion():
  return render_template('highfashion.html', shoes=shoes.find())

@app.route('/cart')
def order_applied():
    print(request.form.get('name'))
    shoe = {
        'name': request.form.get('name'),
        'price': request.form.get('amount'),
        }
    shoe_id=shoe.insert_one(shoe).inserted_id
    return redirect(url_for('product_show',shoe_id=shoe_id))
