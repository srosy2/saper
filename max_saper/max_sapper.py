# -*- coding: utf-8 -*-
import sys
import random

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from max import Ui_MainWindow
from max_dialog import Ui_Dialog



def createArray(size, quantity):
    a = size
    c = quantity
    n = a + 2
    target = c + 1
    arr = [[0] * n for i in range(n)]
    for i in range(c):
        d = 1
        q = random.randint(1, a)
        w = random.randint(1, a)
        if i:
            while d:
                if arr[q][w] == 0:
                    arr[q][w] = target
                    d = 0
                else:
                    q = random.randint(1, a)
                    w = random.randint(1, a)
        else:
            arr[q][w] = target
    for i in range(1, a + 1):
        for j in range(1, a + 1):
            if arr[i][j] >= target:
                arr[i - 1][j - 1] += 1
                arr[i][j - 1] += 1
                arr[i + 1][j - 1] += 1
                arr[i + 1][j] += 1
                arr[i + 1][j + 1] += 1
                arr[i][j + 1] += 1
                arr[i - 1][j] += 1
                arr[i - 1][j + 1] += 1

    for i in range(n):
        for j in range(n):
            if arr[i][j] >= target:
                arr[i][j] = '*'

    del arr[n - 1]
    del arr[0]
    for i in range(a):
        del arr[i][n - 1]
        del arr[i][0]

    return arr


def GameOver(a):
    arr = [i for i in range(a * a)]
    return arr


class DialogWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.numberOfMines = 0
        self.sizeOfArray = 0
        self.initUI()
        self.startGame = 0

    def initUI(self):
        self.show()
        self.pushButton.clicked.connect(self.gettingText)

    def gettingText(self):
        MainWindow.gamesArray = int(self.lineEdit.text())
        MainWindow.gamesMin = int(self.lineEdit_2.text())
        self.numberOfMines = int(self.lineEdit_2.text())
        self.startGame = 1
        am = MainWindow()
        self.hide()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.lengthOfField = ''
        self.numberOfMines = 0
        self.initUI()
        self.inside = []
        self.columns = []
        self.lines = []
        self.arrangement = []
        self.gamesArray = 5
        self.gamesMin = 3

    def initUI(self):
        self.inside = createArray(self.gamesArray, self.gamesMin)
        but = ["but" + str(i) + str(n) for i in range(len(self.inside)) for n in range(len(self.inside))]
        lbl = ["lbl" + str(i) + str(n) for i in range(len(self.inside)) for n in range(len(self.inside))]
        linesFast = 0
        scoreArray = 0
        cp = QDesktopWidget().availableGeometry().center()
        first_number = ""
        second_number = ""
        ad = str(cp)
        pd = []
        for i in ad:
            try:
                pd.append(int(i))
            except ValueError:
                pass
        for i in range(3):
            i += 1
            first_number = first_number + str(pd[i])
        for j in range(3):
            j += 4
            second_number = second_number + str(pd[j])
        first_number = int(first_number) - 50
        second_number = int(second_number) - 50
        for i in self.inside:
            linesFast += 1
            columnsFast = 0
            for j in i:
                columnsFast += 1
                lbl[scoreArray] = QLabel(str(j), self)
                lbl[scoreArray].resize(50, 50)
                lbl[scoreArray].setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
                lbl[scoreArray].move(columnsFast * 50 + first_number - len(self.inside)*25 - 50, second_number - 50 - len(self.inside)*25 + linesFast * 50)
                lbl[scoreArray].setAlignment(Qt.AlignCenter)
                scoreArray += 1
        scoreArray = 0
        def checkArray(n, a, b):

            summa = MainWindow.gamesArray
            if n in b:
                return a
            else:
                b.append(n)
                if (n + 1) % summa:
                    if not ((n + 1) in a):
                        a.append(n + 1)
                    if not int(lbl[n + 1].text()):
                        a = checkArray((n + 1), a, b)
                if n % summa:
                    if not ((n - 1) in a):
                        a.append(n - 1)
                    if not int(lbl[n - 1].text()):
                        a = checkArray(n - 1, a, b)
                if (n + summa) < summa * summa:
                    if not ((n + summa) in a):
                        a.append(n + summa)
                    if not int(lbl[n + summa].text()):
                        a = checkArray(n + summa, a, b)
                if n > summa - 1:
                    if not ((n - summa) in a):
                        a.append(n - summa)
                    if not int(lbl[n - summa].text()):
                        a = checkArray(n - summa, a, b)
                if (n + summa < summa * summa) and ((n + 1) % summa):
                    if not ((n + 1 + summa) in a):
                        a.append(n + 1 + summa)
                    if not int(lbl[n + 1 + summa].text()):
                        a = checkArray(n + 1 + summa, a, b)
                if (n % summa) and ((n + summa) < summa * summa):
                    if not ((n + summa - 1) in a):
                        a.append(n + summa - 1)
                    if not int(lbl[n - 1 + summa].text()):
                        a = checkArray(n - 1 + summa, a, b)
                if (n - summa > 0) and ((n + 1) % summa):
                    if not ((n + 1 - summa) in a):
                        a.append(n + 1 - summa)
                    if not int(lbl[n + 1 - summa].text()):
                        a = checkArray(n + 1 - summa, a, b)
                if (n - summa > 0) and (n % summa):
                    if not ((n - 1 - summa) in a):
                        a.append(n - 1 - summa)
                    if not int(lbl[n - 1 - summa].text()):
                        a = checkArray(n - 1 - summa, a, b)
                return a

        def hideButton():
            MainSumma = MainWindow.gamesArray
            a = []
            b = []
            sender = self.sender()
            sender.hide()
            firstCheck = int(sender.text())
            secondCheck = lbl[firstCheck].text()
            if secondCheck == '*':
                for i in GameOver(MainSumma):
                    but[i].hide()
            else:
                secondCheck = int(secondCheck)
                if not secondCheck:
                    for i in checkArray(firstCheck, a, b):
                        but[i].hide()

        for i in range(len(self.inside)):
            for j in range(len(self.inside)):
                but[scoreArray] = QPushButton(str(scoreArray), self)
                but[scoreArray].setStyleSheet('QPushButton {background-color: #A3C1DA; color: #A3C1DA;} QPushButton:hover{background-color: #B3C1DA}')
                but[scoreArray].setFont(QtGui.QFont("Times", 8, QtGui.QFont.Bold))
                but[scoreArray].resize(50, 50)
                but[scoreArray].move(first_number - len(self.inside)*25 + j * 50, second_number - len(self.inside)*25 + i * 50)
                but[scoreArray].clicked.connect(hideButton)
                scoreArray += 1

        self.showFullScreen()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DialogWindow()
    sys.exit(app.exec_())
