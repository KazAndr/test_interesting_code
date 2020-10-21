import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QLabel, QLineEdit, QLCDNumber,  QGridLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication
from LedIndicatorWidget import * 

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        
        self.lcd = QLCDNumber(self)
        btn = QPushButton('Расчитать', self)
        btn.resize(btn.sizeHint())
        chckBtn = QPushButton('Проверка')
        chckBtn.resize(chckBtn.sizeHint())

        qbtn = QPushButton('Выход', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(btn.sizeHint())
        
        total_bull = QLabel('Общее количество бюллетеней')
        bull_books = QLabel('Выдано по книгам')
        bull_otkrep = QLabel('Выдано дополнительно')
        bull_house = QLabel('Выдано на дому')
        bull_result = QLabel('Неизрасходованных')
        bull_result.setFont(QFont("Times", 15, QFont.Bold)) 
        self.total_bullEdit = QLineEdit('1500')
        self.bull_booksEdit = QLineEdit('0')
        self.bull_otkrepEdit = QLineEdit('0')
        self.bull_houseEdit = QLineEdit('0')
        
        btn.clicked.connect(lambda: self.calculate())

        self.led = LedIndicator(self)
        self.led.setDisabled(True)  # Make the led non clickable

        # Make the led red
        # self.led.on_color_1 = QColor(255, 0, 0)
        # self.led.on_color_2 = QColor(176, 0, 0)
        # self.led.off_color_1 = QColor(28, 0, 0)
        # self.led.off_color_2 = QColor(156, 0, 0)

        chckBtn.clicked.connect(lambda: self.onPressButton())

        
        
        
        grid = QGridLayout() 
        grid.setSpacing(15)


        grid.addWidget(bull_result, 0, 0)
        grid.addWidget(self.lcd, 1, 0, 1, 3)
        grid.addWidget(total_bull, 2, 0)
        grid.addWidget(bull_books, 3 , 0)
        grid.addWidget(bull_otkrep, 4, 0)
        grid.addWidget(bull_house, 5, 0)
        
        grid.addWidget(self.total_bullEdit, 2, 1)
        grid.addWidget(self.bull_booksEdit, 3 , 1)
        grid.addWidget(self.bull_otkrepEdit, 4, 1)
        grid.addWidget(self.bull_houseEdit, 5, 1)


        
        grid.addWidget(btn, 6, 0)
        grid.addWidget(qbtn, 6, 1)
        grid.addWidget(chckBtn, 7, 0)
        grid.addWidget(self.led, 7, 1)
        
        self.setGeometry(300, 300, 300, 400)
        self.setLayout(grid)
        self.setWindowTitle('Test')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Сообщение',
                                    'Вы действительно хотите выйти?',
                                    QMessageBox.Yes | QMessageBox.No, 
                                    QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
              
    def onChanged(self, text):

        self.lbl.setText(str(50*int(text)))
        self.lbl.adjustSize()

    def calculate(self):
        result = (int(self.total_bullEdit.text()) - 
                int(self.bull_booksEdit.text()) - 
                int(self.bull_otkrepEdit.text()) - 
                int(self.bull_houseEdit.text()))

        self.lcd.display(result)




    def onPressButton(self):
        self.led.setChecked(not self.led.isChecked()) 



app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
