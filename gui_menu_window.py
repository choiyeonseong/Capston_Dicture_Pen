import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

from camera import cam_on
from crawling import get_dic_search

from gui_date_window import MyApp
from gui_selectedword_window import *
from gui_table_window import *

#메뉴창

class menuwindow(QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        
        # 위 버튼
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 40, 181, 91))
        # self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        
        # 아래 버튼
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 160, 181, 91))
        # self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.my_words)  # Word Table로 연결

        self.pushButton_2.clicked.connect(self.camera)  # 카메라 실행

    # 표시 이름 설정
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Menu"))
        self.pushButton.setText(_translate("Dialog", "My words"))
        self.pushButton_2.setText(_translate("Dialog", "Camera"))

    #pushButton
    def my_words(self):
        self.ex = MyApp()
        self.ex.show()

    #pushButton_2
    def camera(self):
        # word, mean = cam_on()
        print("cam_on")

        self.Window = wordwindow(word, mean)
        self.Window.setWindowTitle("Selected Word")
        self.Window.resize(422, 290)
        self.Window.show()

if __name__=="__main__":
    app=QApplication(sys.argv)

    Dialog=QtWidgets.QDialog()
    ui=menuwindow()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec())
