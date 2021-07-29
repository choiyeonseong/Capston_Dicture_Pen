import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# 선택 단어창
class wordwindow(QtWidgets.QWidget):
    def __init__(self,word,mean):
        super().__init__()
        self.s_word=word
        self.s_mean=mean
        self.__show_word()

    def __show_word(self):
        
        # 상단 버튼 표시
        pause_button = QPushButton("pause")
        pause_button.setIcon(QIcon(QPixmap("icon/pause.png")))
        pause_button.clicked.connect(self.speaker_sound_pause)

        stop_button = QPushButton("stop")
        stop_button.setIcon(QIcon(QPixmap("icon/stop.png")))
        stop_button.clicked.connect(self.speaker_sound_stop)

        innerLayout=QHBoxLayout()
        innerLayout.setContentsMargins(100, 0,0, 0)
        innerLayout.addStretch(1)
        innerLayout.setSpacing(10)
        innerLayout.addWidget(pause_button)
        innerLayout.addWidget(stop_button)

        # 단어 테이블 표시
        self.table = QtWidgets.QTableWidget(self)
        self.table.resize(400, 230)
        self.table.setColumnCount(3)
        self.table.setRowCount(1)

        self.table.setHorizontalHeaderLabels(["단어", "", "뜻"])

        self.table.setRowHeight(0, 200)
        self.table.setItem(0, 0, QTableWidgetItem(self.s_word))
        
        speaker_button = QPushButton()
        speaker_button.setIcon(QIcon(QPixmap("icon/speaker.png")))
        self.table.setCellWidget(0, 1, speaker_button)
        speaker_button.clicked.connect(self.speaker_sound_each)

        self.table.setItem(0, 2, QTableWidgetItem(self.s_mean))

        # self.table.resizeColumnsToContents()
        # self.table.resizeRowsToContents()
        
        layout = QGridLayout(self)
        layout.addLayout(innerLayout, 0, 0)
        layout.addWidget(self.table, 1, 0)

        self.setLayout(layout)

    # speaker_button2_clicked
    def speaker_sound_each(self):
        send=self.table.item(0,0).text()
        print(send)
        print("play")

        # speaker_button3_clicked
    def speaker_sound_pause(self):
        send = self.table.item(0, 0).text()
        print(send)
        print("pause")

    # speaker_button4_clicked
    def speaker_sound_stop(self):
        send = self.table.item(0, 0).text()
        print(send)
        print("stop")

def selected_window(word,mean):
    app = QApplication(sys.argv)
    Window = wordwindow(word,mean)
    Window.setWindowTitle("Selected Word")
    Window.resize(422, 290)
    Window.show()
    sys.exit(app.exec())

if __name__=="__main__":
    word='empty'
    mean='empty'
    selected_window(word,mean)

    # def selected_window(word,mean):

    # app=QApplication(sys.argv)
    # word='empty'
    # mean='empty'
    #
    # Window = wordwindow(word,mean)
    # Window.setWindowTitle("Selected Word")
    # Window.resize(400, 230)
    # Window.show()
    #
    # sys.exit(app.exec())

