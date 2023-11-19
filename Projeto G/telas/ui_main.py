# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
from telas.icons_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 588)
        MainWindow.setStyleSheet(u"background-color: #212121;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border:none;\n"
"}\n"
"QLabel{\n"
"color: white;\n"
"font: \"Segoe UI Variable Regular\";\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_lateral = QFrame(self.centralwidget)
        self.frame_menu_lateral.setObjectName(u"frame_menu_lateral")
        self.frame_menu_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_menu_lateral.setStyleSheet(u"background-color: #434343;")
        self.frame_menu_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu_lateral)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_menu_lateral)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbl_usuario = QLabel(self.frame)
        self.lbl_usuario.setObjectName(u"lbl_usuario")

        self.horizontalLayout_4.addWidget(self.lbl_usuario)

        self.lbl_status = QLabel(self.frame)
        self.lbl_status.setObjectName(u"lbl_status")

        self.horizontalLayout_4.addWidget(self.lbl_status)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_menu_lateral)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color:rgb(65, 65, 65);\n"
"}\n"
"QToolBox{\n"
"text-align:left;\n"
"background-color:rgb(228, 254, 255);\n"
"}\n"
"QToolBox::tab{\n"
"border-radius:5px;\n"
"background-color:rgb(194, 232, 255);\n"
"text-align:left;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setCursor(QCursor(Qt.ArrowCursor))
        self.toolBox.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: #434343;\n"
