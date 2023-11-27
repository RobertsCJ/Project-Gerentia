# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
from telas.icons_login_rc import *

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(448, 620)
        Form.setMinimumSize(QSize(420, 620))
        Form.setMaximumSize(QSize(854, 620))
        Form.setStyleSheet(u"QWidget{\n"
"background-color: #dcdcdc;\n"
"}\n"
"QFrame{\n"
"background-color: #e6e6fa;\n"
"border-radius: 55px;\n"
"}\n"
"QLineEdit{\n"
"background-color: #ffffff;\n"
"border-radius: 15px;\n"
"color: black;\n"
"}\n"
"QPushButton{\n"
"background-color: #ffffff;\n"
"border-radius: 15px;\n"
"color: black;\n"
"font: 700;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #120a8f;\n"
"color: #ffffff;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #111111;\n"
"color: #ffffff;\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_principal = QFrame(Form)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setMinimumSize(QSize(400, 600))
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_principal)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.icon_login = QLabel(self.frame_principal)
        self.icon_login.setObjectName(u"icon_login")
        self.icon_login.setMinimumSize(QSize(100, 100))
        self.icon_login.setMaximumSize(QSize(100, 100))
        self.icon_login.setPixmap(QPixmap(u":/icons_login/icons_login/icon_login.ico"))
        self.icon_login.setScaledContents(True)
        self.icon_login.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.icon_login)

        self.label_4 = QLabel(self.frame_principal)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.layout_camposLogin = QGridLayout()
        self.layout_camposLogin.setObjectName(u"layout_camposLogin")
        self.label_3 = QLabel(self.frame_principal)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Display"])
        self.label_3.setFont(font)

        self.layout_camposLogin.addWidget(self.label_3, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.icon_user = QLabel(self.frame_principal)
        self.icon_user.setObjectName(u"icon_user")
        self.icon_user.setMinimumSize(QSize(30, 30))
        self.icon_user.setMaximumSize(QSize(30, 30))
        self.icon_user.setPixmap(QPixmap(u":/icons_login/icons_login/icon_user.ico"))
        self.icon_user.setScaledContents(True)
        self.icon_user.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.icon_user)

        self.txt_nomeUser = QLineEdit(self.frame_principal)
        self.txt_nomeUser.setObjectName(u"txt_nomeUser")
        self.txt_nomeUser.setMinimumSize(QSize(250, 30))
        self.txt_nomeUser.setMaximumSize(QSize(250, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Variable Display"])
        font1.setPointSize(11)
        self.txt_nomeUser.setFont(font1)
        self.txt_nomeUser.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.txt_nomeUser)


        self.layout_camposLogin.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon_cadeado = QLabel(self.frame_principal)
        self.icon_cadeado.setObjectName(u"icon_cadeado")
        self.icon_cadeado.setMinimumSize(QSize(30, 30))
        self.icon_cadeado.setMaximumSize(QSize(30, 30))
        self.icon_cadeado.setPixmap(QPixmap(u":/icons_login/icons_login/icon_cadeado.ico"))
        self.icon_cadeado.setScaledContents(True)
        self.icon_cadeado.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.icon_cadeado)

        self.txt_senhaUser = QLineEdit(self.frame_principal)
        self.txt_senhaUser.setObjectName(u"txt_senhaUser")
        self.txt_senhaUser.setMinimumSize(QSize(250, 30))
        self.txt_senhaUser.setMaximumSize(QSize(250, 30))
        self.txt_senhaUser.setFont(font1)
        self.txt_senhaUser.setEchoMode(QLineEdit.Password)
        self.txt_senhaUser.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_senhaUser)


        self.layout_camposLogin.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame_principal)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.layout_camposLogin.addWidget(self.label_2, 2, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.layout_camposLogin)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_login = QPushButton(self.frame_principal)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(160, 30))
        self.btn_login.setMaximumSize(QSize(160, 30))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Variable Display"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_login.setFont(font2)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setLayoutDirection(Qt.RightToLeft)
        self.btn_login.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons_login/icons_login/login_btn.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_login.setIcon(icon)
        self.btn_login.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_login, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addWidget(self.frame_principal)

        QWidget.setTabOrder(self.txt_nomeUser, self.txt_senhaUser)
        QWidget.setTabOrder(self.txt_senhaUser, self.btn_login)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.icon_login.setText("")
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Usu\u00e1rio</span></p></body></html>", None))
        self.icon_user.setText("")
        self.txt_nomeUser.setPlaceholderText(QCoreApplication.translate("Form", u"Nome do usu\u00e1rio", None))
        self.icon_cadeado.setText("")
        self.txt_senhaUser.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Senha</span></p></body></html>", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"LOGIN", None))
    # retranslateUi

