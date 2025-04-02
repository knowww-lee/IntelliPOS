# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(1346, 893)
        self.logincentralwidget = QWidget(LoginWindow)
        self.logincentralwidget.setObjectName(u"logincentralwidget")
        self.gridLayout = QGridLayout(self.logincentralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.logincentralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:white;")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo = QLabel(self.widget)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"")
        self.logo.setPixmap(QPixmap(os.path.abspath("assets/Logo3.png")))

        self.verticalLayout.addWidget(self.logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.IntelliPOSTitle = QLabel(self.widget)
        self.IntelliPOSTitle.setObjectName(u"IntelliPOSTitle")
        self.IntelliPOSTitle.setStyleSheet(u"font-weight:bold;\n"
"font-size:40px;\n"
"color:black;\n"
"margin-bottom:20px;")

        self.verticalLayout.addWidget(self.IntelliPOSTitle, 0, Qt.AlignmentFlag.AlignHCenter)

        self.taglineText = QLabel(self.widget)
        self.taglineText.setObjectName(u"taglineText")
        self.taglineText.setStyleSheet(u"color:black;\n"
"font-size:18px;")

        self.verticalLayout.addWidget(self.taglineText, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.logincentralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color:#0097B2;")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 291, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.loginText = QLabel(self.widget_2)
        self.loginText.setObjectName(u"loginText")
        self.loginText.setStyleSheet(u"font-weight:bold;\n"
"color:white;\n"
"font-size:40px;")

        self.verticalLayout_2.addWidget(self.loginText, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.usernameText = QLabel(self.widget_2)
        self.usernameText.setObjectName(u"usernameText")
        self.usernameText.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"margin-right:180px;")

        self.verticalLayout_2.addWidget(self.usernameText, 0, Qt.AlignmentFlag.AlignHCenter)

        self.usernameField = QLineEdit(self.widget_2)
        self.usernameField.setObjectName(u"usernameField")
        self.usernameField.setStyleSheet(u"padding-left:90px;\n"
"padding-right:90px;\n"
"padding-top:20px;\n"
"padding-bottom:20px;\n"
"background-color:white;\n"
"margin-left:120px;\n"
"margin-right:120px;\n"
"color:black;\n"
" border: 2px solid black;\n"
" border-radius: 20px;")

        self.verticalLayout_2.addWidget(self.usernameField, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.paswordText = QLabel(self.widget_2)
        self.paswordText.setObjectName(u"paswordText")
        self.paswordText.setStyleSheet(u"color:white;\n"
"font-size:20px;\n"
"margin-right:180px;")

        self.verticalLayout_2.addWidget(self.paswordText, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.passwordField = QLineEdit(self.widget_2)
        self.passwordField.setObjectName(u"passwordField")
        self.passwordField.setStyleSheet(u"padding-left:90px;\n"
"padding-right:90px;\n"
"padding-top:20px;\n"
"padding-bottom:20px;\n"
"background-color:white;\n"
"margin-left:120px;\n"
"margin-right:120px;\n"
"color:black;\n"
" border: 2px solid black;\n"
" border-radius: 20px;")
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.passwordField, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.errordisplayLabel = QLabel(self.widget_2)
        self.errordisplayLabel.setObjectName(u"errordisplayLabel")
        self.errordisplayLabel.setStyleSheet(u"color:red;")

        self.verticalLayout_2.addWidget(self.errordisplayLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_10)

        self.loginButton = QPushButton(self.widget_2)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setStyleSheet(u"padding: 20px, 30px, 20px, 30px;\n"
"margin-left:100px;\n"
"margin-right:100px;\n"
"font-size:20px;\n"
"background-color:black;\n"
" border: 2px solid black;\n"
" border-radius: 30px;")

        self.verticalLayout_2.addWidget(self.loginButton)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

        self.forgotpasswordText = QLabel(self.widget_2)
        self.forgotpasswordText.setObjectName(u"forgotpasswordText")
        self.forgotpasswordText.setStyleSheet(u"color:white;")

        self.verticalLayout_2.addWidget(self.forgotpasswordText, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 290, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        LoginWindow.setCentralWidget(self.logincentralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.logo.setText("")
        self.IntelliPOSTitle.setText(QCoreApplication.translate("LoginWindow", u"IntelliPOS", None))
        self.taglineText.setText(QCoreApplication.translate("LoginWindow", u"Smart Solutions for Seamless Transactions", None))
        self.loginText.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.usernameText.setText(QCoreApplication.translate("LoginWindow", u"Username", None))
        self.usernameField.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter Username", None))
        self.paswordText.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.passwordField.setText("")
        self.passwordField.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Enter Password", None))
        self.errordisplayLabel.setText("")
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.forgotpasswordText.setText(QCoreApplication.translate("LoginWindow", u"Forgot Password?", None))
    # retranslateUi

