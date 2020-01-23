import flask
import sqlite3
import os
from rating import Rating
from user import User
from product import Product
import random

from db import init_app



app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

try:
    with app.app_context():
        init_app(app)
except sqlite3.OperationalError:
    # Assume it's already been created
    pass


@app.route("/")
def indexPage():
    return flask.jsonify("hello world")

def createDummyData():
    temp = []
    for i in range(5):
        temp.append([i, i + 10, i])
    return temp


@app.route('/addData')
def addDummyData():
    try:
        tempData = createDummyData()
        for user_id, product_id, rating in tempData:
            User.create(user_id, "randomemail@gmail.com", product_id)
            Product.create(product_id, '10')
            Rating.create(user_id, product_id, rating)
        # add more records
        for user_id in range(20, 25):
            User.create(user_id, 'randomemail@gmail.com', '12')
            Rating.create(user_id, '12', random.randint(0, 5))
        return "dummy Data has been created", 200
    except Exception as e:
        print(e)
        return "exception while adding data, check the logs", 403

@app.route('/users/<user_id>/products/<product_id>/ratings')
def fetchRating(user_id, product_id):
    rating = Rating.get(user_id, product_id)
    if not rating:
        rating = 0
    avg_rating = Rating.get_avg_rating(product_id)
    count_rating = Rating.count_individual_rating(user_id)
    return flask.jsonify({
        "rating": rating,
        "avgRating": avg_rating,
        "countRating": count_rating
    }), 200


if __name__ == "__main__":
    app.run()




