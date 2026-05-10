# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view.ui'
##
## Created by: Qt User Interface Compiler version 6.x.x
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 150)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.verticalLayout.addWidget(self.label)

        self.input_celsius = QLineEdit(self.centralwidget)
        self.input_celsius.setObjectName(u"input_celsius")
        self.verticalLayout.addWidget(self.input_celsius)

        self.btn_convert = QPushButton(self.centralwidget)
        self.btn_convert.setObjectName(u"btn_convert")
        self.verticalLayout.addWidget(self.btn_convert)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.output_fahrenheit = QLabel(self.centralwidget)
        self.output_fahrenheit.setObjectName(u"output_fahrenheit")
        self.verticalLayout.addWidget(self.output_fahrenheit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Temperature Converter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter Celsius:", None))
        self.btn_convert.setText(QCoreApplication.translate("MainWindow", u"Convert to Fahrenheit", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fahrenheit:", None))
        self.output_fahrenheit.setText(QCoreApplication.translate("MainWindow", u"--", None))
    # retranslateUi
