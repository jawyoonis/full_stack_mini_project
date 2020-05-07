from flask import Flask,render_template, request, redirect, url_for, flash,jsonify

#Fake Restaurants
restaurant = {'name': 'The CRUDdy Crab', 'id': '1'}

restaurants = [{'name': 'The CRUDdy Crab', 'id': '1'}, {'name':'Blue Burgers', 'id':'2'},{'name':'Taco Hut', 'id':'3'}]


#Fake Menu Items
items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


app = Flask(__name__)
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return render_template("showRestaurants.html", restaurants=restaurants)

@app.route('/restaurants/<int:restaurant_id>/new/')
def newRestaurant(restaurant_id):
    if request.method=="POST":
        return redirect(url_for('showRestaurants', restaurant_id=restaurant_id))
    else:
        return render_template('newRestaurants.html', restaurant_id=restaurant_id, restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>/edit/')
def editRestaurant(restaurant_id):
    return "edit restaurants"

@app.route('/restaurants/<int:restaurant_id>/delete/')
def deleteRestaurant(restaurant_id):
    return "delete restaurants %s" % restaurant_id

# @app.route("/restaurants/<int:restaurant_id>/")
@app.route("/restaurants/<int:restaurant_id>/menu/")
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
    # app.secret_key="super secret key"
    app.debug=True
    app.run("0.0.0.0", 5000)
