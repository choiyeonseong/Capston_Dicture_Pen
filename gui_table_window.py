from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

#단어장 데이터 설정
from openpyxl import load_workbook

#단어장 창
class tablewindow(QtWidgets.QWidget):
    def __init__(self,sheetname):
        super().__init__()

        self.getData(sheetname)
        self.initUI()
        self.setTable()

    #excel 불러오기
    def getData(self,sheetname):
        load_wb = load_workbook("resource/dictionary_example.xlsx", data_only=True)

        load_ws = load_wb[sheetname]

        self.words = []
        self.means = []
        self.examples = []

        for row in load_ws.rows:
            for cell in row:
                if (cell.column == 1):
                    self.words.append(cell.value)
                if (cell.column == 2):
                    self.means.append(cell.value)
                if (cell.column == 3):
                    self.examples.append(cell.value)

    def initUI(self):

        # #label
        # self.lbl=QLabel()

        #checkAll
        self.checkBoxAll = QtWidgets.QCheckBox("Select All")
        self.checkBoxAll.setChecked(False)
        self.checkBoxAll.stateChanged.connect(self.onStateChangePrincipal)
        self.checkboxes=[]

        #play
        playAll_button = QPushButton("play all")
        # playAll_button.setGeometry(10,10,0,0)
        playAll_button.setIcon(QIcon(QPixmap("icon/speaker.png")))
        playAll_button.clicked.connect(self.speaker_sound_all)

        pause_button=QPushButton("pause")
        pause_button.setIcon(QIcon(QPixmap("icon/pause.png")))
        pause_button.clicked.connect(self.speaker_sound_pause)

        stop_button = QPushButton("stop")
        stop_button.setIcon(QIcon(QPixmap("icon/stop.png")))
        stop_button.clicked.connect(self.speaker_sound_stop)

        self.slider=QSlider(Qt.Horizontal)
        self.slider.setRange(1,5)
        self.slider.setSingleStep(1)
        self.slider.setValue(3)
        self.slider.valueChanged.connect(self.showValue)


        #table
        self.table=QtWidgets.QTableWidget()
        self.table.resize(1000,500)
        self.table.setColumnCount(4)
        self.table.setRowCount(len(self.words))


        self.table.horizontalHeader().setVisible(False)  #table헤더설정

        self.table.cellClicked.connect(self.__mycell_clicked)

        #layout 설정
        innerLayout=QHBoxLayout()
        innerLayout.setContentsMargins(0,0,300,0)
        innerLayout.addStretch(1)
        innerLayout.setSpacing(50)
        # innerLayout.addWidget(self.lbl)
        innerLayout.addWidget(self.checkBoxAll)
        innerLayout.addWidget(playAll_button)
        innerLayout.addWidget(pause_button)
        innerLayout.addWidget(stop_button)
        innerLayout.addWidget(self.slider)

        layout=QGridLayout(self)
        layout.addLayout(innerLayout,0,0)
        layout.addWidget(self.table,1,0)

        self.setLayout(layout)



    def setTable(self):
        #table 내용
        for i in range(len(self.words)):

            # checkbox
            self.checkBox = QtWidgets.QCheckBox(self.words[i])
            self.checkboxes.append(self.checkBox)

            self.table.setCellWidget(i, 0, self.checkBox)

            # self.table.resizeRowsToContents()
            self.table.resizeColumnsToContents()


            for checkbox in self.checkboxes:
                checkbox.stateChanged.connect(self.onStateChange)


            #word
            self.table.setItem(i, 1, QTableWidgetItem(self.words[i]))

            #speaker
            play_button = QPushButton()
            play_button.setIcon(QIcon(QPixmap("icon/speaker.png")))
            self.table.setCellWidget(i, 1, play_button)
            play_button.clicked.connect(self.speaker_sound_each(i))

            self.table.setColumnWidth(1, 50)



            #mean,example
            self.table.setItem(i, 2, QTableWidgetItem(self.means[i]))
            self.table.setColumnWidth(2, 300)

            self.table.setItem(i, 3, QTableWidgetItem(self.examples[i]))
            self.table.setColumnWidth(3, 400)


            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)


    @QtCore.pyqtSlot(int, int)
    def __mycell_clicked(self, row, col):
        if col>=2:
            cell = self.table.item(row, col)
            txt=cell.text()

            msg = QMessageBox.information(self, 'clicked cell', txt)
            return
        else:
            return

    @QtCore.pyqtSlot(int)
    def onStateChangePrincipal(self, state):
        if state == QtCore.Qt.Checked:
            for checkbox in self.checkboxes:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)
        else:
            for checkbox in self.checkboxes:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)

    @QtCore.pyqtSlot(int)
    def onStateChange(self, state):
        self.checkBoxAll.blockSignals(True)
        self.checkBoxAll.setChecked(QtCore.Qt.Unchecked)
        self.checkBoxAll.blockSignals(False)

    #speaker_button1_clicked
    def speaker_sound_all(self):

        print("sound_all")
        for checkbox in self.checkboxes:
            if checkbox.isChecked() == True:
                txt= checkbox.text()
                print(txt)
                time.sleep(self.slider.value())





    #speaker_button2_clicked
    def speaker_sound_each(self,row):
        def speak():
            want=self.table.item(row,1).text()
            print(want)
        return speak

    #speaker_button3_clicked
    def speaker_sound_pause(self):
        row = self.table.currentRow()
        want = self.table.item(row, 1).text()
        print("pause-", want)

    # speaker_button4_clicked
    def speaker_sound_stop(self):
        row = self.table.currentRow()
        want = self.table.item(row, 1).text()
        print("stop-", want)


    def showValue(self):
        print(str(self.slider.value()))


if __name__=="__main__":

    import sys

    app=QApplication(sys.argv)
    sheetname='7월 14일'
    Window = tablewindow(sheetname)
    Window.setWindowTitle("My Words")
    Window.resize(1000, 500)
    Window.show()

    sys.exit(app.exec())
