from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from view import Ui_MainWindow
from model import TemperatureModel


class TemperatureController(QMainWindow):

    def __init__(self):
        super().__init__()

        # Initialize Model
        self.model = TemperatureModel()

        # Initialize View
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_convert.clicked.connect(self.on_convert_clicked)

    @Slot()
    def on_convert_clicked(self):
        celsius_input = self.ui.input_celsius.text()

        # Validate and set in model
        if self.model.set_celsius(celsius_input):
            fahrenheit = self.model.celsius_to_fahrenheit()
            self.ui.output_fahrenheit.setText(f"{fahrenheit:.2f} °F")
        else:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid number.")
            self.ui.output_fahrenheit.setText("--")
