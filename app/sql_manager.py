import pyodbc

class DataBase:
    def __init__(self, conn_str):
        self.connect = pyodbc.connect(conn_str)
        self.cursor = self.connect.cursor()

    def get_info(self):
        with self.connect:
            return self.cursor.execute("""SELECT * FROM products_tb""").fetchall()

    def add_product(self, product_name, price, count, file_path):
        with self.connect:
            try:
                with open(file_path, 'rb') as file:
                    # print(file)
                    # print(file_path)
                    binary_data = file.read()
            except Exception as e:
                print(e)
            return self.cursor.execute("""INSERT INTO products_tb (product_name, price, count, imageData) VALUES (?, ?, ?, ?)""", 
            (product_name, price, count, binary_data))

    def update_product(self, product_id, product_name, price, count, file_path):
        with self.connect:
            try:
                with open(file_path, 'rb') as file:
                    # print(file)
                    # print(file_path)
                    binary_data = file.read()
            except Exception as e:
                print(e)
            return self.cursor.execute("""UPDATE products_tb SET product_name=(?), price=(?), count=(?), imageData=(?) WHERE product_id=(?)""", (product_name, price, count, binary_data, product_id))
        
    def delete_user(self, product_id, product_name, price, count, path, imageData):
        with self.connect:
            return self.cursor.execute("""DELETE FROM products_tb WHERE product_id = (?) AND product_name = (?) AND price = (?) AND count = (?) AND path=(?) AND imageData=(?)""", 
                                        (product_id, product_name, price, count, path, imageData))
        