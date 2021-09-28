from PyQt5 import QtWidgets, QtGui, QtCore
import sys, CreateTables as db
import Dori_olish, Dori_qoshish, Mahsulot_olish, Main, Xodim_qoshish, Xodimlar, Ombor, Dori_tarixi, Dorilar_olish, \
    Qaytarib_berish, Statistika, Sotuv, Sana, Qoshish, Sotish, Sotuv_tarixi

conn = db.conn
cur = db.cur


class Window(QtWidgets.QMainWindow, Main.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showMaximized()
        self.pushButton.clicked.connect(lambda: self.openWindowFun(1))
        self.pushButton_2.clicked.connect(lambda: self.openWindowFun(2))
        self.pushButton_3.clicked.connect(lambda: self.openWindowFun(3))
        self.pushButton_4.clicked.connect(lambda: self.openWindowFun(5))
        self.pushButton_5.clicked.connect(lambda: self.openWindowFun(6))
        self.pushButton_6.clicked.connect(lambda: self.openWindowFun(7))
        self.pushButton_7.clicked.connect(lambda: self.openWindowFun(4))

    def openWindowFun(self, index):
        if index == 1:
            self.oyna = Window_ombor()
        elif index == 2:
            self.oyna = Window_sotuv()
        elif index == 3:
            self.oyna = Window_mahsulot_olish()
        elif index == 4:
            self.oyna = Window_statistika()
        elif index == 5:
            self.oyna = Window_sotuv_tarixi()
        elif index == 6:
            self.oyna = Window_xodimlar()
        else:
            self.oyna = Window_qaytarib_berish()
        self.oyna.showMaximized()
        self.hide()


class Window_ombor(QtWidgets.QWidget, Ombor.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.qoshish_fun)
        self.pushButton_3.clicked.connect(lambda: self.openWindowFun(1))
        self.pushButton_4.clicked.connect(lambda: self.openWindowFun(2))
        self.pushButton_5.clicked.connect(lambda: self.openWindowFun(3))
        self.pushButton_6.clicked.connect(lambda: self.openWindowFun(4))
        self.pushButton_7.clicked.connect(lambda: self.openWindowFun(5))
        self.pushButton_10.clicked.connect(lambda: self.openWindowFun(6))
        self.pushButton_9.clicked.connect(lambda: self.openWindowFun(7))
        self.dorilar()

    def dorilar(self):
        i = self.lineEdit.text()
        cur.execute("select * from kashalog where dori_nomi like ?", ('%' + i + '%',))
        rows = cur.fetchall()
        t = self.tableWidget_2
        itm = QtWidgets.QTableWidgetItem
        t.setRowCount(len(rows))
        for i, d in enumerate(rows):
            t.setItem(i, 0, itm(str(d[1])))
            t.setItem(i, 1, itm(str(d[2])))
            t.setItem(i, 2, itm(str(d[3])))
            t.setItem(i, 3, itm(str(d[4])))
            t.setItem(i, 4, itm(str(d[5])))




    def qoshish_fun(self):
        self.oynacha = Window_dori_qoshish()
        self.oynacha.show()
        self.oynacha.qoshishyakuni.connect(self.dorilar)


    def openWindowFun(self, index):
        if index == 1:
            self.oyna = Window_ombor()
        elif index == 2:
            self.oyna = Window_sotuv()
        elif index == 3:
            self.oyna = Window_mahsulot_olish()
        elif index == 4:
            self.oyna = Window_statistika()
        elif index == 5:
            self.oyna = Window_sotuv_tarixi()
        elif index == 6:
            self.oyna = Window_xodimlar()
        else:
            self.oyna = Window_qaytarib_berish()
        self.oyna.showMaximized()
        self.close()


class Window_dori_qoshish(QtWidgets.QDialog, Dori_qoshish.Ui_Form):

    qoshishyakuni = QtCore.pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('./image/plus (1).png'))
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.add_data)

    def close(self):
        self.hide()

    def add_data(self):
        name = self.lineEdit.text()
        dona = self.lineEdit_2.text()
        sotilish_narx = self.lineEdit_3.text()
        barcode = self.lineEdit_5.text()
        qoshimcha = self.textEdit.toPlainText()

        cur.execute("insert into kashalog(dori_nomi, pachka_soni, narx, barcode, qoshimcha) VALUES (?,?,?,?,?)",
                    (name, dona, sotilish_narx, barcode, qoshimcha))
        conn.commit()
        self.qoshishyakuni.emit(1)
        self.close()


