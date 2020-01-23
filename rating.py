from db import get_db

class Rating:
    def __init__(self, user_id, product_id, rating):
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating

    @staticmethod
    def get(user_id, product_id):
        db = get_db()
        rating = db.execute(
            "SELECT * FROM rating WHERE userId = ? and productId = ?", (user_id, product_id,)
        ).fetchone()
        if not rating:
            return None
        rating = Rating(
            user_id = rating[0], product_id = rating[1], rating = rating[2]
        )
        return rating.rating
            

    @staticmethod
    def get_avg_rating(product_id):
        db = get_db()
        rows = db.execute(
            "SELECT * FROM rating WHERE productId = ?", (product_id,)
        ).fetchall()
        sum_rating = 0
        for row in rows:
            sum_rating += row[2]
        avg_rating = sum_rating // len(rows)
        return avg_rating

    @staticmethod
    def count_individual_rating(user_id):
        db = get_db()
        count_rating = db.execute(
            "SELECT COUNT(*) FROM rating WHERE userId = ?", (user_id,)
        ).fetchone()
        return count_rating[0]

    @staticmethod
    def create(user_id, product_id, rating):
        db = get_db()
        rating = db.execute(
            "INSERT into rating (userId, productId, rating)"
            " VALUES (?, ?, ?)",
            (user_id, product_id, rating)
        )
        db.commit()

    