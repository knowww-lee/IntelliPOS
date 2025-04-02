# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pos.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_POSWindow(object):
    def setupUi(self, POSWindow):
        if not POSWindow.objectName():
            POSWindow.setObjectName(u"POSWindow")
        POSWindow.resize(1584, 997)
        self.centralwidget = QWidget(POSWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:white;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color:black;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_7 = QWidget(self.widget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color:black;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:30px;\n"
"color:white;")

        self.verticalLayout_3.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color:black;\n"
"color:white;")
        self.gridLayout_2 = QGridLayout(self.widget_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_10 = QLabel(self.widget_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_10, 0, 1, 1, 1)

        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.label_21 = QLabel(self.widget_8)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_21, 0, 3, 1, 1)

        self.label_22 = QLabel(self.widget_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"margin-left:20px;")

        self.gridLayout_2.addWidget(self.label_22, 0, 4, 1, 1)

        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_23, 0, 5, 1, 1)

        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_24 = QLabel(self.widget_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_24, 5, 3, 1, 1)

        self.label_26 = QLabel(self.widget_8)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_26, 5, 5, 1, 1)

        self.label_14 = QLabel(self.widget_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"margin-left:20px;")

        self.gridLayout_2.addWidget(self.label_14, 5, 2, 1, 1)

        self.label_25 = QLabel(self.widget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"margin-left:20px;")

        self.gridLayout_2.addWidget(self.label_25, 5, 4, 1, 1)

        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font-weight:bold;")

        self.gridLayout_2.addWidget(self.label_12, 5, 1, 1, 1)

        self.label_13 = QLabel(self.widget_8)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"margin-left:20px;")

        self.gridLayout_2.addWidget(self.label_13, 0, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color:black;\n"
"color:white;")
        self.verticalLayout_4 = QVBoxLayout(self.widget_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.widget_9)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_8.setFont(font)

        self.verticalLayout_4.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color:gray;")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color:white;")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget = QTableWidget(self.widget_4)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMouseTracking(False)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet(u"color:black;")
        self.tableWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Raised)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(28)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.tableWidget)

        self.widget_10 = QWidget(self.widget_4)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_3 = QGridLayout(self.widget_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.widget_10)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:black;")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.label_16 = QLabel(self.widget_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20px;")

        self.gridLayout_3.addWidget(self.label_16, 1, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_18 = QLabel(self.widget_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20px;")

        self.gridLayout_3.addWidget(self.label_18, 2, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_15 = QLabel(self.widget_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20px;")

        self.gridLayout_3.addWidget(self.label_15, 0, 1, 1, 1, Qt.AlignmentFlag.AlignRight)

        self.label_17 = QLabel(self.widget_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"color:black;")

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:black;")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_20 = QLabel(self.widget_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"color:black;")

        self.horizontalLayout_4.addWidget(self.label_20)

        self.label_19 = QLabel(self.widget_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20px;")

        self.horizontalLayout_4.addWidget(self.label_19)


        self.verticalLayout_5.addWidget(self.widget_11)


        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color:white;")
        self.gridLayout = QGridLayout(self.widget_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_19 = QPushButton(self.widget_5)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"padding:20px;\n"
"color:white;\n"
"background-color:#175793;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_19, 0, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.widget_5)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#ADBC3C;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_28, 1, 4, 1, 1)

        self.pushButton_34 = QPushButton(self.widget_5)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_34, 3, 4, 1, 1)

        self.pushButton_31 = QPushButton(self.widget_5)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_31, 5, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"padding:20px;\n"
"color:white;\n"
"background-color:#175793;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_37 = QPushButton(self.widget_5)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_37, 5, 4, 1, 1)

        self.pushButton_27 = QPushButton(self.widget_5)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setStyleSheet(u"padding:20px;\n"
"color:white;\n"
"background-color:#175793;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_27, 0, 4, 1, 1)

        self.pushButton_10 = QPushButton(self.widget_5)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_10, 3, 1, 1, 1)

        self.pushButton_35 = QPushButton(self.widget_5)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_35, 4, 4, 1, 1)

        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20px;")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_2 = QPushButton(self.widget_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#59B17E;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.widget_5)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_17, 3, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.widget_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#BA5F5F;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_7, 1, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.widget_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#F09E55;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_8, 1, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"padding:20px;\n"
"color:white;\n"
"background-color:#175793;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_5, 2, 4, 1, 1)

        self.pushButton_29 = QPushButton(self.widget_5)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_29, 5, 0, 1, 1)

        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#0097B2;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_36 = QPushButton(self.widget_5)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_36, 5, 3, 1, 1)

        self.pushButton_30 = QPushButton(self.widget_5)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_30, 4, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.widget_5)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_18, 4, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)

        self.pushButton_32 = QPushButton(self.widget_5)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_32, 5, 2, 1, 1)

        self.pushButton_33 = QPushButton(self.widget_5)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_33, 4, 3, 1, 1)

        self.pushButton_6 = QPushButton(self.widget_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;\n"
"font-weight:bold;")

        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 1)

        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20px;")

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_9 = QPushButton(self.widget_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"padding:70px;\n"
"color:white;\n"
"background-color:#1A8DC7;\n"
"border-radius:20px;")

        self.gridLayout.addWidget(self.pushButton_9, 3, 3, 1, 1)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"background-color:white;")
        self.verticalLayout_2 = QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:30px;")

        self.verticalLayout_2.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color:black;\n"
