# python 3
# -*- coding: utf-8 -*-
# w_j1ahu1@163.com

import time
import sys
import pymysql
from PyQt5.QtWidgets import (QWidget,QPushButton, QMessageBox, QLineEdit,QLabel,
    QTextEdit,QApplication,QDesktopWidget)
from PyQt5.QtGui import QIcon

con = pymysql.connect(host="localhost", port=3306, user="root", passwd="mysqlrandow", db="wikidata", charset="utf8")
cur = con.cursor()


class GUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 执行时间标签
        self.time=QLabel('',self)
        self.time.move(100,80)
        self.time.resize(200, 20)
        # ID标签
        self.sid = QLabel('ID', self)
        self.sid.move(25, 50)
        self.sid.resize(50, 20)
        # ID搜索框
        self.searchBar = QLineEdit(self)
        self.searchBar.move(100, 30)
        self.searchBar.resize(450,50)
        # 搜索按钮
        self.searchButton = QPushButton("Search",self)
        self.searchButton.move(600, 30)
        self.searchButton.resize(80,50)
        # 清空按钮
        self.clearButton = QPushButton("Clear", self)
        self.clearButton.move(700, 30)
        self.clearButton.resize(80, 50)
        # cnlabels
        self.cnlabels = QLabel('CNLABELS', self)
        self.cnlabels.move(15, 140)
        self.cnlabels.resize(50, 20)
        self.cnlabelsEdit=QTextEdit(self)
        self.cnlabelsEdit.move(100, 120)
        self.cnlabelsEdit.resize(680,60)
        # enlabels
        self.enlabels = QLabel('ENLABELS', self)
        self.enlabels.move(15, 200)
        self.enlabels.resize(50, 20)
        self.enlabelsEdit = QTextEdit(self)
        self.enlabelsEdit.move(100, 180)
        self.enlabelsEdit.resize(680, 60)
        # descriptions
        self.descriptions = QLabel('DESCRIPTIONS', self)
        self.descriptions.move(15, 260)
        self.descriptions.resize(80, 20)
        self.descriptionsEdit = QTextEdit(self)
        self.descriptionsEdit.move(100, 240)
        self.descriptionsEdit.resize(680, 60)
        # aliases
        self.aliases = QLabel('ALIASES', self)
        self.aliases.move(15, 320)
        self.aliases.resize(80, 20)
        self.aliasesEdit = QTextEdit(self)
        self.aliasesEdit.move(100, 300)
        self.aliasesEdit.resize(680, 60)
        # properties
        self.properties = QLabel('PROPERTIES', self)
        self.properties.move(15, 380)
        self.properties.resize(80, 20)
        self.propertiesEdit = QTextEdit(self)
        self.propertiesEdit.move(100, 360)
        self.propertiesEdit.resize(680, 60)
        # datavalue
        self.datavalue = QLabel('DATAVALUE', self)
        self.datavalue.move(15, 440)
        self.datavalue.resize(80, 20)
        self.datavalueEdit = QTextEdit(self)
        self.datavalueEdit.move(100, 420)
        self.datavalueEdit.resize(680, 60)
        # qhash
        self.qhash = QLabel('QHASH', self)
        self.qhash.move(15, 500)
        self.qhash.resize(80, 20)
        self.qhashEdit = QTextEdit(self)
        self.qhashEdit.move(100, 480)
        self.qhashEdit.resize(680, 60)
        # qdatavalue
        self.qdatavalue = QLabel('QDATAVALUE', self)
        self.qdatavalue.move(15, 560)
        self.qdatavalue.resize(80, 20)
        self.qdatavalueEdit = QTextEdit(self)
        self.qdatavalueEdit.move(100, 540)
        self.qdatavalueEdit.resize(680, 60)
        # rhash
        self.rhash = QLabel('RHASH', self)
        self.rhash.move(15, 620)
        self.rhash.resize(80, 20)
        self.rhashEdit = QTextEdit(self)
        self.rhashEdit.move(100, 600)
        self.rhashEdit.resize(680, 60)
        # rdatavalue
        self.rdatavalue = QLabel('RDATAVALUE', self)
        self.rdatavalue.move(15, 680)
        self.rdatavalue.resize(80, 20)
        self.rdatavalueEdit = QTextEdit(self)
        self.rdatavalueEdit.move(100, 660)
        self.rdatavalueEdit.resize(680, 60)
        # snakorder
        self.snakorder = QLabel('SNAKORDER', self)
        self.snakorder.move(15, 740)
        self.snakorder.resize(80, 20)
        self.snakorderEdit = QTextEdit(self)
        self.snakorderEdit.move(100, 720)
        self.snakorderEdit.resize(680, 60)

        self.resize( 800, 800)
        self.center()
        self.setWindowTitle('WikiData---ID-SEARCH')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.show()
        self.searchButton.clicked.connect(self.fun)
        self.clearButton.clicked.connect(self.clear)


    def fun(self):
        start = time.clock()
        queryid=self.searchBar.text()
        sql1 = "SELECT cnlabels FROM entities WHERE id = '%s'" % (queryid)
        cur.execute(sql1)
        cnlabels = str(cur.fetchall()).replace('\'','').replace(',','').replace('(','').replace(')','')
        con.commit()
        self.cnlabelsEdit.append(cnlabels)
        sql2 = "SELECT enlabels FROM entities WHERE id = '%s'" % (queryid)
        cur.execute(sql2)
        enlabels = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.enlabelsEdit.append(enlabels)
        sql3 = "SELECT descriptions FROM entities WHERE id = '%s'" % (queryid)
        cur.execute(sql3)
        descriptions = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.descriptionsEdit.append(descriptions)
        sql4 = "SELECT aliases FROM entities WHERE id = '%s'" % (queryid)
        cur.execute(sql4)
        aliases = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.aliasesEdit.append(aliases)
        sql5 = "SELECT properties FROM mainsnak WHERE id = '%s'" % (queryid)
        cur.execute(sql5)
        properties = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.propertiesEdit.append(properties)
        sql6 = "SELECT datavalue_value FROM mainsnak WHERE id = '%s'" % (queryid)
        cur.execute(sql6)
        datavalue= str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        self.datavalueEdit.append(datavalue)
        sql7 = "SELECT qhash FROM qualifiers WHERE id = '%s'" % (queryid)
        cur.execute(sql7)
        qhash = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.qhashEdit.append(qhash)
        sql8 = "SELECT datavalue_value FROM qualifiers WHERE id = '%s'" % (queryid)
        cur.execute(sql8)
        qdatavalue = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.qdatavalueEdit.append(qdatavalue)
        sql9 = "SELECT rhash FROM reference WHERE id = '%s'" % (queryid)
        cur.execute(sql9)
        rhash = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.rhashEdit.append(rhash)
        sql10 = "SELECT datavalue_value FROM reference WHERE id = '%s'" % (queryid)
        cur.execute(sql10)
        rdatavalue = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.rdatavalueEdit.append(rdatavalue)
        sql11 = "SELECT snakorder FROM reference WHERE id = '%s'" % (queryid)
        cur.execute(sql11)
        snakorder = str(cur.fetchall()).replace('\'', '').replace(',', '').replace('(', '').replace(')', '')
        con.commit()
        self.snakorderEdit.append(snakorder)
        end = time.clock()
        ex_time = 'Excute Time:' + str(end - start)
        # print(ex_time)
        self.time.setText(ex_time)


    def clear(self):
        self.searchBar.setText('')
        self.cnlabelsEdit.setText('')
        self.enlabelsEdit.setText('')
        self.descriptionsEdit.setText('')
        self.aliasesEdit.setText('')
        self.propertiesEdit.setText('')
        self.datavalueEdit.setText('')
        self.qhashEdit.setText('')
        self.qdatavalueEdit.setText('')
        self.rhashEdit.setText('')
        self.rdatavalueEdit.setText('')
        self.snakorderEdit.setText('')
        self.time.setText('')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to exit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())