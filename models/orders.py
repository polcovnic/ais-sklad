from models.database import connection_dec


@connection_dec
def add_new_order(connection, notes, date, customer_ipn, _sum):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO orders (notes, date, customer_ipn, sum) VALUES ('{notes}', '{date}', {customer_ipn}, {_sum});
            SELECT order_id FROM orders WHERE customer_ipn={customer_ipn};
        """)
        return cursor.fetchone()


@connection_dec
def delete_order(connection, _id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            DELETE FROM orders WHERE order_id={_id};
        """)


@connection_dec
def get_order_by_id(connection, _id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM orders WHERE order_id={_id}
        """)
        return cursor.fetchone()


@connection_dec
def get_orders(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM orders")
        return cursor.fetchall()
