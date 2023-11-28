from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
import pyodbc


# noinspection PyUnresolvedReferences
class BioDataApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bio-Data Collection Application')  # Set window title

        layout = QVBoxLayout()

        self.firstName = QLineEdit()
        self.firstName.setPlaceholderText("Enter first name")  # Set placeholder text
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
        submitButton.clicked.connect(self.submitData)  # PyCharm might show a warning here, but it's safe to ignore
        layout.addWidget(submitButton)

        self.setLayout(layout)

    def submitData(self):
        # Check if age input is an integer
        try:
            age = int(self.age.text())
        except ValueError:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Invalid input for age. Please enter an integer.")
            msgBox.exec_()
            return

        print("First Name:", self.firstName.text())
        print("Middle Name:", self.middleName.text())
        print("Last Name:", self.lastName.text())
        print("Age:", age)

        # Connect to the MS Access database and insert the data
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\el_he\Desktop\BIO_DATA.accdb;'  # replace with the path to your database
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO BIO_DATA (FirstName, MiddleName, LastName, Age)
            VALUES (?, ?, ?, ?)
        ''', (self.firstName.text(), self.middleName.text(), self.lastName.text(), age))
        conn.commit()
        conn.close()

        # Show a message box when data is submitted
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Data submitted successfully!")
        msgBox.exec_()

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
