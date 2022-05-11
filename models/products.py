from models.database import connection_dec


@connection_dec
def add_new_product(connection, name, notes, producer_edrpou, category_id, price):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO products(name, notes, producer_edrpou, category_id, price) 
            VALUES ('{name}', '{notes}', '{producer_edrpou}', '{category_id}', '{price}');
            SELECT product_id FROM products WHERE name='{name}';
        """)
        return cursor.fetchone()


@connection_dec
def delete_product(connection, _id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            DELETE FROM products WHERE product_id={_id}
        """)


@connection_dec
def get_product_by_id(connection, _id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM products WHERE product_id={_id}
        """)
        return cursor.fetchone()


@connection_dec
def get_products(connection, *args, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()
