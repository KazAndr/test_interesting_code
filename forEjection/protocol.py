import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QLabel, QLineEdit, QGridLayout, QMainWindow, QDialog
from PyQt5.QtGui import QFont, QIcon 
from PyQt5.QtCore import QCoreApplication
#from LedIndicatorWidget import * 




class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
                
        self.btn = QPushButton('Проверка контрольных соотношений', self)
        #chckBtn = QPushButton('Проверка')

        qbtn = QPushButton('Выход', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        
        r1 = QLabel('[1] Число избирателей, включенных в список на момент окончания голосованияx')
        r2 = QLabel('[2] Число избирательных бюллетеней, полученных участковой избирательной комиссией')
        r3 = QLabel('[3] Число избирательных бюллетеней выданных избирателями, проголосовавшим досрочно')
        r4 = QLabel('[4] Число избирательных бюллетеней, выданных УИК избирателям в помещении для голосавания в помещении для голосования')
        r5 = QLabel('[5] Число избирательных бюллетеней, выданных УИК избирателям, проголосовавшим вне помещения для голосования в день голосования')
        r6 = QLabel('[6] Число погашенных избирательных бюллетеней')
        r7 = QLabel('[7] Число избирательных бюллетеней, содержащихся в переносных ящиках для голосования')
        r8 = QLabel('[8] Число избирательных бюллетеней, содержащихся в стационарных ящиках для голосования')
        r9 = QLabel('[9] Число недействительных избирательных бюллетеней')
        r10 = QLabel('[10] Число действительных избирательных бюллетеней')
        r11 = QLabel('[11] Число утраченных избирательных бюллетеней')
        r12 = QLabel('[12] Число избирательных бюллетеней, не учтенных при получении')

        r1Small = QLabel('[1]')
        r2Small = QLabel('[2]')
        r3Small = QLabel('[3]')
        r4Small = QLabel('[4]')
        r5Small = QLabel('[5]')
        r6Small = QLabel('[6]')
        r7Small = QLabel('[7]')
        r8Small = QLabel('[8]')
        r9Small = QLabel('[9]')
        r10Small = QLabel('[10]')
        r11Small = QLabel('[11]')
        r12Small = QLabel('[12]')
       
        self.r1Edit = QLineEdit('0')
        self.r2Edit = QLineEdit('0')
        self.r3Edit = QLineEdit('0')
        self.r4Edit = QLineEdit('0')
        self.r5Edit = QLineEdit('0')
        self.r6Edit = QLineEdit('0')
        self.r7Edit = QLineEdit('0')
        self.r8Edit = QLineEdit('0')
        self.r9Edit = QLineEdit('0')
        self.r10Edit = QLineEdit('0')
        self.r11Edit = QLineEdit('0')
        self.r12Edit = QLineEdit('0')

        self.btn.clicked.connect(self.showdialog)
        
        grid = QGridLayout() 
        grid.setSpacing(5)


        grid.addWidget(r1, 0, 0)
        grid.addWidget(r2, 1, 0 )
        grid.addWidget(r3, 2, 0)
        grid.addWidget(r4, 3 , 0)
        grid.addWidget(r5, 4, 0)
        grid.addWidget(r6, 5, 0)
        grid.addWidget(r7, 6, 0)
        grid.addWidget(r8, 7 , 0)
        grid.addWidget(r9, 8, 0)
        grid.addWidget(r10, 9, 0)
        grid.addWidget(r11, 10, 0)
        grid.addWidget(r12, 11, 0)
        
        grid.addWidget(r1Small, 0, 1)
        grid.addWidget(r2Small, 1, 1)
        grid.addWidget(r3Small, 2, 1)
        grid.addWidget(r4Small, 3, 1)
        grid.addWidget(r5Small, 4, 1)
        grid.addWidget(r6Small, 5, 1)
        grid.addWidget(r7Small, 6, 1)
        grid.addWidget(r8Small, 7, 1)
        grid.addWidget(r9Small, 8, 1)
        grid.addWidget(r10Small, 9, 1)
        grid.addWidget(r11Small, 10, 1)
        grid.addWidget(r12Small, 11, 1)
    
        grid.addWidget(self.r1Edit, 0, 2)
        grid.addWidget(self.r2Edit, 1, 2)
        grid.addWidget(self.r3Edit, 2, 2)
        grid.addWidget(self.r4Edit, 3, 2)
        grid.addWidget(self.r5Edit, 4, 2)
        grid.addWidget(self.r6Edit, 5, 2)
        grid.addWidget(self.r7Edit, 6, 2)
        grid.addWidget(self.r8Edit, 7, 2)
        grid.addWidget(self.r9Edit, 8, 2)
        grid.addWidget(self.r10Edit, 9, 2)
        grid.addWidget(self.r11Edit, 10, 2)
        grid.addWidget(self.r12Edit, 11, 2)


        grid.addWidget(self.btn, 12, 0)
        grid.addWidget(qbtn, 12, 2)
        #grid.addWidget(chckBtn, 7, 0)
        #grid.addWidget(self.led, 7, 1)
        
        self.setGeometry(300, 300, 300, 300)
        self.setLayout(grid)
        self.setWindowTitle('Test')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()
        

    def on_pushButton_clicked(self):
        self.dialog.show()


    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Сообщение',
                                    'Вы действительно хотите выйти?',
                                    QMessageBox.Yes | QMessageBox.No, 
                                    QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def showdialog(self):
        """
       1 : 2 = 3 + 4 + 5 + 6 + 11 - 12
       2 : 3 + 4 + 5 >= 9 + 10 
       3 : 4 >= 8
       4 : 3 + 5 >= 7
       5 : 7 + 8 = 9 + 10
       6 : 1 >= 3 + 4 + 5
        """
        r1 = int(self.r1Edit.text())
        r2 = int(self.r2Edit.text())
        r3 = int(self.r3Edit.text())
        r4 = int(self.r4Edit.text())
        r5 = int(self.r5Edit.text())
        r6 = int(self.r6Edit.text())
        r7 = int(self.r7Edit.text())
        r8 = int(self.r8Edit.text())
        r9 = int(self.r9Edit.text())
        r10 = int(self.r10Edit.text())
        r11 = int(self.r11Edit.text())
        r12 = int(self.r12Edit.text())
       

        d = QDialog()

        if r2 == r3 + r4 + r5 + r6 + r11 - r12:
            first = QLabel('Контрольное соотношение [2] = [3] + [4] + [5] + [6] + [11] - [12] <font color="green"><b>ВЫПОЛНЯЕТСЯ</b></font>', d)
            firstRes = QLabel('<b>' + str(r2) + ' = ' + str(r3 + r4 + r5 + r6 + r11 - r12) + '</b>')
        else:
            first = QLabel('Контрольное соотношение [2] = [3] + [4] + [5] + [6] + [11] - [12] <font color="red"><b>НЕ ВЫПОЛНЯЕТСЯ</b></font>', d)
            firstRes = QLabel('<b>' + str(r2) + ' не равно ' + str(r3 + r4 + r5 + r6 + r11 - r12) + '</b>' )

        if r3 + r4 + r5 >= r9 + r10:
            second = QLabel('Математическое соотношение [3] + [4] + [5] >= [9] + [10] <font color="green"><b>ВЫПОЛНЯЕТСЯ</b></font>', d)
            secondRes = QLabel('<b>' + str(r3 + r4 + r5 ) + ' >= ' + str(r9 + r10) + '</b>')

        else:
            second = QLabel('Математическое соотношение [3] + [4] + [5] >= [9] + [10] <font color="red"><b>НЕ ВЫПОЛНЯЕТСЯ</b></font>', d)
            secondRes = QLabel('<b>' + str(r3 + r4 + r5 ) + ' меньше ' + str(r9 + r10) + '</b>')


        if r4 >= r8:
            third = QLabel('Логическое соотношение [4] >= [8] <font color="green"><b>ВЫПОЛНЯЕТСЯ</b></font>', d)
            thirdRes = QLabel('<b>' + str(r4) + ' >= ' + str(r8) + '</b>')

        else:
            third = QLabel('Логическое соотношение [4] >= [8] <font color="red"><b>НЕ ВЫПОЛНЯЕТСЯ</b></font>', d)
            thirdRes = QLabel('<b>' + str(r4) + ' меньше ' + str(r8) + '</b>')


        if r3 + r5 >= r7:
            fourth = QLabel('Логическое соотношение [3] + [5] >= [7] <font color="green"><b>ВЫПОЛНЯЕТСЯ</b></font>', d)
            fourthRes = QLabel('<b>' + str(r3 + r5) + ' >= ' + str(r7) + '</b>')

        else:
            fourth = QLabel('Логическое соотношение [3] + [5] >= [7] <font color="red"><b>НЕ ВЫПОЛНЯЕТСЯ</b></font>', d)
            fourthRes = QLabel('<b>' + str(r3 + r5) + ' меньше ' + str(r7) + '</b>')


        if r7 + r8 == r9 + r10:
            five = QLabel('Математическое соотношение [7] + [8] = [9] + [10] <font color="green"><b>ВЫПОЛНЯЕТСЯ</b></font>', d)
            fiveRes = QLabel('<b>' + str(r7 + r8) + ' = ' + str(r9 + r10) + '</b>')

        else:
            five = QLabel('Математическое соотношение [7] + [8] = [9] + [10] <font color="red"><b>НЕ ВЫПОЛНЯЕТСЯ</b></font>', d)
            fiveRes =  QLabel('<b>' + str(r7 + r8) + '  не равно ' + str(r9 + r10) + '</b>')


        if r1 >= r3 + r4 + r5:
            six = QLabel('Логическое соотношение [1] >= [3] + [4] + [5] <font color="green"><b>ВЫПОЛНЯЕТСЯ</b></font>', d)
            sixRes = QLabel('<b>' + str(r1) + ' >= ' + str(r3 + r4 +r5) + '</b>')

        else:
            six = QLabel('Логическое соотношение [1] >= [3] + [4] + [5] <font color="red"><b>НЕ ВЫПОЛНЯЕТСЯ</b></font>', d)
            sixRes = QLabel('<b>' + str(r1) + ' меньше ' + str(r3 + r4 + r5) + '</b>')






        myGrid = QGridLayout(d)
        myGrid.addWidget(first, 0, 0)
        myGrid.addWidget(firstRes, 1, 0 )
        myGrid.addWidget(second, 2, 0)
        myGrid.addWidget(secondRes, 3, 0)
        myGrid.addWidget(third, 4, 0)
        myGrid.addWidget(thirdRes, 5, 0)
        myGrid.addWidget(fourth, 6, 0)
        myGrid.addWidget(fourthRes, 7, 0)
        myGrid.addWidget(five, 8, 0)
        myGrid.addWidget(fiveRes, 9, 0)
        myGrid.addWidget(six, 10, 0)
        myGrid.addWidget(sixRes, 11, 0)
        d.setWindowTitle("Результат проверки соотношений")
        d.setGeometry(300, 300, 300, 300)
        d.setWindowIcon(QIcon('icon.png'))
        d.exec_()



app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