"font-weight:bold;\n"
"font-size:20px;")

        self.verticalLayout_2.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_15 = QPushButton(self.widget_6)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.verticalLayout_2.addWidget(self.pushButton_15)

        self.pushButton_11 = QPushButton(self.widget_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.verticalLayout_2.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.widget_6)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.verticalLayout_2.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.widget_6)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.verticalLayout_2.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.widget_6)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.verticalLayout_2.addWidget(self.pushButton_14)

        self.pushButton_16 = QPushButton(self.widget_6)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#A20E00;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.verticalLayout_2.addWidget(self.pushButton_16)


        self.horizontalLayout.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color:white;")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_20 = QPushButton(self.widget_3)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.horizontalLayout_3.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.widget_3)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.horizontalLayout_3.addWidget(self.pushButton_21)

        self.pushButton_22 = QPushButton(self.widget_3)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.horizontalLayout_3.addWidget(self.pushButton_22)

        self.pushButton_23 = QPushButton(self.widget_3)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.horizontalLayout_3.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.widget_3)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.horizontalLayout_3.addWidget(self.pushButton_24)

        self.pushButton_25 = QPushButton(self.widget_3)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.horizontalLayout_3.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.widget_3)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setStyleSheet(u"padding:40px;\n"
"color:white;\n"
"background-color:#414141;\n"
"border-radius:20px;\n"
"font-size:18px;\n"
"font-weight:bold;")

        self.horizontalLayout_3.addWidget(self.pushButton_26)


        self.verticalLayout.addWidget(self.widget_3)

        POSWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(POSWindow)

        QMetaObject.connectSlotsByName(POSWindow)
    # setupUi

    def retranslateUi(self, POSWindow):
        POSWindow.setWindowTitle(QCoreApplication.translate("POSWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("POSWindow", u"IntelliPOS", None))
        self.label_10.setText(QCoreApplication.translate("POSWindow", u"Noli", None))
        self.label_9.setText(QCoreApplication.translate("POSWindow", u"Cashier:", None))
        self.label_21.setText(QCoreApplication.translate("POSWindow", u"12455679", None))
        self.label_22.setText(QCoreApplication.translate("POSWindow", u"Time:", None))
        self.label_23.setText(QCoreApplication.translate("POSWindow", u"11:00 PM", None))
        self.label_11.setText(QCoreApplication.translate("POSWindow", u"Store:", None))
        self.label_24.setText(QCoreApplication.translate("POSWindow", u"Gwen", None))
        self.label_26.setText(QCoreApplication.translate("POSWindow", u"March 29, 2025", None))
        self.label_14.setText(QCoreApplication.translate("POSWindow", u"Customer:", None))
        self.label_25.setText(QCoreApplication.translate("POSWindow", u"Date:", None))
        self.label_12.setText(QCoreApplication.translate("POSWindow", u"Sweet Avenue", None))
        self.label_13.setText(QCoreApplication.translate("POSWindow", u"Transaction No:", None))
        self.label_8.setText(QCoreApplication.translate("POSWindow", u"Settings", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("POSWindow", u"Item", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("POSWindow", u"Qty", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("POSWindow", u"Amt", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("POSWindow", u"Total", None));
        self.label.setText(QCoreApplication.translate("POSWindow", u"Discount", None))
        self.label_16.setText(QCoreApplication.translate("POSWindow", u"0.00", None))
        self.label_18.setText(QCoreApplication.translate("POSWindow", u"299.00", None))
        self.label_15.setText(QCoreApplication.translate("POSWindow", u"299.00", None))
        self.label_17.setText(QCoreApplication.translate("POSWindow", u"Subtotal", None))
        self.label_2.setText(QCoreApplication.translate("POSWindow", u"Total", None))
        self.label_20.setText(QCoreApplication.translate("POSWindow", u"Recommendation", None))
        self.label_19.setText(QCoreApplication.translate("POSWindow", u"Dark Chocolate", None))
        self.pushButton_19.setText(QCoreApplication.translate("POSWindow", u"Previous", None))
        self.pushButton_28.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_34.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_31.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("POSWindow", u"Previous", None))
        self.pushButton_37.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_27.setText(QCoreApplication.translate("POSWindow", u"Next", None))
        self.pushButton_10.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_35.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("POSWindow", u"Categories", None))
        self.pushButton_2.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_17.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("POSWindow", u"Next", None))
        self.pushButton_29.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_36.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_30.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_18.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_32.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_33.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("POSWindow", u"Dark Chocolate", None))
        self.label_4.setText(QCoreApplication.translate("POSWindow", u"Products", None))
        self.pushButton_9.setText(QCoreApplication.translate("POSWindow", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("POSWindow", u"299.00", None))
        self.label_6.setText(QCoreApplication.translate("POSWindow", u"Subtotal", None))
        self.pushButton_15.setText(QCoreApplication.translate("POSWindow", u"SUSPEND", None))
        self.pushButton_11.setText(QCoreApplication.translate("POSWindow", u"REFUND", None))
        self.pushButton_12.setText(QCoreApplication.translate("POSWindow", u"VOID", None))
        self.pushButton_13.setText(QCoreApplication.translate("POSWindow", u"PRINT", None))
        self.pushButton_14.setText(QCoreApplication.translate("POSWindow", u"MANAGE", None))
        self.pushButton_16.setText(QCoreApplication.translate("POSWindow", u"SETTLE", None))
        self.pushButton_20.setText(QCoreApplication.translate("POSWindow", u"VIEW RECEIPT", None))
        self.pushButton_21.setText(QCoreApplication.translate("POSWindow", u"CUSTOMER", None))
        self.pushButton_22.setText(QCoreApplication.translate("POSWindow", u"DISCOUNT", None))
        self.pushButton_23.setText(QCoreApplication.translate("POSWindow", u"VOIDED", None))
        self.pushButton_24.setText(QCoreApplication.translate("POSWindow", u"REFUNDED", None))
        self.pushButton_25.setText(QCoreApplication.translate("POSWindow", u"SUSPENDED", None))
        self.pushButton_26.setText(QCoreApplication.translate("POSWindow", u"SIGN OUT", None))
    # retranslateUi