"padding-left: 5px;\n"
"text-align: left;\n"
"border-radius: 5px;\n"
"font-weight: bold;\n"
"font-size:9pt;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: #646464;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: #212121;\n"
"color: white;\n"
"background-color: #434343;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"background-color: gray;\n"
"color: white;\n"
"font-family: Segoe UI Variable Display Bold;\n"
"font-weight: 900;\n"
"padding-left: 1px;\n"
"text-align: center;\n"
"border-radius: 0px;\n"
"font-size: 11pt;\n"
"}\n"
"QToolBox::tab:hover{\n"
"background-color: white;\n"
"color: black;\n"
"}\n"
"QToolBox::tab:pressed{\n"
"background-color: #212121;\n"
"color: white;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 131, 448))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        self.btn_home.setMaximumSize(QSize(16777215, 30))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/icons-home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_estoque = QPushButton(self.page)
        self.btn_estoque.setObjectName(u"btn_estoque")
        self.btn_estoque.setMinimumSize(QSize(0, 30))
        self.btn_estoque.setMaximumSize(QSize(16777215, 30))
        self.btn_estoque.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/icon_estoque.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_estoque.setIcon(icon1)
        self.btn_estoque.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_estoque)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 30))
        self.btn_contatos.setMaximumSize(QSize(16777215, 30))
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/icon_contatos.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_contatos.setIcon(icon2)
        self.btn_contatos.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_contatos)

        self.btn_configuracoes = QPushButton(self.page)
        self.btn_configuracoes.setObjectName(u"btn_configuracoes")
        self.btn_configuracoes.setMinimumSize(QSize(0, 30))
        self.btn_configuracoes.setMaximumSize(QSize(16777215, 30))
        self.btn_configuracoes.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/icon-configura\u00e7\u00f5es.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_configuracoes.setIcon(icon3)
        self.btn_configuracoes.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_configuracoes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"MENU")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 141, 448))
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.btn_sobre = QPushButton(self.page_2)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setMaximumSize(QSize(16777215, 30))
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/icons-informa\u00e7\u00f5es.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sobre.setIcon(icon4)
        self.btn_sobre.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.btn_sobre)

        self.toolBox.addItem(self.page_2, u"INFORMA\u00c7\u00d5ES")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame_menu_lateral)

        self.frame_principal_conteudo = QFrame(self.centralwidget)
        self.frame_principal_conteudo.setObjectName(u"frame_principal_conteudo")
        self.frame_principal_conteudo.setFrameShape(QFrame.StyledPanel)
        self.frame_principal_conteudo.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_principal_conteudo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 0, 6, 0)
        self.frame_cabecalho = QFrame(self.frame_principal_conteudo)
        self.frame_cabecalho.setObjectName(u"frame_cabecalho")
        self.frame_cabecalho.setStyleSheet(u"QPushButton:hover{background-color: #646464;}\n"
"QPushButton:pressed{background-color: #212121;}\n"
"QPushButton{border-radius: 7px;}")
        self.frame_cabecalho.setFrameShape(QFrame.StyledPanel)
        self.frame_cabecalho.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_cabecalho)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 6, -1, 0)
        self.btn_menu = QPushButton(self.frame_cabecalho)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/icon_menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon5)
        self.btn_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_menu, 0, Qt.AlignLeft)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)

        self.label = QLabel(self.frame_cabecalho)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addWidget(self.frame_cabecalho)

        self.frame_conteudo = QFrame(self.frame_principal_conteudo)
        self.frame_conteudo.setObjectName(u"frame_conteudo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_conteudo.sizePolicy().hasHeightForWidth())
        self.frame_conteudo.setSizePolicy(sizePolicy)
        self.frame_conteudo.setStyleSheet(u"background-color: #434343;")
        self.frame_conteudo.setFrameShape(QFrame.StyledPanel)
        self.frame_conteudo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_conteudo)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.paginas = QStackedWidget(self.frame_conteudo)
        self.paginas.setObjectName(u"paginas")
        self.paginas.setMinimumSize(QSize(700, 540))
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_8 = QVBoxLayout(self.pg_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_8.addWidget(self.logo)

        self.paginas.addWidget(self.pg_home)
        self.pg_estoque = QWidget()
        self.pg_estoque.setObjectName(u"pg_estoque")
        self.verticalLayout_9 = QVBoxLayout(self.pg_estoque)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(self.pg_estoque)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_13 = QVBoxLayout(self.tab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_4 = QFrame(self.tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"background-color: white;\n"
"border-radius: 5px;\n"
"color: black;\n"
"font: bold;\n"
"font: 10pt \"Segoe UI Variable Display Regular \";\n"
"}\n"
"\n"
"QFrame{background-color:#e7e7e7;\n"
"color: #006395;}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.txt_pCompra = QLineEdit(self.frame_4)
        self.txt_pCompra.setObjectName(u"txt_pCompra")
        self.txt_pCompra.setMinimumSize(QSize(0, 25))
        self.txt_pCompra.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.txt_pCompra)


        self.gridLayout.addLayout(self.horizontalLayout_10, 3, 0, 1, 2)

        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(0, 25))
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.txt_pVenda = QLineEdit(self.frame_4)
        self.txt_pVenda.setObjectName(u"txt_pVenda")
        self.txt_pVenda.setMinimumSize(QSize(0, 25))
        self.txt_pVenda.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.txt_pVenda)


        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.txt_quantidade = QLineEdit(self.frame_4)
        self.txt_quantidade.setObjectName(u"txt_quantidade")
        self.txt_quantidade.setMinimumSize(QSize(0, 25))
        self.txt_quantidade.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.txt_quantidade)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 2, 1, 1)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)

        self.txt_descricao = QLineEdit(self.frame_4)
        self.txt_descricao.setObjectName(u"txt_descricao")
        self.txt_descricao.setMinimumSize(QSize(0, 25))
        self.txt_descricao.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_descricao, 2, 1, 1, 2)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: white;")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 3)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.btn_cadastrar = QPushButton(self.tab)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(150, 30))
        self.btn_cadastrar.setMaximumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(12)
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{background-color: white;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{background-color: #00aaff;\n"
"color: white;}\n"
"QPushButton:pressed{background-color: white;\n"
"color: black;}")

        self.verticalLayout_13.addWidget(self.btn_cadastrar, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color:#e7e7e7;\n"
"}\n"
"QLineEdit{\n"
"background-color: white;\n"
"font: 10pt;\n"
"color: balck;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton{background-color: white;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton:hover{background-color: #00aaff;\n"
"color: white;}\n"
"QPushButton:pressed{background-color: white;\n"
"color: black;}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 9)
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color: white;\n"
"color: #006395;")

        self.verticalLayout_12.addWidget(self.label_12)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_pesquisa = QLineEdit(self.frame_5)
        self.txt_pesquisa.setObjectName(u"txt_pesquisa")
        self.txt_pesquisa.setMinimumSize(QSize(0, 30))
        self.txt_pesquisa.setMaximumSize(QSize(16777215, 30))
        self.txt_pesquisa.setSizeIncrement(QSize(0, 0))
        self.txt_pesquisa.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.txt_pesquisa)

        self.btn_pesquisar = QPushButton(self.frame_5)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar.setMaximumSize(QSize(100, 30))
        self.btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icon_pesquisa.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.btn_pesquisar)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.tb_pesquisa = QTableWidget(self.frame_5)
        if (self.tb_pesquisa.columnCount() < 8):
            self.tb_pesquisa.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_pesquisa.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tb_pesquisa.setObjectName(u"tb_pesquisa")
        self.tb_pesquisa.setStyleSheet(u"QHeaderView::section{\n"
"background-color: rgb(148, 148, 148);\n"
"color: white;\n"
"font: 10pt \"Segoe UI Variable Display Regular\";\n"
"}\n"
"QTableWidget{\n"
"background-color: white;\n"
"}")

        self.verticalLayout_12.addWidget(self.tb_pesquisa)


        self.verticalLayout_13.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background-color: white;\n"
