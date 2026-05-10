import sys
from PySide6.QtWidgets import QApplication
from controller import TemperatureController


def main():
    app = QApplication(sys.argv)

    # Create and show controller
    controller = TemperatureController()
    controller.show()

    # Starts event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
