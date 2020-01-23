from db import get_db

class Product:
    def __init__(self, product_id, price):
        self.product_id = product_id
        self.price = price

    @staticmethod
    def get(product_id):
        db = get_db()
        product = db.execute(
            "SELECT * FROM product WHERE productId = ?", (product_id)
        ).fetchone()
        if not product:
            return None
        product = Product(
            product_id = product[0], price = product[1]
        )
        return product

    @staticmethod
    def create(product_id, price):
        db = get_db()
        rating = db.execute(
            "INSERT into product (productId, price)"
            " VALUES (?, ?)",
            (product_id, price)
        )
        db.commit()

