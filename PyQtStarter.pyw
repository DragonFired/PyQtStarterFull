#!/usr/bin/env python

import sys
import PyQtStarterResources_rc
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class PyQtStarterMainWindow(QMainWindow):
    """A basic shell for a PyQt Project."""

    def __init__(self, parent=None):
        """ Build a GUI  main window for PyQtStarter."""

        super().__init__(parent)
        uic.loadUi("PyQtStarterMainWindow.ui", self)

        self.dummyVariable = True
        self.textOutput = ""

        self.pushButton.clicked.connect(self.pushButtonClickedHandler)

    def __str__(self):
        """String representation for PyQtStarter.
        """

        return "Gettin' started with Qt!!"

    def updateUI(self):
        self.textOutputUI.setText(self.textOutput)

        # Player asked for another roll of the dice.
    def pushButtonClickedHandler(self):
        print("Inside pushButtonClickedHandler()\n")
        if (self.textOutput != "Hello World!" or self.textOutput == ""):
            self.textOutput = "Hello World!"
        else:
            self.textOutput = "Happy to Meet You."
        self.updateUI()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    PyQtStarterApp = PyQtStarterMainWindow()
    PyQtStarterApp.updateUI()
    PyQtStarterApp.show()
    sys.exit(app.exec_())
