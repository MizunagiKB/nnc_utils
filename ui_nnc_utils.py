# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nnc_utils.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 512)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(480, 360))
        Dialog.setMaximumSize(QtCore.QSize(480, 512))
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 461, 201))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 131))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.cid_src_dir = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cid_src_dir.sizePolicy().hasHeightForWidth())
        self.cid_src_dir.setSizePolicy(sizePolicy)
        self.cid_src_dir.setMinimumSize(QtCore.QSize(0, 0))
        self.cid_src_dir.setSizeIncrement(QtCore.QSize(0, 0))
        self.cid_src_dir.setBaseSize(QtCore.QSize(0, 0))
        self.cid_src_dir.setObjectName("cid_src_dir")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cid_src_dir)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cid_hash = QtWidgets.QComboBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cid_hash.sizePolicy().hasHeightForWidth())
        self.cid_hash.setSizePolicy(sizePolicy)
        self.cid_hash.setObjectName("cid_hash")
        self.cid_hash.addItem("")
        self.cid_hash.addItem("")
        self.cid_hash.addItem("")
        self.cid_hash.addItem("")
        self.cid_hash.addItem("")
        self.cid_hash.addItem("")
        self.cid_hash.addItem("")
        self.cid_hash.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cid_hash)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.cid_hash_size = QtWidgets.QSpinBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cid_hash_size.sizePolicy().hasHeightForWidth())
        self.cid_hash_size.setSizePolicy(sizePolicy)
        self.cid_hash_size.setMinimum(4)
        self.cid_hash_size.setMaximum(16)
        self.cid_hash_size.setProperty("value", 8)
        self.cid_hash_size.setObjectName("cid_hash_size")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cid_hash_size)
        self.cid_select_src_dir = QtWidgets.QPushButton(self.formLayoutWidget)
        self.cid_select_src_dir.setObjectName("cid_select_src_dir")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cid_select_src_dir)
        self.cid_proceed = QtWidgets.QPushButton(self.tab)
        self.cid_proceed.setGeometry(QtCore.QRect(10, 140, 441, 32))
        self.cid_proceed.setObjectName("cid_proceed")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.nnc_log = QtWidgets.QPlainTextEdit(Dialog)
        self.nnc_log.setGeometry(QtCore.QRect(10, 250, 461, 191))
        self.nnc_log.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.nnc_log.setObjectName("nnc_log")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 450, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 220, 461, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.nnc_close = QtWidgets.QPushButton(Dialog)
        self.nnc_close.setGeometry(QtCore.QRect(350, 470, 121, 32))
        self.nnc_close.setObjectName("nnc_close")
        self.actionCIDProceed = QtWidgets.QAction(Dialog)
        self.actionCIDProceed.setObjectName("actionCIDProceed")
        self.actionCIDSelect_src_dir = QtWidgets.QAction(Dialog)
        self.actionCIDSelect_src_dir.setObjectName("actionCIDSelect_src_dir")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.nnc_close.pressed.connect(Dialog.close)
        self.cid_proceed.pressed.connect(self.actionCIDProceed.trigger)
        self.cid_select_src_dir.pressed.connect(self.actionCIDSelect_src_dir.trigger)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NNC Utils"))
        self.label.setText(_translate("Dialog", "Target dir"))
        self.label_2.setText(_translate("Dialog", "Hash"))
        self.cid_hash.setItemText(0, _translate("Dialog", "Average hash"))
        self.cid_hash.setItemText(1, _translate("Dialog", "Perceptual hash"))
        self.cid_hash.setItemText(2, _translate("Dialog", "Perceptual hash (simple)"))
        self.cid_hash.setItemText(3, _translate("Dialog", "Difference hash"))
        self.cid_hash.setItemText(4, _translate("Dialog", "Difference hash (vertical)"))
        self.cid_hash.setItemText(5, _translate("Dialog", "Wavelet hash"))
        self.cid_hash.setItemText(6, _translate("Dialog", "sha1"))
        self.cid_hash.setItemText(7, _translate("Dialog", "md5"))
        self.label_3.setText(_translate("Dialog", "Hash size"))
        self.cid_select_src_dir.setText(_translate("Dialog", "Select target dir"))
        self.cid_proceed.setText(_translate("Dialog", "Proceed"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "chk_image_dup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "gen_image_dataset"))
        self.nnc_close.setText(_translate("Dialog", "Close"))
        self.actionCIDProceed.setText(_translate("Dialog", "CIDProceed"))
        self.actionCIDProceed.setToolTip(_translate("Dialog", "CID Proceed"))
        self.actionCIDSelect_src_dir.setText(_translate("Dialog", "CIDSelect_src_dir"))

