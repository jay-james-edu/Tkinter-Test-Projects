# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asn8.ui'
##
## 
##
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)


class Ui_root(object):
    def setupUi(self, root):
        if not root.objectName():
            root.setObjectName("root")
        root.resize(500, 300)


        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(root.sizePolicy().hasHeightForWidth())
        root.setSizePolicy(sizePolicy)
        root.setBaseSize(500, 300)


        self.centralwidget = QWidget(root)
        self.centralwidget.setObjectName("centralwidget")


        self.lblFrPerson = QGroupBox(self.centralwidget)
        self.lblFrPerson.setObjectName("lblFrPerson")
        self.lblFrPerson.setGeometry(QRect(0, 0, 500, 241))


        self.gridLayout = QGridLayout(self.lblFrPerson)
        self.gridLayout.setObjectName("gridLayout")


        self.lblFirst = QLabel(self.lblFrPerson)
        self.lblFirst.setObjectName("lblFirst")
        self.lblFirst.setStyleSheet("background-color: blue; color: white;")
        self.gridLayout.addWidget(self.lblFirst, 0, 0, 1, 1)

        self.entFirst = QLineEdit(self.lblFrPerson)
        self.entFirst.setObjectName("entFirst")
        self.gridLayout.addWidget(self.entFirst, 0, 1, 1, 1)


        self.lblLast = QLabel(self.lblFrPerson)
        self.lblLast.setObjectName("lblLast")
        self.lblLast.setStyleSheet("background-color: blue; color: white;")
        self.gridLayout.addWidget(self.lblLast, 1, 0, 1, 1)

        self.entLast = QLineEdit(self.lblFrPerson)
        self.entLast.setObjectName("entLast")
        self.gridLayout.addWidget(self.entLast, 1, 1, 1, 1)


        self.lblEmail = QLabel(self.lblFrPerson)
        self.lblEmail.setObjectName("lblEmail")
        self.gridLayout.addWidget(self.lblEmail, 2, 0, 1, 1)

        self.entEmail = QLineEdit(self.lblFrPerson)
        self.entEmail.setObjectName("entEmail")
        self.gridLayout.addWidget(self.entEmail, 2, 1, 1, 1)


        self.lblPhone = QLabel(self.lblFrPerson)
        self.lblPhone.setObjectName("lblPhone")
        self.gridLayout.addWidget(self.lblPhone, 3, 0, 1, 1)

        self.entPhone = QLineEdit(self.lblFrPerson)
        self.entPhone.setObjectName("entPhone")
        self.gridLayout.addWidget(self.entPhone, 3, 1, 1, 1)


        self.fraButtons = QFrame(self.centralwidget)
        self.fraButtons.setObjectName("fraButtons")
        self.fraButtons.setGeometry(QRect(0, 240, 501, 51))
        self.fraButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.fraButtons.setFrameShadow(QFrame.Shadow.Raised)


        self.horizontalLayout = QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btnS = QPushButton(self.fraButtons)
        self.btnS.setObjectName("btnS")
        self.btnS.setBaseSize(80, 0)
        self.horizontalLayout.addWidget(self.btnS)

        self.btnR = QPushButton(self.fraButtons)
        self.btnR.setObjectName("btnR")
        self.btnR.setBaseSize(80, 0)
        self.horizontalLayout.addWidget(self.btnR)

        self.btnQ = QPushButton(self.fraButtons)
        self.btnQ.setObjectName("btnQ")
        self.btnQ.setBaseSize(80, 0)
        self.horizontalLayout.addWidget(self.btnQ)

        root.setCentralWidget(self.centralwidget)


        self.menubar = QMenuBar(root)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 984, 33))
        root.setMenuBar(self.menubar)


        self.statusbar = QStatusBar(root)
        self.statusbar.setObjectName("statusbar")
        root.setStatusBar(self.statusbar)

        self.retranslateUi(root)
        QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        root.setWindowTitle(QCoreApplication.translate("root", "Form", None))
        self.lblFrPerson.setTitle(QCoreApplication.translate("root", "Personal Information", None))
        self.lblFirst.setText(QCoreApplication.translate("root", "*First Name:", None))
        self.lblLast.setText(QCoreApplication.translate("root", "*Last Name:", None))
        self.lblEmail.setText(QCoreApplication.translate("root", "Email:", None))
        self.lblPhone.setText(QCoreApplication.translate("root", "Phone:", None))
        self.btnS.setText(QCoreApplication.translate("root", "Submit", None))
        self.btnR.setText(QCoreApplication.translate("root", "Reset", None))
        self.btnQ.setText(QCoreApplication.translate("root", "Quit", None))



class Ui(object):
    class root(Ui_root):
        pass
