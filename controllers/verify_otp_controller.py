from PyQt5.QtWidgets import QMessageBox, QPushButton, QDialog

from verify_otp_ui import Ui_verifyOtpForm
import user_utils


class VerifyOtpController(Ui_verifyOtpForm):
    def __init__(self, user):
        self.user = user
        self.successful = False
        self.closeDialog = QPushButton()

    def setupUi(self, verifyOtpForm):
        super().setupUi(verifyOtpForm)
        self.verifyOtpButton.clicked.connect(self.verify_otp)
        self.resendOtpButton.clicked.connect(self.resend_otp)
        self.closeDialog.clicked.connect(verifyOtpForm.close)

    def display_message(self, status_code, message):
        message_box = QMessageBox()
        message_box.setWindowTitle(status_code)
        message_box.setText(message)

        if status_code == "Success":
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.setIcon(QMessageBox.Information)
            if self.successful:
                message_box.finished.connect(self.on_message_box_close)
        else:
            message_box.setStandardButtons(QMessageBox.Cancel)
            message_box.setIcon(QMessageBox.Warning)

        message_box.exec_()

    def on_message_box_close(self):
        from controllers import login_controller
        self.closeDialog.click()
        loginDialog = QDialog()
        loginController = login_controller.LoginController()
        loginController.setupUi(loginDialog)
        loginDialog.exec_()

    def verify_otp(self):
        code = self.otpCodeInput.text()
        if not code:
            self.display_message("Error", "Please enter your OTP code")
            return

        status_code, response = user_utils.verify_otp({"send_to": self.user, "code": code})

        if not status_code:
            self.display_message("Error", response)
            return
        self.successful = True
        self.display_message("Success", response)

    def resend_otp(self):
        status_code, response = user_utils.resend_otp({"send_to": self.user})

        if not status_code:
            self.display_message("Error", response)
            return

        self.display_message("Success", response)
