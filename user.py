from db import get_db

class User:
    def __init__(self, user_id, email, productIds):
        self.user_id = user_id
        self.email = email
        self.productIds = productIds

    @staticmethod
    def get(user_id):
        db = get_db()
        user = db.execute(
            "SELECT * FROM user WHERE userId = ?", (user_id)
        ).fetchone()
        if not user:
            return None
        user = User(
            user_id = user[0], email = user[1], productIds = user[2]
        )
        return user

    @staticmethod
    def create(user_id, email, productId):
        db = get_db()
        rating = db.execute(
            "INSERT into user (userId, email, productId)"
            " VALUES (?, ?, ?)",
            (user_id, email, productId)
        )
        db.commit()

