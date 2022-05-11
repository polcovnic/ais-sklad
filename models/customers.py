from models.database import connection_dec


@connection_dec
def add_customer(connection, customer_ipn, name, surname, patronymic, country, state, city, street,
                 house_number, phone_number, email, debt, notes):
    with connection.cursor() as cursor:
        cursor.execute(f"""
        INSERT INTO customers (customer_ipn, notes, name, surname, patronymic, country, state, city, street,
         house_number, phone_number, email, debt) VALUES ({customer_ipn}, '{notes}', '{name}', '{surname}', '{patronymic}',
         '{country}', '{state}', '{city}', '{street}', '{house_number}', '{phone_number}', '{email}', '{debt}');
        """)
        return customer_ipn


@connection_dec
def get_customer(connection, customer_ipn):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM customers WHERE customer_ipn={customer_ipn};
        """)


@connection_dec
def get_customers(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"""
            SELECT * FROM customers;
        """)
        return cursor.fetchall()


@connection_dec
def delete_customer(connection, customer_ipn):
    with connection.cursor() as cursor:
        cursor.execute(f"""
        DELETE FROM customers WHERE customer_ipn={customer_ipn};
        """)
