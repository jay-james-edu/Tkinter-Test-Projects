import sys
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                               QVBoxLayout, QLabel, QLineEdit, 
                               QPushButton, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Number Generator")
        self.setMinimumSize(300, 250)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.layout = QVBoxLayout()
        central_widget.setLayout(self.layout)

        self.lblHelp = QLabel("Enter an integer greater than 2")
        self.lblHelp.setFont(QFont("Arial", 18))
        self.lblHelp.setStyleSheet("background-color: #79aa38; padding: 10px;")
        self.layout.addWidget(self.lblHelp)

        self.input = QLineEdit()
        self.input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.input)

        self.lblOutput = QLabel()
        self.lblOutput.setFont(QFont("Arial", 25))
        self.lblOutput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblOutput.setStyleSheet("background-color: #d85a28; padding: 10px;")
        self.layout.addWidget(self.lblOutput)

        self.btnRand = QPushButton("Random Numbers")
        self.layout.addWidget(self.btnRand)

        self.btnRand.pressed.connect(self.update_label)

    def update_label(self):
        input_text = self.input.text()

        try:
            val = int(input_text)
            if val < 2:
                QMessageBox.warning(self, "Warning", "Please enter an integer greater than 2.")
                return
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid integer.")
            return

        rand_num = random.randint(1, val)
        self.lblOutput.setText(str(rand_num))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())