# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_section.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 640)
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(30, 0))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)
        self.label_type_icon = QtWidgets.QLabel(self.tab)
        self.label_type_icon.setMinimumSize(QtCore.QSize(30, 30))
        self.label_type_icon.setObjectName("label_type_icon")
        self.gridLayout_4.addWidget(self.label_type_icon, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(30, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 4, 1, 1)
        self.comboBox_unit = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_unit.sizePolicy().hasHeightForWidth())
        self.comboBox_unit.setSizePolicy(sizePolicy)
        self.comboBox_unit.setMinimumSize(QtCore.QSize(100, 28))
        self.comboBox_unit.setObjectName("comboBox_unit")
        self.gridLayout_4.addWidget(self.comboBox_unit, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 6, 1, 1)
        self.comboBox_type = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_type.sizePolicy().hasHeightForWidth())
        self.comboBox_type.setSizePolicy(sizePolicy)
        self.comboBox_type.setMinimumSize(QtCore.QSize(100, 28))
        self.comboBox_type.setObjectName("comboBox_type")
        self.gridLayout_4.addWidget(self.comboBox_type, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.table_options = QtWidgets.QTableWidget(self.tab)
        self.table_options.setObjectName("table_options")
        self.table_options.setColumnCount(0)
        self.table_options.setRowCount(0)
        self.gridLayout_6.addWidget(self.table_options, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_select_invert = QtWidgets.QPushButton(self.tab)
        self.pushButton_select_invert.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_select_invert.setObjectName("pushButton_select_invert")
        self.gridLayout_3.addWidget(self.pushButton_select_invert, 0, 2, 1, 1)
        self.pushButton_select_all = QtWidgets.QPushButton(self.tab)
        self.pushButton_select_all.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_select_all.setObjectName("pushButton_select_all")
        self.gridLayout_3.addWidget(self.pushButton_select_all, 0, 1, 1, 1)
        self.pushButton_select_clear = QtWidgets.QPushButton(self.tab)
        self.pushButton_select_clear.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_select_clear.setObjectName("pushButton_select_clear")
        self.gridLayout_3.addWidget(self.pushButton_select_clear, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 4, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_ID = QtWidgets.QLineEdit(Form)
        self.lineEdit_ID.setMinimumSize(QtCore.QSize(110, 28))
        self.lineEdit_ID.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.gridLayout_2.addWidget(self.lineEdit_ID, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(40, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_UIName = QtWidgets.QLineEdit(Form)
        self.lineEdit_UIName.setMinimumSize(QtCore.QSize(110, 28))
        self.lineEdit_UIName.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_UIName.setObjectName("lineEdit_UIName")
        self.gridLayout_2.addWidget(self.lineEdit_UIName, 0, 1, 1, 1)
        self.comboBox_ID_type = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_ID_type.sizePolicy().hasHeightForWidth())
        self.comboBox_ID_type.setSizePolicy(sizePolicy)
        self.comboBox_ID_type.setMinimumSize(QtCore.QSize(100, 28))
        self.comboBox_ID_type.setObjectName("comboBox_ID_type")
        self.gridLayout_2.addWidget(self.comboBox_ID_type, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(40, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_5.addWidget(self.line, 2, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_NameDesc = QtWidgets.QLineEdit(Form)
        self.lineEdit_NameDesc.setMinimumSize(QtCore.QSize(110, 28))
        self.lineEdit_NameDesc.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lineEdit_NameDesc.setObjectName("lineEdit_NameDesc")
        self.gridLayout.addWidget(self.lineEdit_NameDesc, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 2, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 0, 3, 1, 1)
        self.pushButton_sure = QtWidgets.QPushButton(Form)
        self.pushButton_sure.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.gridLayout.addWidget(self.pushButton_sure, 0, 4, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "类型"))
        self.label_type_icon.setText(_translate("Form", "icon"))
        self.label_2.setText(_translate("Form", "单位"))
        self.pushButton_select_invert.setText(_translate("Form", "反选"))
        self.pushButton_select_all.setText(_translate("Form", "全选"))
        self.pushButton_select_clear.setText(_translate("Form", "清除选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "从单位仿造"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "从模板新建"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "新建空的"))
        self.label_3.setText(_translate("Form", "注册名"))
        self.label_4.setText(_translate("Form", "注册ID"))
        self.label_5.setText(_translate("Form", "注册类型"))
        self.label_6.setText(_translate("Form", "中文注释（可空）"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
        self.pushButton_sure.setText(_translate("Form", "确定"))
