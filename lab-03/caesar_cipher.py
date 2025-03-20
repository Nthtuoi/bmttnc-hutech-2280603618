import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnEN.clicked.connect(self.call_api_encrypt)
        self.ui.btnDE.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            "plain_text": self.ui.txtplaintext.toPlainText(),
            "key": self.ui.txtkey.toPlainText()  # ✅ Sửa từ .text() thành .toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtcipher.setPlainText(data["encrypted_message"])  # ✅ Sử dụng setPlainText thay vì setText

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)  # ✅ Sửa .information thành QMessageBox.Information
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))  # ✅ Sửa e.message thành str(e)

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            "cipher_text": self.ui.txtcipher.toPlainText(),  # ✅ Xóa dấu cách thừa trong "cipher_text"
            "key": self.ui.txtkey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtplaintext.setPlainText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))  # ✅ Sửa e.message thành str(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
