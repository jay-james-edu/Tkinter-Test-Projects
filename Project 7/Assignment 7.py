
" A GUI-based application that converts measurements between Inches and Meters using PySide6. Layout designed to match provided reference screenshot."

import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout,
    QMessageBox, QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

INCH_TO_METER = 0.0254

class ConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Measurement Converter")
        self._build_ui()
        self._wire_events()
        self._reset_form()

    def _setup_image(self):
        """
        Setup the house image with robust path checking relative to the script location.
        Checks current directory, assets folder, and the script's specific directory.
        """
        self.imgFrame = QFrame()
        self.imgFrame.setStyleSheet("background-color: #2c3e50; border: 2px solid #3498db; border-radius: 5px;")
        self.imgLabel = QLabel(alignment=Qt.AlignCenter)

        # Get the directory where this script is located
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Define possible paths for the image
        possible_paths = [
            "house.png",
            "assets/house.png",
            os.path.join(script_dir, "house.png"),
            os.path.join(script_dir, "assets", "house.png")
        ]

        loaded = False
        for path in possible_paths:
            if os.path.exists(path):
                pix = QPixmap(path)
                if not pix.isNull():
                    self.imgLabel.setPixmap(pix.scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation))
                    loaded = True
                    break

        if not loaded:
            self.imgLabel.setText("Image not found")
            self.imgLabel.setStyleSheet("color: white;")

        vimg = QVBoxLayout(self.imgFrame)
        vimg.addWidget(self.imgLabel)

    def _build_ui(self):
        """Build and configure the user interface."""
        central = QWidget(self)
        self.setCentralWidget(central)

        # Main layout with image on the right
        main_layout = QHBoxLayout(central)

        content_layout = QVBoxLayout()
        content_layout.setSpacing(20)
        content_layout.setContentsMargins(10, 10, 10, 10)

        # Title section
        self.lblTitle = QLabel("Converter App")
        self.lblTitle.setStyleSheet("font-size: 24px; font-weight: bold; color: #ecf0f1;")
        self.lblTitle.setAlignment(Qt.AlignCenter)

        self.lblPrompt = QLabel("Enter a value and choose conversion")
        self.lblPrompt.setStyleSheet("font-size: 16px; color: #bdc3c7;")
        self.lblPrompt.setAlignment(Qt.AlignCenter)

        # Input section
        self.txtInput = QLineEdit()
        self.txtInput.setPlaceholderText("Enter a value")
        self.txtInput.setStyleSheet("font-size: 14px; padding: 8px; background-color: white; color: black;")

        # Radio group
        self.grp = QGroupBox("Convert Measurement")
        self.grp.setStyleSheet("color: #ecf0f1; font-size: 14px; font-weight: bold;")

        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbInToM.setStyleSheet("color: #ecf0f1; font-size: 12px;")

        self.rbMToIn = QRadioButton("Meters to Inches")
        self.rbMToIn.setStyleSheet("color: #ecf0f1; font-size: 12px;")

        vgrp = QVBoxLayout()
        vgrp.addWidget(self.rbInToM)
        vgrp.addWidget(self.rbMToIn)
        self.grp.setLayout(vgrp)

        # Result label
        self.lblResult = QLabel("")
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setStyleSheet("font-size: 16px; font-weight: bold; color: #2ecc71; background-color: #2c3e50; border: 2px solid #3498db; border-radius: 5px; padding: 10px;")

        # Button layout
        self.btnConvert = QPushButton("Convert")
        self.btnConvert.setStyleSheet("background-color: #2ecc71; color: white; font-size: 14px; font-weight: bold; padding: 8px 16px;")

        self.btnClear = QPushButton("Clear")
        self.btnClear.setStyleSheet("background-color: #f39c12; color: white; font-size: 14px; font-weight: bold; padding: 8px 16px;")

        self.btnExit = QPushButton("Exit")
        self.btnExit.setStyleSheet("background-color: #e74c3c; color: white; font-size: 14px; font-weight: bold; padding: 8px 16px;")

        hbtns = QHBoxLayout()
        hbtns.setSpacing(10)
        hbtns.addWidget(self.btnConvert)
        hbtns.addWidget(self.btnClear)
        hbtns.addWidget(self.btnExit)

        # Add all widgets to content layout
        content_layout.addWidget(self.lblTitle)
        content_layout.addWidget(self.lblPrompt)
        content_layout.addWidget(self.txtInput)
        content_layout.addWidget(self.grp)
        content_layout.addWidget(self.lblResult)
        content_layout.addStretch() 
        content_layout.addLayout(hbtns)

        self._setup_image()

        # Add content and image to main layout
        main_layout.addLayout(content_layout, 2)  
        main_layout.addWidget(self.imgFrame, 1)  

        # Main window styling
        self.setStyleSheet("""
            QMainWindow { background: #243447; }
            QLabel, QGroupBox, QRadioButton { color: #f0f0f0; font-size: 14px; }
            QPushButton { font-size: 14px; padding: 6px 12px; }
        """)

        # Explicit text input styling
        self.txtInput.setStyleSheet("font-size: 14px; padding: 6px; background-color: white; color: black;")

    def _wire_events(self):
        """Connect signals and slots for event handling."""
        self.btnConvert.clicked.connect(self.on_convert)
        self.btnClear.clicked.connect(self.on_clear)
        self.btnExit.clicked.connect(QApplication.instance().quit)

    def _reset_form(self):
        """Reset the form to initial state."""
        self.txtInput.clear()
        self.lblResult.setText("")
        self.rbInToM.setChecked(True)
        self.txtInput.setFocus()

    def _error(self, message: str):
        """Display error message box."""
        QMessageBox.critical(self, "Error", message)

    def on_clear(self):
        """Handle Clear button click."""
        self._reset_form()

    def on_convert(self):
        """Handle Convert button click."""
        text = self.txtInput.text().strip()
        if not text:
            self._error("Value entered is not numeric.")
            return
        try:
            value = float(text)
        except ValueError:
            self._error("Value entered is not numeric.")
            return
        if value <= 0:
            self._error("Converted value is negative.")
            return

        if self.rbInToM.isChecked():
            meters = value * INCH_TO_METER
            self.lblResult.setText(f"{value} inches is {meters:.3f} meters.")
        else:
            inches = value / INCH_TO_METER
            self.lblResult.setText(f"{value} meters is {inches:.3f} inches.")

def main():
    """Main function to run the application."""
    app = QApplication(sys.argv)
    w = ConverterWindow()
    w.resize(600, 400)
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()