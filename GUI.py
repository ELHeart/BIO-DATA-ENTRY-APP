from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QDialog,
                             QHBoxLayout)
import pyodbc
import hashlib


# SignUpDialog class creates a sign-up dialog box
class SignUpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sign Up')  # Dialog box title
        self.setModal(True)

        layout = QVBoxLayout()

        # Username and password entry points.
        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter password")
        self.password.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password)

        # Sign up button creation
        signup_button = QPushButton("Sign Up")
        signup_button.clicked.connect(self.register_user)
        layout.addWidget(signup_button)

        # Button to switch to the Sign In window
        signin_button = QPushButton("Sign In")
        signin_button.clicked.connect(self.switch_to_signin)
        layout.addWidget(signin_button)

        self.setLayout(layout)

    # Function for user sign-up information storage
    def register_user(self):
        username = self.username.text()
        password = self.password.text()

        # Hashes the entered password into hexadecimals
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Connect to the MS Access database to insert new user data
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\el_he\Desktop\BIO-CAP-DATABASE FILES\BIO-CAP-SIGN-UP.accdb;'
            # Path to database for new user data information storage
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Users (Username, PasswordHash) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        conn.close()

        # Successful data entry alert
        QMessageBox.information(self, "Success", "You have signed up successfully!")
        self.accept()

    def switch_to_signin(self):
        self.done(0)  # Close the sign-up dialog with a rejection code 0


# Login Dialog Class
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setModal(True)

        layout = QVBoxLayout()

        # Login Data entry
        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter password")
        self.password.setEchoMode(QLineEdit.Password)

        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password)

        # Login Button creation and credentials check
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.check_credentials)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def check_credentials(self):
        username = self.username.text()
        password = self.password.text()

        # Hash the entered password
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Connect to the MS Access database to check credentials
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\el_he\Desktop\BIO-CAP-DATABASE FILES\BIO-CAP-SIGN-UP.accdb;'
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Users WHERE Username=? AND PasswordHash=?', (username, hashed_password))
        result = cursor.fetchone()
        conn.close()

        # Credentials check
        if result:
            self.accept()  # Closes the dialog box and continues
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
            self.username.clear()               # Wrong data entry.
            self.password.clear()


# ConfirmDialog Class
# The dialog box for users to confirm data entry into the database.
class ConfirmDialog(QDialog):
    def __init__(self, parent, first_name, middle_name, last_name, age):
        super().__init__(parent)
        self.setWindowTitle('Confirm Data')

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"First Name: {first_name}"))
        layout.addWidget(QLabel(f"Middle Name: {middle_name}"))
        layout.addWidget(QLabel(f"Last Name: {last_name}"))
        layout.addWidget(QLabel(f"Age: {age}"))

        # Confirm Button creation
        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)
        button_layout.addWidget(self.confirm_button)

        # Edit Button creation
        self.edit_button = QPushButton("Edit")
        self.edit_button.clicked.connect(self.reject)
        button_layout.addWidget(self.edit_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)


# BioDataApp Class
# This is the main application class that specifies the data entry form for the application
class BioDataApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bio-Data Collection Application')      # Title bar name

        layout = QVBoxLayout()

        # Data Entry field creation
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

        # Submit button creation
        submitButton = QPushButton("Submit")
        # noinspection PyUnresolvedReferences
        submitButton.clicked.connect(self.showConfirmDialog)
        layout.addWidget(submitButton)

        self.setLayout(layout)

    def showConfirmDialog(self):
        # Checks if age input is an integer
        try:
            age = int(self.age.text())
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Invalid input for age. Please enter an integer.")
            return

        dialog = ConfirmDialog(self, self.firstName.text(), self.middleName.text(), self.lastName.text(), age)
        if dialog.exec_():
            self.submitData()

    # Function enters the data into the connection database file.
    def submitData(self):
        age = int(self.age.text())
        print("First Name:", self.firstName.text())
        print("Middle Name:", self.middleName.text())
        print("Last Name:", self.lastName.text())
        print("Age:", age)

        # Connects to the MS Access database and inserts the data
        conn_str = (
            r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\Users\el_he\Desktop\BIO-CAP-DATABASE FILES\BIO_DATA.accdb;'
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute('''
                   INSERT INTO BIO_DATA (FirstName, MiddleName, LastName, Age)
                   VALUES (?, ?, ?, ?)
               ''', (self.firstName.text(), self.middleName.text(), self.lastName.text(), age))
        conn.commit()
        conn.close()

        # Show a SUCCESS message box when data is submitted
        QMessageBox.information(self, "Success", "Data submitted successfully!")

        # Clear the form fields for a new entry
        self.firstName.clear()
        self.middleName.clear()
        self.lastName.clear()
        self.age.clear()


if __name__ == '__main__':
    app = QApplication([])

    # Shows the sign-up dialog first
    signup = SignUpDialog()
    result = signup.exec_()

    # If the user closes the sign-up dialog or clicks "Sign In", show the login dialog
    if result == QDialog.Rejected:
        login = LoginDialog()
        if login.exec_() == QDialog.Accepted:
            ex = BioDataApp()
            ex.show()
            app.exec_()
    else:
        login = LoginDialog()
        if login.exec_() == QDialog.Accepted:
            ex = BioDataApp()
            ex.show()
            app.exec_()
