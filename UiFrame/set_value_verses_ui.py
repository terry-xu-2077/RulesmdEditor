# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'set_value_verses.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(714, 250)
        self.gridLayout_4 = QtWidgets.QGridLayout(Form)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.gridLayout_25 = QtWidgets.QGridLayout()
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.verticalSlider_1 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_1.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_1.setMaximum(100)
        self.verticalSlider_1.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_1.setObjectName("verticalSlider_1")
        self.gridLayout_2.addWidget(self.verticalSlider_1, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.spinBox_1 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_1.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_1.setMaximum(1000)
        self.spinBox_1.setObjectName("spinBox_1")
        self.gridLayout_3.addWidget(self.spinBox_1, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout_3.addWidget(self.label_1, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalSlider_2 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_2.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_2.setMaximum(100)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout_6.addWidget(self.verticalSlider_2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_5.addWidget(self.spinBox_2, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 0, 0, 1, 1)
        self.verticalSlider_3 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_3.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_3.setMaximum(100)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.gridLayout_8.addWidget(self.verticalSlider_3, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_3.setMaximum(1000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.gridLayout_7.addWidget(self.spinBox_3, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_7, 0, 2, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        spacerItem6 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem6, 0, 0, 1, 1)
        self.verticalSlider_4 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_4.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_4.setMaximum(100)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.gridLayout_10.addWidget(self.verticalSlider_4, 0, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem7, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.spinBox_4 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_4.setMaximum(1000)
        self.spinBox_4.setObjectName("spinBox_4")
        self.gridLayout_9.addWidget(self.spinBox_4, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_9, 0, 3, 1, 1)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem8, 0, 0, 1, 1)
        self.verticalSlider_5 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_5.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_5.setMaximum(100)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.gridLayout_12.addWidget(self.verticalSlider_5, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem9, 0, 2, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_12, 0, 0, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_5.setMaximum(1000)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout_11.addWidget(self.spinBox_5, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_11.addWidget(self.label_5, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_11, 0, 4, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem10, 0, 0, 1, 1)
        self.verticalSlider_6 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_6.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_6.setMaximum(100)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.gridLayout_14.addWidget(self.verticalSlider_6, 0, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem11, 0, 2, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_6.setMaximum(1000)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_13.addWidget(self.spinBox_6, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_13.addWidget(self.label_6, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_13, 0, 5, 1, 1)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem12 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem12, 0, 0, 1, 1)
        self.verticalSlider_7 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_7.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_7.setMaximum(100)
        self.verticalSlider_7.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_7.setObjectName("verticalSlider_7")
        self.gridLayout_16.addWidget(self.verticalSlider_7, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem13, 0, 2, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_16, 0, 0, 1, 1)
        self.spinBox_7 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_7.setMaximum(1000)
        self.spinBox_7.setObjectName("spinBox_7")
        self.gridLayout_15.addWidget(self.spinBox_7, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_15.addWidget(self.label_7, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_15, 0, 6, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        spacerItem14 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem14, 0, 0, 1, 1)
        self.verticalSlider_8 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_8.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_8.setMaximum(100)
        self.verticalSlider_8.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_8.setObjectName("verticalSlider_8")
        self.gridLayout_18.addWidget(self.verticalSlider_8, 0, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem15, 0, 2, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_18, 0, 0, 1, 1)
        self.spinBox_8 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_8.setMaximum(1000)
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout_17.addWidget(self.spinBox_8, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_17.addWidget(self.label_8, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_17, 0, 7, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        spacerItem16 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem16, 0, 0, 1, 1)
        self.verticalSlider_9 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_9.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_9.setMaximum(100)
        self.verticalSlider_9.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_9.setObjectName("verticalSlider_9")
        self.gridLayout_20.addWidget(self.verticalSlider_9, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem17, 0, 2, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.spinBox_9 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_9.setMaximum(1000)
        self.spinBox_9.setObjectName("spinBox_9")
        self.gridLayout_19.addWidget(self.spinBox_9, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_19.addWidget(self.label_9, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_19, 0, 8, 1, 1)
        self.gridLayout_21 = QtWidgets.QGridLayout()
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.gridLayout_22 = QtWidgets.QGridLayout()
        self.gridLayout_22.setObjectName("gridLayout_22")
        spacerItem18 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem18, 0, 0, 1, 1)
        self.verticalSlider_10 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_10.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_10.setMaximum(100)
        self.verticalSlider_10.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_10.setObjectName("verticalSlider_10")
        self.gridLayout_22.addWidget(self.verticalSlider_10, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem19, 0, 2, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_22, 0, 0, 1, 1)
        self.spinBox_10 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_10.setMaximum(1000)
        self.spinBox_10.setObjectName("spinBox_10")
        self.gridLayout_21.addWidget(self.spinBox_10, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_21.addWidget(self.label_10, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_21, 0, 9, 1, 1)
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_24 = QtWidgets.QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        spacerItem20 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem20, 0, 0, 1, 1)
        self.verticalSlider_11 = QtWidgets.QSlider(self.widget)
        self.verticalSlider_11.setMinimumSize(QtCore.QSize(0, 120))
        self.verticalSlider_11.setMaximum(100)
        self.verticalSlider_11.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_11.setObjectName("verticalSlider_11")
        self.gridLayout_24.addWidget(self.verticalSlider_11, 0, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem21, 0, 2, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_24, 0, 0, 1, 1)
        self.spinBox_11 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_11.setMaximum(1000)
        self.spinBox_11.setObjectName("spinBox_11")
        self.gridLayout_23.addWidget(self.spinBox_11, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_23.addWidget(self.label_11, 2, 0, 1, 1)
        self.gridLayout_25.addLayout(self.gridLayout_23, 0, 10, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_25, 0, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(178, 39, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem22, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem23, 0, 0, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 0, 1, 1, 1)
        self.pushButton_sure = QtWidgets.QPushButton(self.widget)
        self.pushButton_sure.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton_sure.setObjectName("pushButton_sure")
        self.gridLayout.addWidget(self.pushButton_sure, 0, 2, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.verticalSlider_1.valueChanged['int'].connect(self.spinBox_1.setValue)
        self.verticalSlider_2.valueChanged['int'].connect(self.spinBox_2.setValue)
        self.verticalSlider_3.valueChanged['int'].connect(self.spinBox_3.setValue)
        self.verticalSlider_4.valueChanged['int'].connect(self.spinBox_4.setValue)
        self.verticalSlider_5.valueChanged['int'].connect(self.spinBox_5.setValue)
        self.verticalSlider_6.valueChanged['int'].connect(self.spinBox_6.setValue)
        self.verticalSlider_7.valueChanged['int'].connect(self.spinBox_7.setValue)
        self.verticalSlider_8.valueChanged['int'].connect(self.spinBox_8.setValue)
        self.verticalSlider_9.valueChanged['int'].connect(self.spinBox_9.setValue)
        self.verticalSlider_10.valueChanged['int'].connect(self.spinBox_10.setValue)
        self.verticalSlider_11.valueChanged['int'].connect(self.spinBox_11.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_1.setText(_translate("Form", "无装甲"))
        self.label_2.setText(_translate("Form", "布质"))
        self.label_3.setText(_translate("Form", "铁质"))
        self.label_4.setText(_translate("Form", "金属"))
        self.label_5.setText(_translate("Form", "中型"))
        self.label_6.setText(_translate("Form", "重型"))
        self.label_7.setText(_translate("Form", "木质"))
        self.label_8.setText(_translate("Form", "钢铁"))
        self.label_9.setText(_translate("Form", "混凝土"))
        self.label_10.setText(_translate("Form", "特殊1"))
        self.label_11.setText(_translate("Form", "特殊2"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))
        self.pushButton_sure.setText(_translate("Form", "确定"))
