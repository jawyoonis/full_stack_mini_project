from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_db import Base, Restaurant, MenuItem
engine= create_engine("sqlite:///restaurantmenu.db")
Base.metadata.bind=engine
DBSession= sessionmaker(bind=engine)
session= DBSession()
app = Flask(__name__)

# @app.route("/")
@app.route("/restaurants/<int:restaurant_id>/menu/json/")
def jsonifyMenuItems(restaurant_id):
    restaurant= session.query(Restaurant).filter_by(id=restaurant_id).one()
    items=session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return jsonify(MenuItem=[item.serialize for item in items])

# ADD JSON ENDPOINT HERE
@app.route("/restaurants/<int:restaurant_id>/menu/json/<int:menu_id>/")
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(MenuItem=menuItem.serialize)


@app.route('/')
@app.route("/restaurants/<int:restaurant_id>/")
def restaurant_menue(restaurant_id):
    restaurant= session.query(Restaurant).filter_by(id=restaurant_id).one()
    items=session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template("menu.html", items=items, restaurant=restaurant)


# @app.route("/")
@app.route("/restaurants/<int:restaurant_id>/new/", methods=['GET','POST'])
def newMenuItem(restaurant_id):
    # return "page to create a new menu item. Task 1 complete!"
    if request.method=="POST":
        newItem= MenuItem(name= request.form['name'], description= request.form['description'],
        price= request.form['price'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item is created")
        return redirect(url_for('restaurant_menue', restaurant_id=restaurant_id))
    else:
        return render_template('newitemMenu.html', restaurant_id=restaurant_id)




# Task 2: Create route for editMenuItem function here

# @app.route("/")
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/',methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    edittedItem= session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method=="POST":
        if request.form['name']:
            edittedItem.name=request.form['name']
        if request.form['price']:
            edittedItem.price=request.form['price']
        if request.form['description']:
            edittedItem.description=request.form['description']
        if request.form['course']:
            edittedItem.course=request.form['course']
        session.add(edittedItem)
        session.commit()
        flash("menu items are editted")
        return redirect(url_for('restaurant_menue', restaurant_id=restaurant_id))
    else:
        return render_template("editMenu.html",
        restaurant_id=restaurant_id,
        menu_id=menu_id,
        item=edittedItem)


# @app.route("/")
@app.route("/restaurants/<int:restaurant_id>/<int:menu_id>/delete/", methods=['GET','POST'])
def deleteMenuItem(restaurant_id, menu_id):
    itemDeleted= session.query(MenuItem).filter_by(id=menu_id).one()
    if request.form=="POST":
        session.delete(itemDeleted)
        session.commit()
        flash("menu item is deleted")
        return redirect(url_for("restaurant_menue", restaurant_id=restaurant_id))
    return render_template('deleteMenuItem.html',item=itemDeleted)





if __name__ == "__main__":
    app.secret_key="super secret key"
    app.debug=True
    app.run("0.0.0.0", 8000)
