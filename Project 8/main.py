import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from asn8_ui import Ui_root


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_root()
        self.ui.setupUi(self)

        self.ui.btnS.clicked.connect(self.handle_submit)
        self.ui.btnR.clicked.connect(self.handle_reset)
        self.ui.btnQ.clicked.connect(self.handle_quit)

    def handle_submit(self):
        first_name = self.ui.entFirst.text()
        last_name = self.ui.entLast.text()
        email = self.ui.entEmail.text()
        phone = self.ui.entPhone.text()

        if not first_name.strip() or not last_name.strip():
            QMessageBox.warning(self, "Validation Error",
                            "First Name and Last Name are required.")
            return

        print(f"Submitted: {first_name} {last_name}, {email}, {phone}")
        QMessageBox.information(self, "Success", "Data submitted successfully!")

    def handle_reset(self):
        self.ui.entFirst.clear()
        self.ui.entLast.clear()
        self.ui.entEmail.clear()
        self.ui.entPhone.clear()

    def handle_quit(self):
        self.close()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
