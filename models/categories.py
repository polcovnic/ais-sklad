from models.database import connection_dec


@connection_dec
def add_new_category(connection, name, notes):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO categories (name, notes) VALUES {name}, {notes};
            SELECT category_id FROM categories WHERE  name={name}
        """)
        return cursor.fetchone()


@connection_dec
def delete_category(connection, _id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            DELETE FROM categories WHERE category_id={_id}
        """)


@connection_dec
def get_category_by_id(connection, _id):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM categories WHERE category_id={_id}
        """)
        return cursor.fetchone()


@connection_dec
def get_categories(connection):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM categories")
        return cursor.fetchall()