from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = b'4564312348'

cars = [
  {'id':1,'brand':'Toyota','model':'Yaris Ativ','year':2024,'price':695000},
  {'id':2,'brand':'Honda','model':'City Hatchback','year':2024,'price':731000},
  {'id':3,'brand':'Nissan','model':'Amera','year':2025,'price':535000}
]

@app.route('/')
def index():
  return render_template('index.html', title='Home Page')

@app.route('/cars',methods=['GET','POST'])
def all_cars():
  if request.method == "POST":
    brand = request.form['brand']
    tmp_cars  = []
    for car in cars:
      if brand in car['brand']:
        tmp_cars.append(car)
    return render_template('cars/all_cars.html', title='Search Cars Page',cars=tmp_cars)
  return render_template('cars/all_cars.html', title='Show All Cars Page',cars=cars)

@app.route('/cars/new',methods=['GET','POST'])
def new_car():
  if request.method == 'POST':
    brand = request.form['brand']
    model = request.form['model']
    year = int(request.form['year'])
    price = int(request.form['price'])
    length = len(cars)
    id = cars[length-1]['id']+1

    car = {'id':id,'brand':brand,'model':model,'year':year,'price':price}

    cars.append(car)
    flash('Add new Car Successfully','success')
    return redirect(url_for('all_cars'))
  return render_template('cars/new_car.html',title='New Car Page')

@app.route('/cars/<int:id>/delete')
def delete_car(id):
  for car in cars:
    if id == car['id']:
      cars.remove(car)
      break
  flash('Delete Car Successfully','success')
  return redirect(url_for('all_cars'))

@app.route('/cars/<int:id>/edit',methods=['GET','POST'])
def edit_car(id):
  for c in cars:
    if id == c['id']:
      car = c
      break
  if request.method == 'POST':
    brand = request.form['brand']
    model = request.form['model']
    year = int(request.form['year'])
    price = int(request.form['price'])

    for c in cars:
      if id == c['id']:
        c['brand'] = brand
        c['model'] = model
        c['year'] = year
        c['price'] = price
        break
    flash('Update Car Successfully','success')
    return redirect(url_for('all_cars'))
  return render_template('cars/edit_car.html',title='Edit Car Page',car=car)