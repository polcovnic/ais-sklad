import psycopg2


def create_tables(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS categories(
                    category_id integer GENERATED ALWAYS AS IDENTITY,
                    name varchar(47) NOT NULL,
                    notes varchar(197) NOT NULL,
                    PRIMARY KEY (category_id));
                    
                CREATE TABLE IF NOT EXISTS products(
                    product_id integer GENERATED ALWAYS AS IDENTITY,
                    name varchar(49) NOT NULL,
                    notes varchar(199) NULL,
                    producer_edrpou integer NOT NULL,
                    category_id integer NOT NULL,
                    price integer NOT NULL,
                    PRIMARY KEY(product_id),
                    CONSTRAINT category_id
                        FOREIGN KEY (category_id)
                            REFERENCES categories(category_id));                

                CREATE TABLE IF NOT EXISTS producers(
                    edrpou integer NOT NULL,
                    name varchar(49) NOT NULL,
                    notes varchar(199) NOT NULL,
                    email varchar(49) NOT NULL,
                    phone_number varchar(19) NOT NULL,
                    country varchar(19) NOT NULL,
                    state varchar(19) NOT NULL,
                    city varchar(19) NOT NULL,
                    street varchar(49) NOT NULL,
                    house_number integer NOT NULL
                    );
                    
                CREATE TABLE IF NOT EXISTS customers(
                    customer_ipn integer NOT NULL,
                    notes varchar(199) NOT NULL,
                    name varchar(49) NOT NULL,
                    surname varchar(49) NOT NULL,
                    patronymic varchar(49) NOT NULL,
                    country varchar(49) NOT NULL,
                    state varchar(49) NOT NULL,
                    city varchar(49) NOT NULL,
                    street varchar(49) NOT NULL,
                    house_number varchar(49) NOT NULL,
                    phone_number varchar(19) NOT NULL,
                    email varchar(49) NOT NULL,
                    debt integer NOT NULL,
                    UNIQUE (customer_ipn)
                );
                    
                CREATE TABLE IF NOT EXISTS orders(
                    order_id integer GENERATED ALWAYS AS IDENTITY,
                    notes varchar(199) NOT NULL,
                    date varchar(29) NOT NULL,
                    customer_ipn integer NOT NULL,
                    sum integer NOT NULL,
                    PRIMARY KEY (order_id),
                    CONSTRAINT customer_ipn
                        FOREIGN KEY (customer_ipn)
                            REFERENCES customers(customer_ipn)
                    );
                CREATE TABLE IF NOT EXISTS order_rows(
                    order_row_id integer GENERATED ALWAYS AS IDENTITY,
                    order_id integer,
                    sum integer NOT NULL,
                    amount integer NOT NULL,
                    product_id integer NOT NULL,
                    PRIMARY KEY (order_row_id),
                    CONSTRAINT product_id
                        FOREIGN KEY (product_id)
                            REFERENCES products(product_id),
                    CONSTRAINT order_id
                        FOREIGN KEY (order_id)
                            REFERENCES orders(order_id)
                    );
                    
                
                    INSERT INTO categories (name, notes) VALUES ('Солодощі', 'Печиво та цукерки');
                    INSERT INTO categories (name, notes) VALUES ('Техніка', '');

                    INSERT INTO products (name, notes, producer_edrpou, category_id, price) VALUES
                    ('Lovita', 'Печиво з шоколадом', 12345, 1, 20);

                    INSERT INTO products (name, notes, producer_edrpou, category_id, price) VALUES
                    ('Червоний мак', 'Цукерки', 12345, 1, 20);


                    INSERT INTO producers (edrpou, name, notes, email, phone_number, country, state, city, street, house_number)
                    VALUES (12345,'Roshen', 'Кондитерська компанія Пороха', 'roshen@mail.com', '+380958676823', 'Україна',
                    'Київська обл.', 'Київ', 'Бандери', '47');
             """)


# try:
#     connection = psycopg2.connect(
#         host='ec2-34-253-29-48.eu-west-1.compute.amazonaws.com',
#         user='ahhrknbvzyhpxs',
#         password='bc4532ad71e5d34c05bd29cfda94516bb7b242ae1fa643f613cd2fc99ec7dfa6',
#         database='dbptm0c8o662b4'
#     )
#     connection.autocommit = True
#     create_tables(connection)
# except Exception as e:
#     print(e)


def connection_dec(my_func):
    def wrapper(*args, **kwargs):
        try:
            connection = psycopg2.connect(
                host='ec2-34-253-29-48.eu-west-1.compute.amazonaws.com',
                user='ahhrknbvzyhpxs',
                password='bc4532ad71e5d34c05bd29cfda94516bb7b242ae1fa643f613cd2fc99ec7dfa6',
                database='dbptm0c8o662b4'
            )
            connection.autocommit = True
            return my_func(connection, *args, **kwargs)
        except Exception as e:
            print(e)

    return wrapper
