from models.database import connection_dec


@connection_dec
def add_new_row(connection, order_id, product_id, amount, _sum):
    with connection.cursor() as cursor:
        cursor.execute(f"""
        INSERT INTO order_rows (order_id, sum, product_id) VALUES ({order_id}, {_sum}, {product_id});
        
        SELECT order_row_id FROM order_rows WHERE product_id={product_id} AND order_id={order_id}
        """)
        return cursor.fetchone()


@connection_dec
def get_all_rows_in_order(connection, order_id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM order_rows WHERE order_id={order_id}")
        return cursor.fetchall()
