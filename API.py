from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QDialog,
                             QHBoxLayout)
import hashlib
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Function to initialize the Google Sheets connection


def init_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = (ServiceAccountCredentials.from_json_keyfile_name
             (r'C:\Users\el_he\Desktop\bio-cap-c9841b6b39e2.json', scope))
    # Update the path to your downloaded credentials
    client = gspread.authorize(creds)
    sheet = client.open('Credentials').sheet1  # Update with your Google Sheet name
    return sheet


def init_google_sheets1():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = (ServiceAccountCredentials.from_json_keyfile_name
             (r'C:\Users\el_he\Desktop\bio-cap-c9841b6b39e2.json', scope))
    # Update the path to your downloaded credentials
    client = gspread.authorize(creds)
    sheet = client.open('Bio-Data').sheet1  # Update with your Google Sheet name
    return sheet


# Function to find a user in the Google Sheet
def find_user(username, hashed_password):
    sheet = init_google_sheets()
    users = sheet.get_all_records()
    for user in users:
        if user['Username'] == username and user['PasswordHash'] == hashed_password:
            return True
    return False


# Function to add a new user to the Google Sheet
def add_user(username, hashed_password):
    sheet = init_google_sheets()
    sheet.append_row([username, hashed_password])


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

    def switch_to_signin(self):
        self.done(0)  # Close the sign-up dialog with a rejection code 0
    # ... (rest of the SignUpDialog code remains unchanged) ...

    def register_user(self):
        username = self.username.text()
        password = self.password.text()
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Add user to Google Sheets
        add_user(username, hashed_password)

        # Successful data entry alert
        QMessageBox.information(self, "Success", "You have signed up successfully!")
        self.accept()


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

    # ... (rest of the LoginDialog code remains unchanged) ...

    def check_credentials(self):
        username = self.username.text()
        password = self.password.text()
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Check credentials against Google Sheets
        if find_user(username, hashed_password):
            self.accept()  # Closes the dialog box and continues
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")
            self.username.clear()
            self.password.clear()


# ConfirmDialog Class
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

# ... (ConfirmDialog code remains unchanged) ...
        try:
            sheet.append_row([first_name, middle_name, last_name, age])
        except Exception as e:
            print("An error occurred:", e)


# BioDataApp Class
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

    # ... (rest of the BioDataApp code remains unchanged) ...

    def submitData(self):
        age = int(self.age.text())
        first_name = self.firstName.text()
        middle_name = self.middleName.text()
        last_name = self.lastName.text()

        # Write data to Google Sheets
        sheet = init_google_sheets1()
        sheet.append_row([first_name, middle_name, last_name, age])

        # Show a SUCCESS message box when data is submitted
        QMessageBox.information(self, "Success", "Data submitted successfully!")

        # Clear the form fields for a new entry
        self.firstName.clear()
        self.middleName.clear()
        self.lastName.clear()
        self.age.clear()

# ... (rest of your application code) ...


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
