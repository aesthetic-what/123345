import pyodbc

class DataBase:
    def __init__(self, str_conn):
        self.connect = pyodbc.connect(str_conn)
        self.cursor = self.connect.cursor()

    def get_info(self):
        """
        Это функция для вывода товаров в каталог
        """
        with self.connect:
            return self.cursor.execute("""SELECT product_id, product_name, price, count, path FROM products_tb""").fetchall()

    def buy_prod(self, count, product_name):
        """
        Покупка товара
        """
        with self.connect:
            return self.cursor.execute("""UPDATE products_tb SET count=(?) WHERE product_name=(?)""", (count, product_name,))

    def change_info(self, articule, new_name):
        """При отстутсвии товара (количество = 0) изменяет название товара"""
        with self.connect:
            return self.cursor.execute("""UPDATE products_tb SET product_name=(?) WHERE product_id=(?)""", (articule, new_name))

    def check_user(self, login):
        with self.connect:
            result = self.cursor.execute("""SELECT * FROM users WHERE login = ?""", (login, )).fetchone()
            if result is not None:
                return False
            else:
                return True

    def login_user(self, login):
        with self.connect:
            return self.cursor.execute("""SELECT login, username, password, role FROM users WHERE login=(?)""", (login, )).fetchone()

    def add_user(self, login, username, password):
        with self.connect:
            return self.cursor.execute("""INSERT INTO users (login, username, role, password) VALUES (?, ?, ?, ?)""", (login, username, 'user', password))

    def get_info_product(self):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM products_tb""").fetchall()

    def add_product(self, product_name, price, count, product_path):
        with self.connect:
            return self.cursor.execute("""INSERT INTO products_tb (product_name, price, count, path) VALUES (?, ?, ?, ?)""", 
            (product_name, price, count, product_path))

    def update_product(self, product_id, product_name, price, count, path):
        with self.connect:
            return self.cursor.execute("""UPDATE products_tb SET product_name=(?), price=(?), count=(?), path=(?) WHERE product_id=(?)""", (product_name, price, count, path, product_id))
        
    def delete_user(self, product_id, product_name, price, count, path):
        with self.connect:
            return self.cursor.execute("""DELETE FROM products_tb WHERE product_id = (?) AND product_name = (?) AND price = (?) AND count = (?) AND path=(?)""", 
                                        (product_id, product_name, price, count, path))

    def get_info_users(self):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM users""").fetchall()

    def add_user(self, login, username, password):
        with self.connect:
            return self.cursor.execute("""INSERT INTO users (login, username, role, password) VALUES (?, ?, ?, ?)""",
                                       (login, username, 'user', password, ))

    def update_user(self, user_id, login, username, role, password):
        with self.connect:
            return self.cursor.execute("""UPDATE users SET login=(?), username=(?), role=(?), password=(?) WHERE user_id=(?)""", (login, username, role, password, user_id))

    def delete_user(self, user_id, login, username, role, password):
        with self.connect:
            return self.cursor.execute("""DELETE FROM users WHERE user_id=(?) AND login=(?) AND username=(?) AND role=(?) AND password=(?)""",
                                       (user_id, login, username, role, password))