import sqlite3
import chooser_lib as chooser

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):

    def __init__(self, way_to_raw, way_to_catalog) -> None:

        super().__init__()
        self.way_to_raw = way_to_raw
        self.way_to_catalog = way_to_catalog


    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 980, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 0, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PhotoChooser"))
        self.label_5.setText(_translate("MainWindow", "Путь до raw файлов:"))
        self.label_4.setText(_translate("MainWindow", self.way_to_raw))
        self.pushButton_3.setText(_translate("MainWindow", "изменить"))
        self.label.setText(_translate("MainWindow", "Выбранные фотографии:"))
        self.label_3.setText(_translate("MainWindow", "Путь до каталога lightroom:"))
        self.label_2.setText(_translate("MainWindow", self.way_to_catalog))
        self.pushButton_2.setText(_translate("MainWindow", "изменить"))
        self.pushButton.setText(_translate("MainWindow", "OK"))

        self.pushButton.clicked.connect(self.push_button)
        self.pushButton_2.clicked.connect(self.push_button_2)
        self.pushButton_3.clicked.connect(self.push_button_3)

        self.plainTextEdit.setPlaceholderText('вставте текст с номерами выбранных фотографий')


    def push_button(self):

        try:
        
            raw_file_list = chooser.get_list_of_raw_files(self.way_to_raw)

            text = self.plainTextEdit.toPlainText()
            changed_photos_names_list = chooser.get_list_from_text(text)

            update_list = chooser.get_files_to_update(raw_file_list, changed_photos_names_list)
            chooser.update_rating_in_catalog(self.way_to_catalog, self.way_to_raw, update_list)
            
        except sqlite3.DatabaseError:
            self.pushButton.setText("файл каталога выбран неверно")
        except FileNotFoundError:
            self.pushButton.setText("в директории нет raw-файлов")
        except ValueError:
            self.pushButton.setText("файл каталога выбран неверно")
    
    
    def push_button_2(self):
        self.way_to_catalog = chooser.change_way_to_file('выбор каталога lightroom')
        self.label_2.setText(self.way_to_catalog)
        chooser.refresh_way_to_catalog_info(self.way_to_catalog)
        self.pushButton.setText("OK")


    def push_button_3(self):
        self.way_to_raw = chooser.change_way_to_dir('выбор директории с raw-файлами')
        self.label_4.setText(self.way_to_raw)
    



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    way_to_raw = chooser.get_way_to_raw()
    way_to_catalog = chooser.get_way_to_catalog()

    ui = Ui_MainWindow(way_to_raw, way_to_catalog)
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())