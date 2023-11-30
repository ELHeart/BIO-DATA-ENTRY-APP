from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QDialog, \
    QHBoxLayout

import pyodbc


# noinspection PyUnresolvedReferences
class ConfirmDialog(QDialog):
    def __init__(self, parent, first_name, middle_name, last_name, age):
        super().__init__(parent)
        self.setWindowTitle('Confirm Data')

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"First Name: {first_name}"))
        layout.addWidget(QLabel(f"Middle Name: {middle_name}"))
        layout.addWidget(QLabel(f"Last Name: {last_name}"))
        layout.addWidget(QLabel(f"Age: {age}"))

        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)
        button_layout.addWidget(self.confirm_button)

        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.reject)
        button_layout.addWidget(self.edit_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)


class BioDataApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bio-Data Collection Application')

        layout = QVBoxLayout()

        self.firstName = QLineEdit()
        self.firstName.setPlaceholderText("Enter first name")
        self.middleName = QLineEdit()
        self.middleName.setPlaceholderText("Enter middle name (Skip if none)")
        self.lastName = QLineEdit()
        self.lastName.setPlaceholderText("Enter last name")
        self.age = QLineEdit()
        self.age.setPlaceholderText("Enter age")

        layout.addWidget(QLabel("First Name:"))
        layout.addWidget(self.firstName)
        layout.addWidget(QLabel("Middle Name (Skip if none):"))
        layout.addWidget(self.middleName)
        layout.addWidget(QLabel("Last Name:"))
        layout.addWidget(self.lastName)
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age)

        submitButton = QPushButton("Submit")
        # noinspection PyUnresolvedReferences
        submitButton.clicked.connect(self.showConfirmDialog)
        layout.addWidget(submitButton)

        self.setLayout(layout)

    def showConfirmDialog(self):
        # Check if age input is an integer
        try:
            age = int(self.age.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Invalid input for age. Please enter an integer.")
            return

        dialog = ConfirmDialog(self, self.firstName.text(), self.middleName.text(), self.lastName.text(), age)
        if dialog.exec_():
            self.submitData()

    def submitData(self):
        age = int(self.age.text())
        print("First Name:", self.firstName.text())
        print("Middle Name:", self.middleName.text())
        print("Last Name:", self.lastName.text())
        print("Age:", age)

        # Connect to the MS Access database and insert the data
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\el_he\Desktop\BIO_DATA.accdb;'
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute('''
                   INSERT INTO BIO_DATA (FirstName, MiddleName, LastName, Age)
                   VALUES (?, ?, ?, ?)
               ''', (self.firstName.text(), self.middleName.text(), self.lastName.text(), age))
        conn.commit()
        conn.close()
        # ... (database code remains the same)

        # Show a SUCCESS message box when data is submitted
        QMessageBox.information(self, "Success", "Data submitted successfully!")

        # Clear the form fields for a new entry
        self.firstName.clear()
        self.middleName.clear()
        self.lastName.clear()
        self.age.clear()


if __name__ == '__main__':
    app = QApplication([])
    ex = BioDataApp()
    ex.show()
    app.exec_()