"color: #006395;")

        self.verticalLayout_11.addWidget(self.label_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_3 = QFrame(self.tab_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{background-color: #e7e7e7;}\n"
"QPushButton{\n"
"background-color: white;\n"
"border-radius: 15px;\n"
"color: black;\n"
"font: 500 11pt \"Segoe UI Variable Display Reguler\";\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_relatorio = QPushButton(self.frame_3)
        self.btn_relatorio.setObjectName(u"btn_relatorio")
        self.btn_relatorio.setMinimumSize(QSize(120, 30))
        self.btn_relatorio.setMaximumSize(QSize(120, 30))
        self.btn_relatorio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_relatorio.setStyleSheet(u"QPushButton:hover{\n"
"color: white;\n"
"background-color: rgb(49, 147, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background-color: white;\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_relatorio)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 30))
        self.btn_alterar.setMaximumSize(QSize(120, 30))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"color: white;\n"
"background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background-color: white;\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 30))
        self.btn_excluir.setMaximumSize(QSize(120, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{\n"
"color: white;\n"
"background-color: red;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background-color: white;\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_excluir)

        self.btn_sincronizar = QPushButton(self.frame_3)
        self.btn_sincronizar.setObjectName(u"btn_sincronizar")
        self.btn_sincronizar.setMinimumSize(QSize(120, 30))
        self.btn_sincronizar.setMaximumSize(QSize(120, 30))
        self.btn_sincronizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sincronizar.setStyleSheet(u"QPushButton:hover{\n"
"color: white;\n"
"background-color: #00aaff;\n"
"}\n"
"QPushButton:pressed{\n"
"color: black;\n"
"background-color: white;\n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_sincronizar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.tb_estoque = QTableWidget(self.tab_2)
        if (self.tb_estoque.columnCount() < 8):
            self.tb_estoque.setColumnCount(8)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_estoque.setHorizontalHeaderItem(7, __qtablewidgetitem15)
        self.tb_estoque.setObjectName(u"tb_estoque")
        self.tb_estoque.setStyleSheet(u"QHeaderView::section{\n"
"background-color: rgb(148, 148, 148);\n"
"color: white;\n"
"font: 10pt \"Segoe UI Variable Display Regular\";\n"
"}\n"
"QTableWidget{\n"
"background-color: white;\n"
"}")

        self.verticalLayout_10.addWidget(self.tb_estoque)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.paginas.addWidget(self.pg_estoque)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_15 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.layout_label_contatos = QVBoxLayout()
        self.layout_label_contatos.setObjectName(u"layout_label_contatos")
        self.label_13 = QLabel(self.pg_contatos)
        self.label_13.setObjectName(u"label_13")

        self.layout_label_contatos.addWidget(self.label_13)

        self.label_14 = QLabel(self.pg_contatos)
        self.label_14.setObjectName(u"label_14")

        self.layout_label_contatos.addWidget(self.label_14)


        self.verticalLayout_15.addLayout(self.layout_label_contatos)

        self.layout_sobre = QHBoxLayout()
        self.layout_sobre.setObjectName(u"layout_sobre")
        self.layout_jonatas = QVBoxLayout()
        self.layout_jonatas.setObjectName(u"layout_jonatas")
        self.label_15 = QLabel(self.pg_contatos)
        self.label_15.setObjectName(u"label_15")

        self.layout_jonatas.addWidget(self.label_15)

        self.label_27 = QLabel(self.pg_contatos)
        self.label_27.setObjectName(u"label_27")

        self.layout_jonatas.addWidget(self.label_27)

        self.label_26 = QLabel(self.pg_contatos)
        self.label_26.setObjectName(u"label_26")

        self.layout_jonatas.addWidget(self.label_26)

        self.label_25 = QLabel(self.pg_contatos)
        self.label_25.setObjectName(u"label_25")

        self.layout_jonatas.addWidget(self.label_25)


        self.layout_sobre.addLayout(self.layout_jonatas)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_sobre.addItem(self.horizontalSpacer_2)

        self.layout_roberto = QVBoxLayout()
        self.layout_roberto.setObjectName(u"layout_roberto")
        self.label_16 = QLabel(self.pg_contatos)
        self.label_16.setObjectName(u"label_16")

        self.layout_roberto.addWidget(self.label_16)

        self.label_24 = QLabel(self.pg_contatos)
        self.label_24.setObjectName(u"label_24")

        self.layout_roberto.addWidget(self.label_24)

        self.label_23 = QLabel(self.pg_contatos)
        self.label_23.setObjectName(u"label_23")

        self.layout_roberto.addWidget(self.label_23)

        self.label_22 = QLabel(self.pg_contatos)
        self.label_22.setObjectName(u"label_22")

        self.layout_roberto.addWidget(self.label_22)


        self.layout_sobre.addLayout(self.layout_roberto)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_sobre.addItem(self.horizontalSpacer_3)

        self.layout_wallyson = QVBoxLayout()
        self.layout_wallyson.setObjectName(u"layout_wallyson")
        self.label_17 = QLabel(self.pg_contatos)
        self.label_17.setObjectName(u"label_17")

        self.layout_wallyson.addWidget(self.label_17)

        self.label_19 = QLabel(self.pg_contatos)
        self.label_19.setObjectName(u"label_19")

        self.layout_wallyson.addWidget(self.label_19)

        self.label_20 = QLabel(self.pg_contatos)
        self.label_20.setObjectName(u"label_20")

        self.layout_wallyson.addWidget(self.label_20)

        self.label_21 = QLabel(self.pg_contatos)
        self.label_21.setObjectName(u"label_21")

        self.layout_wallyson.addWidget(self.label_21)


        self.layout_sobre.addLayout(self.layout_wallyson)


        self.verticalLayout_15.addLayout(self.layout_sobre)

        self.label_18 = QLabel(self.pg_contatos)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background-color: #434343;")
        self.label_18.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_18)

        self.paginas.addWidget(self.pg_contatos)
        self.pg_configuracoes = QWidget()
        self.pg_configuracoes.setObjectName(u"pg_configuracoes")
        self.verticalLayout_17 = QVBoxLayout(self.pg_configuracoes)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_32 = QLabel(self.pg_configuracoes)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_16.addWidget(self.label_32)

        self.label_41 = QLabel(self.pg_configuracoes)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_16.addWidget(self.label_41)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame_config = QFrame(self.pg_configuracoes)
        self.frame_config.setObjectName(u"frame_config")
        self.frame_config.setStyleSheet(u"QLineEdit{background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton{background-color: white;\n"
"border-radius: 15px;\n"
"font: 700;\n"
"}\n"
"QPushButton:hover{background-color: red;\n"
"color: white;\n"
"}\n"
"QPushButton:pressed{background-color: black;\n"
"color: white;\n"
"}")
        self.frame_config.setFrameShape(QFrame.StyledPanel)
        self.frame_config.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_config)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_38 = QLabel(self.frame_config)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_19.addWidget(self.label_38)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_39 = QLabel(self.frame_config)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_3.addWidget(self.label_39, 0, 0, 1, 1)

        self.txt_matricula = QLineEdit(self.frame_config)
        self.txt_matricula.setObjectName(u"txt_matricula")
        self.txt_matricula.setMinimumSize(QSize(0, 25))
        self.txt_matricula.setMaximumSize(QSize(16777215, 25))
        self.txt_matricula.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_matricula, 1, 0, 1, 1)

        self.label_40 = QLabel(self.frame_config)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_3.addWidget(self.label_40, 2, 0, 1, 1)

        self.txt_nomeFunci = QLineEdit(self.frame_config)
        self.txt_nomeFunci.setObjectName(u"txt_nomeFunci")
        self.txt_nomeFunci.setMinimumSize(QSize(0, 25))
        self.txt_nomeFunci.setMaximumSize(QSize(16777215, 25))
        self.txt_nomeFunci.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.txt_nomeFunci, 3, 0, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_3)

        self.btn_removerFunci = QPushButton(self.frame_config)
        self.btn_removerFunci.setObjectName(u"btn_removerFunci")
        self.btn_removerFunci.setMinimumSize(QSize(100, 30))
        self.btn_removerFunci.setMaximumSize(QSize(100, 30))

        self.verticalLayout_19.addWidget(self.btn_removerFunci, 0, Qt.AlignHCenter)


        self.horizontalLayout_13.addLayout(self.verticalLayout_19)


        self.horizontalLayout_12.addWidget(self.frame_config)

        self.frame_usuarios = QFrame(self.pg_configuracoes)
        self.frame_usuarios.setObjectName(u"frame_usuarios")
        self.frame_usuarios.setStyleSheet(u"QLineEdit{background-color: white;\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton{background-color: white;\n"
"border-radius: 15px;\n"
"font: 700;\n"
"}\n"
"QPushButton:hover{background-color: #479bd8;}\n"
"QPushButton:pressed{background-color: blue;\n"
"color: white;\n"
"}")
        self.frame_usuarios.setFrameShape(QFrame.StyledPanel)
        self.frame_usuarios.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_usuarios)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_34 = QLabel(self.frame_usuarios)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_18.addWidget(self.label_34)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_35 = QLabel(self.frame_usuarios)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_2.addWidget(self.label_35, 0, 0, 1, 1)

        self.txt_cUsuario = QLineEdit(self.frame_usuarios)
        self.txt_cUsuario.setObjectName(u"txt_cUsuario")
        self.txt_cUsuario.setMinimumSize(QSize(0, 25))
        self.txt_cUsuario.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cUsuario, 1, 0, 1, 1)

        self.label_36 = QLabel(self.frame_usuarios)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_2.addWidget(self.label_36, 2, 0, 1, 1)

        self.txt_cSenha = QLineEdit(self.frame_usuarios)
        self.txt_cSenha.setObjectName(u"txt_cSenha")
        self.txt_cSenha.setMinimumSize(QSize(0, 25))
        self.txt_cSenha.setEchoMode(QLineEdit.Password)
        self.txt_cSenha.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cSenha, 3, 0, 1, 1)

        self.label_37 = QLabel(self.frame_usuarios)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_2.addWidget(self.label_37, 4, 0, 1, 1)

        self.txt_cConfiSenha = QLineEdit(self.frame_usuarios)
        self.txt_cConfiSenha.setObjectName(u"txt_cConfiSenha")
        self.txt_cConfiSenha.setMinimumSize(QSize(0, 25))
        self.txt_cConfiSenha.setEchoMode(QLineEdit.Password)
        self.txt_cConfiSenha.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cConfiSenha, 5, 0, 1, 1)


        self.verticalLayout_18.addLayout(self.gridLayout_2)

        self.btn_cadUsuario = QPushButton(self.frame_usuarios)
        self.btn_cadUsuario.setObjectName(u"btn_cadUsuario")
        self.btn_cadUsuario.setMinimumSize(QSize(100, 30))
        self.btn_cadUsuario.setMaximumSize(QSize(100, 30))

        self.verticalLayout_18.addWidget(self.btn_cadUsuario, 0, Qt.AlignHCenter)


        self.horizontalLayout_14.addLayout(self.verticalLayout_18)


        self.horizontalLayout_12.addWidget(self.frame_usuarios)


        self.verticalLayout_16.addLayout(self.horizontalLayout_12)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.paginas.addWidget(self.pg_configuracoes)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_14 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_28 = QLabel(self.pg_sobre)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_14.addWidget(self.label_28)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.label_30 = QLabel(self.pg_sobre)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(130, 130))
        self.label_30.setStyleSheet(u"background-color: #646464;\n"
"border-radius: 25px;")

        self.horizontalLayout_11.addWidget(self.label_30)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.label_31 = QLabel(self.pg_sobre)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(130, 130))
        self.label_31.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_31)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_14.addLayout(self.horizontalLayout_11)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_4)

        self.label_29 = QLabel(self.pg_sobre)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setWordWrap(True)

        self.verticalLayout_14.addWidget(self.label_29)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.paginas.addWidget(self.pg_sobre)

        self.verticalLayout_7.addWidget(self.paginas)


        self.verticalLayout.addWidget(self.frame_conteudo)

        self.frame_rodape = QFrame(self.frame_principal_conteudo)
        self.frame_rodape.setObjectName(u"frame_rodape")
        self.frame_rodape.setFrameShape(QFrame.StyledPanel)
        self.frame_rodape.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_rodape)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.label_2 = QLabel(self.frame_rodape)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.label_33 = QLabel(self.frame_rodape)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_3.addWidget(self.label_33)


        self.verticalLayout.addWidget(self.frame_rodape)


        self.horizontalLayout.addWidget(self.frame_principal_conteudo)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        self.paginas.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">GERENTIA</span></p></body></html>", None))
        self.lbl_usuario.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Nome de Usuario</p></body></html>", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">status</p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"P\u00c1GINA INICIAL", None))
        self.btn_estoque.setText(QCoreApplication.translate("MainWindow", u"ESTOQUE", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"CONTATOS", None))
        self.btn_configuracoes.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00d5ES", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Gerentia</span></p><p align=\"center\">Sistema de Gerenciamento</p><p align=\"center\"><span style=\" font-weight:700;\">V 1.0.0</span></p></body></html>", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"INFORMA\u00c7\u00d5ES", None))
        self.btn_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Gerentia - Sistema de Gerenciamento</span></p></body></html>", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo.png\"/></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pre\u00e7o de compra:</p></body></html>", None))
        self.txt_pCompra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de Compra", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pre\u00e7o de Venda:</p></body></html>", None))
        self.txt_pVenda.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o de Venda", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Quantidade:</p></body></html>", None))
        self.txt_quantidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">Descri\u00e7\u00e3o: </p></body></html>", None))
        self.txt_descricao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">ADICIONANDO PRODUTO AO ESTOQUE</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nome: </p></body></html>", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">PESQUISAR POR PRODUTO</span></p></body></html>", None))
        self.txt_pesquisa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquise por Nome ou Descri\u00e7\u00e3o", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem = self.tb_pesquisa.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00d3D DE BARRAS", None));
        ___qtablewidgetitem1 = self.tb_pesquisa.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tb_pesquisa.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem3 = self.tb_pesquisa.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem4 = self.tb_pesquisa.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O DE COMPRA", None));
        ___qtablewidgetitem5 = self.tb_pesquisa.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O DE VENDA", None));
        ___qtablewidgetitem6 = self.tb_pesquisa.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem7 = self.tb_pesquisa.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"HORA", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">PRODUTOS CADASTRADOS</span></p></body></html>", None))
        self.btn_relatorio.setText(QCoreApplication.translate("MainWindow", u"Gerar Relat\u00f3rio", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.btn_sincronizar.setText(QCoreApplication.translate("MainWindow", u"Sincronizar", None))
        ___qtablewidgetitem8 = self.tb_estoque.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"C\u00d3D DE BARRAS", None));
        ___qtablewidgetitem9 = self.tb_estoque.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem10 = self.tb_estoque.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem11 = self.tb_estoque.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"QUANTIDADE", None));
        ___qtablewidgetitem12 = self.tb_estoque.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O DE COMPRA", None));
        ___qtablewidgetitem13 = self.tb_estoque.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"PRE\u00c7O DE VENDA", None));
        ___qtablewidgetitem14 = self.tb_estoque.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem15 = self.tb_estoque.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"HORA", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">CONTATOS</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/icon_dev.ico\"/></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Jonatas N. Freitas</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_whatsapp.ico\"/><span style=\" font-size:18pt; vertical-align:super;\">(88) 98136 - 8335</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_email.ico\"/><span style=\" font-size:18pt; vertical-align:super;\">jonatasfreitas008@gmail.com</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_github.ico\"/><a href=\"https://github.com/johnHPX\"><span style=\" font-size:18pt; text-decoration: underline; color:#0078d4; vertical-align:super;\">https://github.com/johnHPX</span></a></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Roberto Carlos</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_whatsapp.ico\"/><span style=\" font-size:18pt; vertical-align:super;\">(88) 99842 - 5346</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_email.ico\"/><span style=\" font-size:18pt; vertical-align:super;\">rcarlos@aluno.ifce.edu.br</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_github.ico\"/><span style=\" font-size:18pt; vertical-align:super;\"/><a href=\"https://github.com/RobertsCJ\"><span style=\" font-size:18pt; text-decoration: underline; color:#0078d4; vertical-align:super;\">https://github.com/RobertsCJ</span></a></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Wallyson S. Souza</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_whatsapp.ico\"/><span style=\" font-size:18pt; vertical-align:super;\">(88) 98833 - 6418</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_email.ico\"/><span style=\" font-size:18pt; vertical-align:super;\">contato.wallyson@hotmail.com</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/icon_github.ico\"/><a href=\"https://github.com/WallysonSantos\"><span style=\" font-size:18pt; text-decoration: underline; color:#0078d4; vertical-align:super;\">https://github.com/WallysonSantos</span></a></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'-apple-system','Roboto','SegoeUI','Segoe UI','Helvetica Neue','Helvetica','Microsoft YaHei','Meiryo UI','Meiryo','Arial Unicode MS','sans-serif'; font-size:12pt; color:#ffffff; background-color:rgba(255,255,255,0.07451);\">Estamos aqui para ajudar! Entre em contato conosco e responderemos o mais r\u00e1pido poss\u00edvel. Sua satisfa\u00e7\u00e3o \u00e9 nossa prioridade.</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">CONFIGURA\u00c7\u00d5ES</span></p><p align=\"center\"><img src=\":/icons/icons/em_desenvolvimento.gif\"/></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">A\u00c7\u00d5ES ADICIONAIS</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">REMOVER UM USU\u00c1RIO</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">MATR\u00cdCULA</span></p></body></html>", None))
        self.txt_matricula.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula do funcion\u00e1rio", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">USU\u00c1RIO</span></p></body></html>", None))
        self.txt_nomeFunci.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do funcion\u00e1rio", None))
        self.btn_removerFunci.setText(QCoreApplication.translate("MainWindow", u"REMOVER", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">ADICONAR UM NOVO USU\u00c1RIO</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">USU\u00c1RIO</span></p></body></html>", None))
        self.txt_cUsuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome de usu\u00e1rio", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">SENHA</span></p></body></html>", None))
        self.txt_cSenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">CONFIRMA\u00c7\u00c3O DE SENHA</span></p></body></html>", None))
        self.txt_cConfiSenha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirme sua senha", None))
        self.btn_cadUsuario.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">SOBRE</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/icon_sqlite.ico\"/></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/icon_python.ico\"/></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Gerentia \u00e9 um sistema de gerenciamento de estoque inovador, desenvolvido com Python e SQLite3, projetado para otimizar e simplificar a gest\u00e3o de estoque. Com uma interface amig\u00e1vel e intuitiva, o Gerentia permite que voc\u00ea adicione, exclua e atualize produtos com facilidade.</span></p><p><span style=\" font-size:14pt;\">O sistema oferece um relat\u00f3rio detalhado dos produtos em estoque, fornecendo informa\u00e7\u00f5es valiosas que podem ajudar a melhorar a efici\u00eancia do seu neg\u00f3cio. Al\u00e9m disso, o Gerentia possui uma funcionalidade de sincroniza\u00e7\u00e3o com um segundo banco de dados, garantindo que suas informa\u00e7\u00f5es estejam sempre atualizadas e acess\u00edveis.</span></p><p><span style=\" font-size:14pt;\">Seja voc\u00ea um pequeno empres\u00e1rio procurando uma maneira simples de gerenciar seu estoque, ou uma grande empresa buscando uma solu\u00e7\u00e3o robusta e confi\u00e1vel, o Gerentia \u00e9 a escol"
                        "ha perfeita. Com o Gerentia, a gest\u00e3o de estoque nunca foi t\u00e3o f\u00e1cil!</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por: Equipe Gerentia", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">\u00a9 2023</p></body></html>", None))
    # retranslateUi

