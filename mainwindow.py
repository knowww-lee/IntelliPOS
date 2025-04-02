import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from database.auth import authenticate_user
from ui.login_ui import Ui_LoginWindow
from ui.pos_ui import Ui_POSWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("IntelliPOS - Login")
        self.ui.loginButton.clicked.connect(self.handle_login)

    def handle_login(self):
        """Authenticate user securely using hashed passwords."""
        username = self.ui.usernameField.text().strip()
        password = self.ui.passwordField.text().strip()

        if not username or not password:
            self.ui.errordisplayLabel.setText("Fields cannot be empty!")
            return

        if authenticate_user(username, password):
            self.ui.errordisplayLabel.setText("Login Successful!")
            self.ui.errordisplayLabel.setStyleSheet("color: green;")
            self.open_pos_window()
        else:
            self.ui.errordisplayLabel.setText("Invalid Username or Password!")
            self.ui.errordisplayLabel.setStyleSheet("color: red;")

    def open_pos_window(self):
        """Open the POS system window after successful login."""
        self.pos_window = POSWindow()
        self.pos_window.show()
        self.close()

class POSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_POSWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("IntelliPOS - Point of Sale")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
