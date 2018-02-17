# -*- coding: utf-8 -*-
# ------------------------------------------------------------------ import(s)
import sys
import os

import imagehash

import PyQt5
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtSvg
import PyQt5.QtWidgets

import ui_nnc_utils

import chk_image_dup


# ------------------------------------------------------------------- class(s)
class CMainWindow(PyQt5.QtWidgets.QMainWindow):

    def __init__(self):
        super(CMainWindow, self).__init__()

        self.ui = ui_nnc_utils.Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.actionCIDSelect_src_dir.triggered.connect(self.actionCIDSelect_src_dir)
        self.ui.actionCIDProceed.triggered.connect(self.actionCIDProceed)

    def cb_log(self, msg):

        self.ui.nnc_log.appendPlainText(msg)

    def actionCIDSelect_src_dir(self):

        o = PyQt5.QtWidgets.QFileDialog()
        src_dir = o.getExistingDirectory(
            self,
            "Choose dir", os.getcwd(),
            options=PyQt5.QtWidgets.QFileDialog.DontResolveSymlinks | PyQt5.QtWidgets.QFileDialog.ShowDirsOnly
        )

        if len(src_dir) > 0:
            self.ui.cid_src_dir.setText(src_dir)

    def actionCIDProceed(self):

        dic_hash_function = {
            "Average hash": imagehash.average_hash,
            "Perceptual hash": imagehash.phash,
            "Perceptual hash (simple)": imagehash.phash_simple,
            "Difference hash": imagehash.dhash,
            "Difference hash (vertical)": imagehash.dhash_vertical,
            "Wavelet hash": imagehash.whash,
        }

        if len(self.ui.cid_src_dir.text()) == 0:
            PyQt5.QtWidgets.QErrorMessage(self).showMessage(
                "Target dir empty"
            )

        if self.ui.cid_hash.currentText() not in dic_hash_function:
            PyQt5.QtWidgets.QErrorMessage(self).showMessage(
                "Undefined hash %s" % self.ui.cid_hash.currentText()
            )

        self.ui.nnc_log.clear()

        chk_image_dup.proceed(
            self.ui.cid_src_dir.text(),
            dic_hash_function[self.ui.cid_hash.currentText()],
            self.ui.cid_hash_size.value(),
            self.cb_log
        )


# ---------------------------------------------------------------- function(s)
# ============================================================================
def main():

    oCApp = PyQt5.QtWidgets.QApplication(sys.argv)

    oCMain = CMainWindow()
    oCMain.show()

    return(oCApp.exec_())


if(__name__ == '__main__'):
    sys.exit(main())



# [EOF]
