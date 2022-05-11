from models.database import connection_dec


@connection_dec
def add_new_producer(connection, edrpou, name, notes, email, phone_number, country, state, city, street, house_number):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            INSERT INTO producers(edrpou, name, notes, email, phone_number, country, state, city, street, house_number) 
            VALUES ('{edrpou}', '{name}', '{notes}', '{email}', '{phone_number}', '{country}', '{state}', '{city}',
            '{street}', '{house_number}');
        """)
        return edrpou


@connection_dec
def delete_producer(connection, edrpou):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            DELETE FROM producers WHERE edrpou={edrpou}
        """)
        return edrpou


@connection_dec
def get_producer_by_edrpou(connection, edrpou):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM producers WHERE edrpou={edrpou}
        """)
        return cursor.fetchone()


@connection_dec
def get_producers(connection, *args, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM producers")
        return cursor.fetchall()
