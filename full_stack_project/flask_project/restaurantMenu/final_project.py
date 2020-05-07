from flask import Flask,render_template, request, redirect, url_for, flash,jsonify

from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_db import Base, Restaurant, MenuItem
engine= create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind=engine
DBSession= sessionmaker(bind=engine)
session= DBSession()


app = Flask(__name__)
# @app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def showRestaurants(restaurant_id):
    restaurant= session.query(Restaurant).filter_by(id=restaurant_id).one()
    return render_template("showRestaurants.html", restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newRestaurant(restaurant_id):
    if request.method=="POST":
        newrestaurant=Restaurant(name= request.form['name'])
        session.add(newrestaurant)
        session.commit()
        print(newrestaurant.name)
        flash("new menu item is created")

        return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template('newRestaurants.html', restaurant_id=restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    editedRestaurant= session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method=='POST':
        if request.form['name']:
            editedRestaurant.name=request.form['name']
        session.add(editedRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template('editRestaurants.html',
        restaurant_id=restaurant_id,
        rest=editedRestaurant)

@app.route('/restaurants/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    deletedRestname=session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.form=="POST":
        session.delete(deleteRestname)
        session.commit()
        return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))

    return render_template('deleteRestaurants.html',
    restaurant_id=restaurant_id,
    rest=deletedRestname)



# @app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/", methods=['GET', 'POST'])
def showMenu(restaurant_id):
    return "delete restaurants %s" % restaurant_id

@app.route("/restaurants/<int:restaurant_id>/menu/new/")
def newMenu(restaurant_id):
    return "delete restaurants %s" % restaurant_id


@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit/")
def editMenu(restaurant_id, menu_id):
    return "edit restaurants %s" % menu_id

@app.route("/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete/")
def deleteMenu(restaurant_id, menu_id):
    return "delete restaurants %s" % menu_id







if __name__ == "__main__":
    app.secret_key="super secret key"
    app.debug=True
    app.run("0.0.0.0", 5000)
