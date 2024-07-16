# ------------------------------------------------------------------------------
# Name:        calculator.py
# Author:      Alamine
# Copyright:   (c) Alamine 2024
# Licence:     MIT
# Github:      https://github.com/alaminedione/collection-of-python-projects/calculatrice
#
#                      made with love 💚 hope you like it
# ------------------------------------------------------------------------------

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

# uncomment this if you want to apply stylesheet: qt_material
# from qt_material import apply_stylesheet


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 674)
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(20, 9, 371, 81))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(27)
        self.outputLabel.setFont(font)
        self.outputLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.outputLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter
        )
        self.outputLabel.setObjectName("outputLabel")
        self.Button_percent = QtWidgets.QPushButton(self.centralwidget)
        self.Button_percent.setGeometry(QtCore.QRect(20, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_percent.setFont(font)
        self.Button_percent.setObjectName("Button_percent")
        self.Button_c = QtWidgets.QPushButton(self.centralwidget)
        self.Button_c.setGeometry(QtCore.QRect(120, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_c.setFont(font)
        self.Button_c.setObjectName("Button_c")
        self.Button_parenthese_left = QtWidgets.QPushButton(self.centralwidget)
        self.Button_parenthese_left.setGeometry(QtCore.QRect(220, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_parenthese_left.setFont(font)
        self.Button_parenthese_left.setObjectName("Button_arrow")
        self.Button_divide = QtWidgets.QPushButton(self.centralwidget)
        self.Button_divide.setGeometry(QtCore.QRect(320, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_divide.setFont(font)
        self.Button_divide.setObjectName("Button_divide")
        self.Button_multiple = QtWidgets.QPushButton(self.centralwidget)
        self.Button_multiple.setGeometry(QtCore.QRect(320, 210, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_multiple.setFont(font)
        self.Button_multiple.setObjectName("Button_multiple")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(20, 210, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_7.setFont(font)
        self.Button_7.setObjectName("Button_7")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(220, 210, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_9.setFont(font)
        self.Button_9.setObjectName("Button_9")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(120, 210, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_8.setFont(font)
        self.Button_8.setObjectName("Button_8")
        self.Button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_minus.setGeometry(QtCore.QRect(320, 310, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_minus.setFont(font)
        self.Button_minus.setObjectName("Button_minus")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(20, 310, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_4.setFont(font)
        self.Button_4.setObjectName("Button_4")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(220, 310, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_6.setFont(font)
        self.Button_6.setObjectName("Button_6")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(120, 310, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_5.setFont(font)
        self.Button_5.setObjectName("Button_5")
        self.Button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_plus.setGeometry(QtCore.QRect(320, 410, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_plus.setFont(font)
        self.Button_plus.setObjectName("Button_plus")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(20, 410, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_1.setFont(font)
        self.Button_1.setObjectName("Button_1")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(220, 410, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_3.setFont(font)
        self.Button_3.setObjectName("Button_3")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(120, 410, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_2.setFont(font)
        self.Button_2.setObjectName("Button_2")
        self.Button_egal = QtWidgets.QPushButton(self.centralwidget)
        self.Button_egal.setGeometry(QtCore.QRect(320, 510, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_egal.setFont(font)
        self.Button_egal.setObjectName("Button_egal")
        self.Butthon_parenthese_right = QtWidgets.QPushButton(self.centralwidget)
        self.Butthon_parenthese_right.setGeometry(QtCore.QRect(20, 510, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Butthon_parenthese_right.setFont(font)
        self.Butthon_parenthese_right.setObjectName("Button_plus_minus")
        self.Button_decimal = QtWidgets.QPushButton(self.centralwidget)
        self.Button_decimal.setGeometry(QtCore.QRect(220, 510, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        font.setPointSize(25)
        self.Button_decimal.setFont(font)
        self.Button_decimal.setObjectName("Button_decimal")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(120, 510, 75, 75))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Mono")
        font.setPointSize(25)
        self.Button_0.setFont(font)
        self.Button_0.setObjectName("Button_0")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 600, 361, 21))
        font = QtGui.QFont()
        font.setFamily("Hack Nerd Font")
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # connectect  buttons to  write_expression function
        self.Button_percent.clicked.connect(lambda: self.write_expression("%"))
        self.Button_parenthese_left.clicked.connect(lambda: self.write_expression("("))
        self.Button_divide.clicked.connect(lambda: self.write_expression("/"))
        self.Button_multiple.clicked.connect(lambda: self.write_expression("*"))
        self.Button_minus.clicked.connect(lambda: self.write_expression("-"))
        self.Button_plus.clicked.connect(lambda: self.write_expression("+"))
        self.Button_1.clicked.connect(lambda: self.write_expression("1"))
        self.Button_2.clicked.connect(lambda: self.write_expression("2"))
        self.Button_3.clicked.connect(lambda: self.write_expression("3"))
        self.Button_4.clicked.connect(lambda: self.write_expression("4"))
        self.Button_5.clicked.connect(lambda: self.write_expression("5"))
        self.Button_6.clicked.connect(lambda: self.write_expression("6"))
        self.Button_7.clicked.connect(lambda: self.write_expression("7"))
        self.Button_8.clicked.connect(lambda: self.write_expression("8"))
        self.Button_9.clicked.connect(lambda: self.write_expression("9"))
        self.Button_0.clicked.connect(lambda: self.write_expression("0"))
        self.Button_decimal.clicked.connect(lambda: self.write_expression("."))
        self.Butthon_parenthese_right.clicked.connect(
            lambda: self.write_expression(")")
        )

        # connect clear button to clear_output function
        self.Button_c.clicked.connect(lambda: self.clear_output())

        # connect egual button to write_result function
        self.Button_egal.clicked.connect(
            lambda: self.write_result(self.outputLabel.text())
        )

    # function to write expression in output label
    def write_expression(self, expression):
        if self.outputLabel.text() == "0" or self.outputLabel.text() == "Error":
            self.outputLabel.setText("")
        self.outputLabel.setText(self.outputLabel.text() + expression)

    # function to clear output label
    def clear_output(self):
        self.outputLabel.setText("0")

    # function to evaluate expression
    # WARNING: security risk
    # eval can evaluate malicious code
    # TODO: try to find a way to evaluate expression without eval

    def evaluate_expression(self, expression):
        try:
            # NOTE: try to evaluate expression becaause eval can't evaluate some expression
            return eval(expression)
        except:
            return None

    # function to write expression in output label
    def write_result(self, expression):
        result = self.evaluate_expression(expression)
        if result:
            self.outputLabel.setText(str(result))
        else:
            self.outputLabel.setText("Error")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.Button_percent.setText(_translate("MainWindow", "%"))
        self.Button_c.setText(_translate("MainWindow", "C"))
        self.Button_parenthese_left.setText(_translate("MainWindow", "("))
        self.Button_divide.setText(_translate("MainWindow", "/"))
        self.Button_multiple.setText(_translate("MainWindow", "x"))
        self.Button_minus.setText(_translate("MainWindow", "-"))
        self.Button_plus.setText(_translate("MainWindow", "+"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_egal.setText(_translate("MainWindow", "="))
        self.Butthon_parenthese_right.setText(_translate("MainWindow", ")"))
        self.Button_decimal.setText(_translate("MainWindow", "."))
        self.label.setText(
            _translate("MainWindow", "made with love 💚 by alaminedione ")
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # uncomment this if you want to apply stylesheet from qt_material
    # apply_stylesheet(app, theme='dark_teal.xml')

    MainWindow.show()
    sys.exit(app.exec_())
