from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QByteArray
from PyQt5 import uic
from PyQt5 import Qt

import sys
import os

import pyodbc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('open_files.ui', self)
        self.file_name = ''
        self.file_path = ''
        self.output_image = ''
        # button
        self.open_explorer.clicked.connect(self.explorer)
        self.add_data.clicked.connect(self.add_file)

        self.conn = pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; "
            "user=22200322; Database=DB_for_python_lessons;")
        self.cursor = self.conn.cursor()

    def explorer(self):
        self.file_path = QFileDialog.getOpenFileName(self, 'single file')
        self.file_name = os.path.basename(self.file_path[0])
        print(self.file_name)
        print(self.file_path)

    def add_file(self):
        try:
            with open(self.file_path[0], 'rb') as file:
                with self.conn:
                    print(file)
                    print(self.file_path[0])
                    binary_data = file.read()
                    query = '''INSERT INTO products_tb (product_name, imageData) VALUES(?, ?)'''
                    self.cursor.execute(query, (self.file_name, binary_data))
                    self.open_image(binary_data, self.file_name)
        except Exception as e:
            print(e)

    def open_image(self, binaryData, file_name):
        pixmap = QPixmap()
        pixmap.loadFromData(QByteArray(binaryData))
        scaled_pixmap = pixmap.scaled(300, 300)
        self.label.setText(file_name)
        self.image_label.setPixmap(scaled_pixmap)
        # self.image_label.setFixedSize(200,200)
        # try:
        #     with self.conn:
        #         query = """SELECT product_name, imageData FROM products_tb WHERE product_id=(?)"""
        #         row = self.cursor.execute(query, (id, )).fetchone()

        #         if row:
        #             product_name, imageData = row
        #             with open(output_path, 'wb') as file:
        #                 file.write(imageData)
        #                 print(product_name + 'загружен')


        # except Exception as e:
        #     print(e)
                


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())