from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QStandardItem, QStandardItemModel, QPixmap
from PyQt5.QtCore import pyqtSignal, QByteArray, QSize, Qt
from PyQt5 import uic

import sys, pyodbc, os
import base64

from app.sql_manager import DataBase




class ManagerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"design\manager_win.ui", self)
        self.setWindowTitle("DataBase")
        self.db = DataBase(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=KLABSQLW19S1,49172;Trusted_Connection=yes; "
            "user=22200322; Database=DB_for_python_lessons;"
        )
        # Объявление таблицы
        self.model = QStandardItemModel(self)
        self.tableView.setModel(self.model)
        # self.model.setHorizontalHeaderLabels(['ID', 'Имя', 'Номер телефона', 'Роль', 'Пароль', 'Хеш пароля'])
        self.load_data()

        # Подключение кнопок
        self.add_data.clicked.connect(self.add_data_button)
        self.del_data.clicked.connect(self.delete)
        self.edit_data.clicked.connect(self.edit_data_button)

    def load_data(self):
        self.model.clear()
        data = self.db.get_info()

        for row in data:
            # print(row)
            items = [QStandardItem(str(field)) for field in row]
            self.model.appendRow(items)

    def close_data(self):
        close = self.db.close_db(self.database)

        if not close:
            print("База данных активна")
        else:
            pyodbc.pooling = False
            print("База данных выключена")

    def add_data_button(self):
        self.add = Add_data_window(self.db)
        self.add.setFixedSize(718, 410)
        self.add.data_added.connect(self.load_data)
        self.add.show()

    def delete(self):
        selected_index = self.tableView.selectedIndexes()
        if not selected_index:
            QMessageBox.warning(
                self, "Предупреждение", "Пожалуйста, выберите строку для удаления."
            )
            return

        row_to_delete = selected_index[0].row()
        val_product_id = self.model.item(row_to_delete, 0).text()
        val_product_name = self.model.item(row_to_delete, 1).text()
        val_product_price = self.model.item(row_to_delete, 2).text()
        val_product_count = self.model.item(row_to_delete, 3).text()
        val_product_path = self.model.item(row_to_delete, 4).text()
        val_product_data = self.model.item(row_to_delete, 5).text()

        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Подтверждение")
            msg_box.setText("Вы уверены, что хотите продолжить?")
            msg_box.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
            result = msg_box.exec_()
            if result == QMessageBox.Ok:
                self.db.delete_user(
                    val_product_id,
                    val_product_name,
                    val_product_price,
                    val_product_count,
                    val_product_path,
                    val_product_data
                )
                # print(selected_user_id, selected_username, selected_user_last_name, selected_user_role, selected_user_password)
                QMessageBox.information(self, "Успех", "Данные удалены успешно.")
                self.model.removeRow(row_to_delete)
            else:
                QMessageBox.information(self, "Успех", "Действие отменено")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            print(e)

    def edit_data_button(self):
        selected_index = self.tableView.selectedIndexes()
        if not selected_index:
            QMessageBox.warning(
                self, "Предупреждение", "Пожалуйста, выберите строку для удаления."
            )
            return

        row = selected_index[0].row()
        val_product_id = self.model.item(row, 0).text()
        val_product_name = self.model.item(row, 1).text()
        val_product_price = self.model.item(row, 2).text()
        val_product_count = self.model.item(row, 3).text()
        # val_product_path = self.model.item(row_to_delete, 4).text()
        val_product_data = self.model.item(row, 5).data()
        self.edit = Edit_data_window(
            self.db,
            val_product_id,
            val_product_name,
            val_product_price,
            val_product_count,
            val_product_data
        )
        self.edit.setFixedSize(857, 444)
        self.edit.data_edit.connect(self.load_data)
        self.edit.show()


class Add_data_window(QMainWindow):
    data_added = pyqtSignal()

    def __init__(self, db):
        super().__init__()
        uic.loadUi(r"design\manager_add_product.ui", self)
        self.setWindowTitle("Add data")
        self.model = QStandardItemModel(self)
        self.add_product.clicked.connect(self.append_data)
        self.check_image.clicked.connect(self.check)
        self.db = db
        self.main_window = ManagerWindow()

        self.file_path = ''
        self.file_name = ''

    def check(self):
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        self.file_name = os.path.basename(self.file_path[0])
        if self.file_path:
            pixmap = QPixmap(self.file_path)
            if pixmap.isNull():
                QMessageBox.warning(self, 'Ошибка', "Вознилка ошибка при загрузке изображения")
            else:
                scaled_image = pixmap.scaled(300, 300)
                self.image_label.setPixmap(scaled_image)

    def append_data(self):
        product_name = self.product_name.text()
        price = self.product_price.text()
        count = self.product_count.text()
        # path = self.product_path.text()
        self.db.add_product(product_name, int(price), int(count), self.file_path)
        self.data_added.emit()
        # Уведомление и завершение работы окна Add_data_window
        QMessageBox.information(self, "Успех", "Данные успешно добавлены")
        self.file_path = ''
        Add_data_window.close(self)


class Edit_data_window(QMainWindow):
    data_edit = pyqtSignal()

    def __init__(
        self,
        db,
        val_id,
        val_name,
        val_price,
        val_count,
        val_data
    ):
        super().__init__()
        uic.loadUi(r"design\edit_data_form.ui", self)
        self.setWindowTitle("Edit data")
        self.model = QStandardItemModel(self)
        self.pushButton.clicked.connect(self.edit_data)
        self.take_photo.clicked.connect(self.check)
        self.name_input.setText(val_name)
        self.price_input.setText(val_price)
        self.count_input.setText(val_count)
        self.product_id = val_id
        self.db = db
        print(f'тип данных: {type(val_data)}')
        print(f"\nproduct name: {val_name},\nID: {val_id}\n")
        pixmap = QPixmap()
        pixmap.loadFromData(val_data)
        scaled_pixmap = pixmap.scaled(200, 200)
        self.image_label.setPixmap(scaled_pixmap)

    def check(self):
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.jpg *.png *.jpeg *.bmp *.gif)", options=options)
        self.file_name = os.path.basename(self.file_path[0])
        if self.file_path:
            pixmap = QPixmap(self.file_path)
            if pixmap.isNull():
                QMessageBox.warning(self, 'Ошибка', "Вознилка ошибка при загрузке изображения")
            else:
                scaled_image = pixmap.scaled(300, 300)
                self.image_label.setPixmap(scaled_image)

    def edit_data(self):
        try:
            new_name = self.name_input.text()
            new_price = self.price_input.text()
            new_count = self.count_input.text()
            print(
                f"\nproduct_name: {new_name},\n product_price: {new_price}\nproduct_count: {new_count}"
            )
            # добавление данных в БД
            print(self.file_path)
            self.db.update_product(
                self.product_id,
                new_name,
                int(new_price),
                int(new_count),
                self.file_path
            )
            self.data_edit.emit()
            QMessageBox.information(self, "Успех", "Данные обновлены")
            self.file_path = ''
            Edit_data_window.close(self)
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", "Не удалось выполнить запрос(")
            print(f"Запрос не удалось реализовать(. Ошибка: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ManagerWindow()
    window.setFixedSize(784, 600)
    window.show()
    sys.exit(app.exec())
