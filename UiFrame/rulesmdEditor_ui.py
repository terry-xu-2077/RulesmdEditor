# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rulesmdEditor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1064, 485)
        self.gridLayout_10 = QtWidgets.QGridLayout(Form)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_open = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)
        self.pushButton_open.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButton_open.setObjectName("pushButton_open")
        self.gridLayout_6.addWidget(self.pushButton_open, 0, 0, 1, 1)
        self.pushButton_new = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_new.sizePolicy().hasHeightForWidth())
        self.pushButton_new.setSizePolicy(sizePolicy)
        self.pushButton_new.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButton_new.setObjectName("pushButton_new")
        self.gridLayout_6.addWidget(self.pushButton_new, 0, 1, 1, 1)
        self.pushButton_setting = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_setting.sizePolicy().hasHeightForWidth())
        self.pushButton_setting.setSizePolicy(sizePolicy)
        self.pushButton_setting.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.gridLayout_6.addWidget(self.pushButton_setting, 0, 2, 1, 1)
        self.pushButton_save_desc = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_desc.sizePolicy().hasHeightForWidth())
        self.pushButton_save_desc.setSizePolicy(sizePolicy)
        self.pushButton_save_desc.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButton_save_desc.setObjectName("pushButton_save_desc")
        self.gridLayout_6.addWidget(self.pushButton_save_desc, 0, 3, 1, 1)
        self.pushButton_run_game = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_run_game.sizePolicy().hasHeightForWidth())
        self.pushButton_run_game.setSizePolicy(sizePolicy)
        self.pushButton_run_game.setMinimumSize(QtCore.QSize(100, 32))
        self.pushButton_run_game.setObjectName("pushButton_run_game")
        self.gridLayout_6.addWidget(self.pushButton_run_game, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(238, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 5, 1, 1)
        self.pushButton_save_new = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_new.sizePolicy().hasHeightForWidth())
        self.pushButton_save_new.setSizePolicy(sizePolicy)
        self.pushButton_save_new.setMinimumSize(QtCore.QSize(120, 32))
        self.pushButton_save_new.setObjectName("pushButton_save_new")
        self.gridLayout_6.addWidget(self.pushButton_save_new, 0, 6, 1, 1)
        self.line = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 0, 7, 1, 1)
        self.pushButton_save_data = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_data.sizePolicy().hasHeightForWidth())
        self.pushButton_save_data.setSizePolicy(sizePolicy)
        self.pushButton_save_data.setMinimumSize(QtCore.QSize(120, 32))
        self.pushButton_save_data.setObjectName("pushButton_save_data")
        self.gridLayout_6.addWidget(self.pushButton_save_data, 0, 8, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_6, 0, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setMinimumSize(QtCore.QSize(350, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(550, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tree_sections = QtWidgets.QTreeWidget(self.groupBox)
        self.tree_sections.setMinimumSize(QtCore.QSize(300, 200))
        self.tree_sections.setObjectName("tree_sections")
        self.tree_sections.headerItem().setText(0, "1")
        self.gridLayout_9.addWidget(self.tree_sections, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_item_find = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_item_find.sizePolicy().hasHeightForWidth())
        self.label_item_find.setSizePolicy(sizePolicy)
        self.label_item_find.setMaximumSize(QtCore.QSize(40, 40))
        self.label_item_find.setObjectName("label_item_find")
        self.gridLayout.addWidget(self.label_item_find, 0, 0, 1, 1)
        self.lineEdit_item_find = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_item_find.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit_item_find.setObjectName("lineEdit_item_find")
        self.gridLayout.addWidget(self.lineEdit_item_find, 0, 1, 1, 1)
        self.pushButton_item_find = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_item_find.sizePolicy().hasHeightForWidth())
        self.pushButton_item_find.setSizePolicy(sizePolicy)
        self.pushButton_item_find.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_item_find.setObjectName("pushButton_item_find")
        self.gridLayout.addWidget(self.pushButton_item_find, 0, 2, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_9.addWidget(self.line_2, 2, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_item_new = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_item_new.sizePolicy().hasHeightForWidth())
        self.pushButton_item_new.setSizePolicy(sizePolicy)
        self.pushButton_item_new.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_item_new.setObjectName("pushButton_item_new")
        self.gridLayout_8.addWidget(self.pushButton_item_new, 0, 0, 1, 1)
        self.pushButton_item_remove = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_item_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_item_remove.setSizePolicy(sizePolicy)
        self.pushButton_item_remove.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_item_remove.setObjectName("pushButton_item_remove")
        self.gridLayout_8.addWidget(self.pushButton_item_remove, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem1, 0, 2, 1, 1)
        self.pushButton_item_replay = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_item_replay.sizePolicy().hasHeightForWidth())
        self.pushButton_item_replay.setSizePolicy(sizePolicy)
        self.pushButton_item_replay.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_item_replay.setObjectName("pushButton_item_replay")
        self.gridLayout_8.addWidget(self.pushButton_item_replay, 0, 3, 1, 1)
        self.pushButton_item_back = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_item_back.sizePolicy().hasHeightForWidth())
        self.pushButton_item_back.setSizePolicy(sizePolicy)
        self.pushButton_item_back.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_item_back.setObjectName("pushButton_item_back")
        self.gridLayout_8.addWidget(self.pushButton_item_back, 0, 4, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 3, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMinimumSize(QtCore.QSize(600, 300))
        self.widget.setObjectName("widget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_name = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        self.label_name.setMinimumSize(QtCore.QSize(36, 0))
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.checkBox_display_table_box = QtWidgets.QCheckBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_display_table_box.sizePolicy().hasHeightForWidth())
        self.checkBox_display_table_box.setSizePolicy(sizePolicy)
        self.checkBox_display_table_box.setMinimumSize(QtCore.QSize(90, 0))
        self.checkBox_display_table_box.setObjectName("checkBox_display_table_box")
        self.gridLayout_2.addWidget(self.checkBox_display_table_box, 0, 3, 1, 1)
        self.lineEdit_name_desc = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name_desc.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit_name_desc.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEdit_name_desc.setObjectName("lineEdit_name_desc")
        self.gridLayout_2.addWidget(self.lineEdit_name_desc, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(149, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget_edit = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_edit.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_edit.setObjectName("tabWidget_edit")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.table_options = QtWidgets.QTableWidget(self.tab)
        self.table_options.setObjectName("table_options")
        self.table_options.setColumnCount(0)
        self.table_options.setRowCount(0)
        self.gridLayout_5.addWidget(self.table_options, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_optin_find = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_optin_find.sizePolicy().hasHeightForWidth())
        self.label_optin_find.setSizePolicy(sizePolicy)
        self.label_optin_find.setMaximumSize(QtCore.QSize(40, 40))
        self.label_optin_find.setObjectName("label_optin_find")
        self.gridLayout_4.addWidget(self.label_optin_find, 0, 0, 1, 1)
        self.lineEdit_option_find = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_option_find.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit_option_find.setObjectName("lineEdit_option_find")
        self.gridLayout_4.addWidget(self.lineEdit_option_find, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 2, 1, 1)
        self.pushButton_option_new = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_option_new.sizePolicy().hasHeightForWidth())
        self.pushButton_option_new.setSizePolicy(sizePolicy)
        self.pushButton_option_new.setMinimumSize(QtCore.QSize(100, 28))
        self.pushButton_option_new.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_option_new.setObjectName("pushButton_option_new")
        self.gridLayout_4.addWidget(self.pushButton_option_new, 0, 3, 1, 1)
        self.pushButton_option_remove = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_option_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_option_remove.setSizePolicy(sizePolicy)
        self.pushButton_option_remove.setMinimumSize(QtCore.QSize(100, 28))
        self.pushButton_option_remove.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_option_remove.setObjectName("pushButton_option_remove")
        self.gridLayout_4.addWidget(self.pushButton_option_remove, 0, 4, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.tabWidget_edit.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_node = QtWidgets.QFrame(self.tab_2)
        self.frame_node.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_node.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_node.setObjectName("frame_node")
        self.gridLayout_11.addWidget(self.frame_node, 0, 0, 1, 1)
        self.tableWidget_option = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_option.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tableWidget_option.setObjectName("tableWidget_option")
        self.tableWidget_option.setColumnCount(0)
        self.tableWidget_option.setRowCount(0)
        self.gridLayout_11.addWidget(self.tableWidget_option, 0, 1, 1, 1)
        self.tabWidget_edit.addTab(self.tab_2, "")
        self.gridLayout_7.addWidget(self.tabWidget_edit, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.widget, 1, 1, 2, 1)
        self.groupBox_help = QtWidgets.QGroupBox(Form)
        self.groupBox_help.setMinimumSize(QtCore.QSize(350, 0))
        self.groupBox_help.setMaximumSize(QtCore.QSize(550, 200))
        self.groupBox_help.setObjectName("groupBox_help")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_help)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser_help = QtWidgets.QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setObjectName("textBrowser_help")
        self.gridLayout_3.addWidget(self.textBrowser_help, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.groupBox_help, 2, 0, 1, 1)
        self.label_about = QtWidgets.QLabel(Form)
        self.label_about.setObjectName("label_about")
        self.gridLayout_10.addWidget(self.label_about, 3, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget_edit.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_open.setText(_translate("Form", "  打开"))
        self.pushButton_new.setText(_translate("Form", "  新建"))
        self.pushButton_setting.setText(_translate("Form", "  设置"))
        self.pushButton_save_desc.setText(_translate("Form", "  保存描述"))
        self.pushButton_run_game.setText(_translate("Form", "  启动游戏"))
        self.pushButton_save_new.setText(_translate("Form", "  另存为"))
        self.pushButton_save_data.setText(_translate("Form", "  保存修改"))
        self.groupBox.setTitle(_translate("Form", "目录"))
        self.label_item_find.setText(_translate("Form", "icon"))
        self.pushButton_item_find.setText(_translate("Form", "  查找"))
        self.pushButton_item_new.setText(_translate("Form", "  新建项"))
        self.pushButton_item_remove.setText(_translate("Form", "  移除此项"))
        self.pushButton_item_replay.setText(_translate("Form", "  还原此项"))
        self.pushButton_item_back.setText(_translate("Form", "  备份此项"))
        self.label_name.setText(_translate("Form", "名称："))
        self.checkBox_display_table_box.setText(_translate("Form", "表格视图"))
        self.label_optin_find.setText(_translate("Form", "icon"))
        self.pushButton_option_new.setText(_translate("Form", "  新建值"))
        self.pushButton_option_remove.setText(_translate("Form", "  移除此值"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab), _translate("Form", "简单模式"))
        self.tabWidget_edit.setTabText(self.tabWidget_edit.indexOf(self.tab_2), _translate("Form", "专业模式"))
        self.groupBox_help.setTitle(_translate("Form", "提示"))
        self.label_about.setText(_translate("Form", "关于"))
