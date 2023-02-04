import sys
import requests
from PyQt5.QtWidgets import QMessageBox, QDialog, QPushButton

import utils
import user_utils
from settings import BASE_URL
from login_ui import Ui_loginDialog
from controllers import registration_controller, verify_otp_controller


def error_display():
    error_dialog = QMessageBox()
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setText("Error")
    error_dialog.setInformativeText("This app is not genuine")
    error_dialog.setWindowTitle("Error")
    error_dialog.exec_()
    sys.exit(0)


class LoginController(Ui_loginDialog):
    def __init__(self, main_window=None):
        self.closeDialog = QPushButton()
        self.user = None
        self.main_window = main_window

    def setupUi(self, loginDialog):
        super().setupUi(loginDialog)
        self.loginButton.clicked.connect(self.login)
        self.closeDialog.clicked.connect(loginDialog.close)
        self.createAccountButton.clicked.connect(self.redirect_to_registration)

    def on_message_box_close(self):
        self.closeDialog.click()
        verifyOtpDialog = QDialog()
        verifyOtpController = verify_otp_controller.VerifyOtpController(self.user)
        verifyOtpController.setupUi(verifyOtpDialog)

        # resend otp
        user_utils.resend_otp({"send_to": self.user})
        verifyOtpDialog.exec_()

    def display_message(self, status_code, message):
        message_box = QMessageBox()
        message_box.setWindowTitle(status_code)
        message_box.setText(message)
        message_box.setStandardButtons(QMessageBox.Ok)

        if status_code == "Success":
            message_box.setIcon(QMessageBox.Information)
        else:
            message_box.setIcon(QMessageBox.Warning)
            if bool(self.user):
                message_box.finished.connect(self.on_message_box_close)

        message_box.exec_()

    def login(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()

        if not username or not password:
            self.display_message("Error", "Please enter a username and password")
            return

        url = f"{BASE_URL}/api/v1/users/auth/login"
        try:
            response = requests.post(url=url, json={"username": username, "password": password}, timeout=5)
            if response.status_code == 200:
                # The login request was successful, so accept the dialog and close it
                try:
                    resp = response.json()['message']
                    auth = resp['access_token']
                    refresh_token = resp['refresh_token']
                    jwtauth = resp['jwt_token']

                    # check if app is registered
                    if not utils.app_registered():
                        error_display()
                    utils.store_headers(auth, jwtauth, refresh_token)
                    self.closeDialog.click()

                    if self.main_window:
                        self.main_window.show()

                except KeyError:
                    self.display_message("Error", "Invalid response from server")
                    return
            else:
                # The login request was unsuccessful, so display an error message
                resp = response.json()
                if resp.get('user'):
                    self.user = resp['user']
                self.display_message("Error", resp['message'])
        except Exception as e:
            print(e)
            self.display_message("Error", "Make sure you are connected to the internet")

    def redirect_to_registration(self):
        self.closeDialog.click()
        registrationDialog = QDialog()
        registrationController = registration_controller.RegistrationController()
        registrationController.setupUi(registrationDialog)
        registrationDialog.exec_()
