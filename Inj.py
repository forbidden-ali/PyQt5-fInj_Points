# -*- coding: utf-8 -*-

"""
Module implementing Inj.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog,  QApplication
import spid
from Ui_Inj import Ui_Dialog


class Inj(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super(Inj, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_b_1_clicked(self):
        self.lW_1.clear()
        self.lW_2.clear()
        filep = self.lE_1.text()
        filec = open(filep)
        for line in filec.readlines():
            line = line.strip()
            if not len(line):
                break
            self.lW_1.addItem(line)
        
    @pyqtSlot()
    def on_b_2_clicked(self):
        rows = self.lW_1.count()
        file2 = open('file2.txt', 'a')
        print(rows)
        for row in range(0, rows, 1):
            url1 = self.lW_1. item(row).text()
            print(url1)
            points = spid.spide(url1)
            #print(points2)
        self.lW_2.addItems(points)
        for row2 in points:
            file2.write(row2+'\n')
        points = []
        file2.close()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    Inj_p = Inj()
    Inj_p.show()
    sys.exit(app.exec_())