class Window_sotuv(QtWidgets.QWidget, Sotuv.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_12.clicked.connect(lambda: self.openWindowFun(1))
        self.pushButton_13.clicked.connect(lambda: self.openWindowFun(2))
        self.pushButton_14.clicked.connect(lambda: self.openWindowFun(3))
        self.pushButton_15.clicked.connect(lambda: self.openWindowFun(4))
        self.pushButton_16.clicked.connect(lambda: self.openWindowFun(5))
        self.pushButton_17.clicked.connect(lambda: self.openWindowFun(6))
        self.pushButton_19.clicked.connect(lambda: self.openWindowFun(7))
        self.pushButton.clicked.connect(self.qoshish_fun)
        self.pushButton_21.clicked.connect(self.sotish_fun)

    def openWindowFun(self, index):
        if index == 1:
            self.oyna = Window_ombor()
        elif index == 2:
            self.oyna = Window_sotuv()
        elif index == 3:
            self.oyna = Window_mahsulot_olish()
        elif index == 4:
            self.oyna = Window_statistika()
        elif index == 5:
            self.oyna = Window_sotuv_tarixi()
        elif index == 6:
            self.oyna = Window_xodimlar()
        else:
            self.oyna = Window_qaytarib_berish()
        self.oyna.showMaximized()
        self.close()

    def qoshish_fun(self):
        self.oynacha = Window_qoshish()
        self.oynacha.show()

    def sotish_fun(self):
        self.oynacha = Window_sotish()
        self.oynacha.show()


class Window_qoshish(QtWidgets.QDialog, Qoshish.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.add_data)

    def close(self):
        self.hide()

    def add_data(self):
        self.hide()
        # self.setGeometry(700, 100, 100, 100)


class Window_sotish(QtWidgets.QDialog, Sotish.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.add_data)

    def close(self):
        self.hide()

    def add_data(self):
        self.hide()
        # self.setGeometry(700, 100, 100, 100)


class Window_mahsulot_olish(QtWidgets.QWidget, Mahsulot_olish.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.add)
        self.pushButton_3.clicked.connect(lambda: self.openWindowFun(1))
        self.pushButton_4.clicked.connect(lambda: self.openWindowFun(2))
        self.pushButton_5.clicked.connect(lambda: self.openWindowFun(3))
        self.pushButton_6.clicked.connect(lambda: self.openWindowFun(4))
        self.pushButton_7.clicked.connect(lambda: self.openWindowFun(5))
        self.pushButton_10.clicked.connect(lambda: self.openWindowFun(6))
        self.pushButton_9.clicked.connect(lambda: self.openWindowFun(7))

    def openWindowFun(self, index):
        if index == 1:
            self.oyna = Window_ombor()
        elif index == 2:
            self.oyna = Window_sotuv()
        elif index == 3:
            self.oyna = Window_mahsulot_olish()
        elif index == 4:
            self.oyna = Window_statistika()
        elif index == 5:
            self.oyna = Window_sotuv_tarixi()
        elif index == 6:
            self.oyna = Window_xodimlar()
        else:
            self.oyna = Window_qaytarib_berish()
        self.oyna.showMaximized()
        self.close()

    def add(self):
        self.oynacha = Window_dori_olish()
        self.oynacha.show()


class Window_dori_olish(QtWidgets.QWidget, Dori_olish.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.add)

    def close(self):
        self.hide()

    def add(self):
        self.hide()


class Window_statistika(QtWidgets.QWidget, Statistika.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_12.clicked.connect(lambda: self.openWindowFun(1))
        self.pushButton_13.clicked.connect(lambda: self.openWindowFun(2))
        self.pushButton_14.clicked.connect(lambda: self.openWindowFun(3))
        self.pushButton_15.clicked.connect(lambda: self.openWindowFun(4))
        self.pushButton_16.clicked.connect(lambda: self.openWindowFun(5))
        self.pushButton_17.clicked.connect(lambda: self.openWindowFun(6))
        self.pushButton_19.clicked.connect(lambda: self.openWindowFun(7))

    def openWindowFun(self, index):
        if index == 1:
            self.oyna = Window_ombor()
        elif index == 2:
            self.oyna = Window_sotuv()
        elif index == 3:
            self.oyna = Window_mahsulot_olish()
        elif index == 4:
            self.oyna = Window_statistika()
        elif index == 5:
            self.oyna = Window_sotuv_tarixi()
        elif index == 6:
            self.oyna = Window_xodimlar()
        else:
            self.oyna = Window_qaytarib_berish()
        self.oyna.showMaximized()
        self.close()


class Window_sotuv_tarixi(QtWidgets.QWidget, Sotuv_tarixi.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.startDate)
        self.pushButton_2.clicked.connect(self.endDate)
        self.pushButton_12.clicked.connect(lambda: self.openWindowFun(1))
        self.pushButton_13.clicked.connect(lambda: self.openWindowFun(2))
        self.pushButton_14.clicked.connect(lambda: self.openWindowFun(3))
        self.pushButton_15.clicked.connect(lambda: self.openWindowFun(4))
        self.pushButton_16.clicked.connect(lambda: self.openWindowFun(5))
        self.pushButton_17.clicked.connect(lambda: self.openWindowFun(6))
        self.pushButton_19.clicked.connect(lambda: self.openWindowFun(7))

    def startDate(self):
        self.oynacha = Window_sana()
        self.oynacha.show()

    def endDate(self):
        self.oynacha = Window_sana()
        self.oynacha.show()

    def openWindowFun(self, index):
        if index == 1:
            self.oyna = Window_ombor()
        elif index == 2:
            self.oyna = Window_sotuv()
        elif index == 3:
            self.oyna = Window_mahsulot_olish()
        elif index == 4:
            self.oyna = Window_statistika()
        elif index == 5:
            self.oyna = Window_sotuv_tarixi()
        elif index == 6:
            self.oyna = Window_xodimlar()
        else:
            self.oyna = Window_qaytarib_berish()
        self.oyna.showMaximized()
        self.close()


class Window_sana(QtWidgets.QDialog, Sana.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.add)

    def close(self):
        self.hide()

    def add(self):
        self.hide()


class Window_xodimlar(QtWidgets.QWidget, Xodimlar.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.xodimQoshish)
        self.pushButton_12.clicked.connect(lambda: self.openWindowFun(1))
        self.pushButton_13.clicked.connect(lambda: self.openWindowFun(2))
        self.pushButton_14.clicked.connect(lambda: self.openWindowFun(3))
        self.pushButton_15.clicked.connect(lambda: self.openWindowFun(4))
        self.pushButton_16.clicked.connect(lambda: self.openWindowFun(5))
        self.pushButton_17.clicked.connect(lambda: self.openWindowFun(6))
        self.pushButton_19.clicked.connect(lambda: self.openWindowFun(7))

    def openWindowFun(self, index):
        if index == 1:
            self.oyna = Window_ombor()
        elif index == 2:
            self.oyna = Window_sotuv()
        elif index == 3:
            self.oyna = Window_mahsulot_olish()
        elif index == 4:
            self.oyna = Window_statistika()
        elif index == 5:
            self.oyna = Window_sotuv_tarixi()
        elif index == 6:
            self.oyna = Window_xodimlar()
        else:
            self.oyna = Window_qaytarib_berish()
        self.oyna.showMaximized()
        self.close()

    def xodimQoshish(self):
        self.oynacha = Window_xodim_qoshish()
        self.oynacha.show()


class Window_xodim_qoshish(QtWidgets.QDialog, Xodim_qoshish.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.add_data)
        self.pushButton_3.clicked.connect(self.add)

    def close(self):
        self.hide()

    def add_data(self):
        self.hide()

    def add(self):
        self.lineEdit_6.setText(self.lineEdit_6.text() + ', ')


class Window_qaytarib_berish(QtWidgets.QWidget, Qaytarib_berish.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_12.clicked.connect(lambda: self.openWindowFun(1))
        self.pushButton_13.clicked.connect(lambda: self.openWindowFun(2))
        self.pushButton_14.clicked.connect(lambda: self.openWindowFun(3))
        self.pushButton_15.clicked.connect(lambda: self.openWindowFun(4))
        self.pushButton_16.clicked.connect(lambda: self.openWindowFun(5))
        self.pushButton_17.clicked.connect(lambda: self.openWindowFun(6))
        self.pushButton_19.clicked.connect(lambda: self.openWindowFun(7))

    def openWindowFun(self, index):
        if index == 1:
            self.oyna = Window_ombor()
        elif index == 2:
            self.oyna = Window_sotuv()
        elif index == 3:
            self.oyna = Window_mahsulot_olish()
        elif index == 4:
            self.oyna = Window_statistika()
        elif index == 5:
            self.oyna = Window_sotuv_tarixi()
        elif index == 6:
            self.oyna = Window_xodimlar()
        else:
            self.oyna = Window_qaytarib_berish()
        self.oyna.showMaximized()
        self.close()


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    # window.show()
    sys.exit(App.exec())
