# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1292, 538)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(440, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(600, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_9.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.tree_sections = QtWidgets.QTreeWidget(self.groupBox)
        self.tree_sections.setMinimumSize(QtCore.QSize(300, 200))
        self.tree_sections.setObjectName("tree_sections")
        self.tree_sections.headerItem().setText(0, "1")
        self.gridLayout_9.addWidget(self.tree_sections, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_section_find = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_section_find.sizePolicy().hasHeightForWidth())
        self.pushButton_section_find.setSizePolicy(sizePolicy)
        self.pushButton_section_find.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_section_find.setObjectName("pushButton_section_find")
        self.gridLayout.addWidget(self.pushButton_section_find, 0, 6, 1, 2)
        self.label_item_find = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_item_find.sizePolicy().hasHeightForWidth())
        self.label_item_find.setSizePolicy(sizePolicy)
        self.label_item_find.setMinimumSize(QtCore.QSize(30, 30))
        self.label_item_find.setObjectName("label_item_find")
        self.gridLayout.addWidget(self.label_item_find, 0, 0, 1, 1)
        self.comboBox_section_find = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_section_find.sizePolicy().hasHeightForWidth())
        self.comboBox_section_find.setSizePolicy(sizePolicy)
        self.comboBox_section_find.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox_section_find.setObjectName("comboBox_section_find")
        self.gridLayout.addWidget(self.comboBox_section_find, 0, 1, 1, 1)
        self.lineEdit_item_find = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_item_find.sizePolicy().hasHeightForWidth())
        self.lineEdit_item_find.setSizePolicy(sizePolicy)
        self.lineEdit_item_find.setObjectName("lineEdit_item_find")
        self.gridLayout.addWidget(self.lineEdit_item_find, 0, 3, 1, 1)
        self.checkBox_display_find = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_display_find.setObjectName("checkBox_display_find")
        self.gridLayout.addWidget(self.checkBox_display_find, 0, 4, 1, 2)
        self.gridLayout_9.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_9.addWidget(self.line_2, 2, 0, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setSpacing(4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_section_add = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_section_add.sizePolicy().hasHeightForWidth())
        self.pushButton_section_add.setSizePolicy(sizePolicy)
        self.pushButton_section_add.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_section_add.setObjectName("pushButton_section_add")
        self.gridLayout_8.addWidget(self.pushButton_section_add, 0, 0, 1, 1)
        self.pushButton_section_remove = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_section_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_section_remove.setSizePolicy(sizePolicy)
        self.pushButton_section_remove.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_section_remove.setObjectName("pushButton_section_remove")
        self.gridLayout_8.addWidget(self.pushButton_section_remove, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 2, 1, 1)
        self.pushButton_section_replay = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_section_replay.sizePolicy().hasHeightForWidth())
        self.pushButton_section_replay.setSizePolicy(sizePolicy)
        self.pushButton_section_replay.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_section_replay.setObjectName("pushButton_section_replay")
        self.gridLayout_8.addWidget(self.pushButton_section_replay, 0, 3, 1, 1)
        self.pushButton_section_back = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_section_back.sizePolicy().hasHeightForWidth())
        self.pushButton_section_back.setSizePolicy(sizePolicy)
        self.pushButton_section_back.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_section_back.setObjectName("pushButton_section_back")
        self.gridLayout_8.addWidget(self.pushButton_section_back, 0, 4, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 3, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 1, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_save_new = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_new.sizePolicy().hasHeightForWidth())
        self.pushButton_save_new.setSizePolicy(sizePolicy)
        self.pushButton_save_new.setMinimumSize(QtCore.QSize(120, 32))
        self.pushButton_save_new.setObjectName("pushButton_save_new")
        self.gridLayout_6.addWidget(self.pushButton_save_new, 0, 9, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 0, 5, 1, 1)
        self.pushButton_save_data = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_data.sizePolicy().hasHeightForWidth())
        self.pushButton_save_data.setSizePolicy(sizePolicy)
        self.pushButton_save_data.setMinimumSize(QtCore.QSize(120, 32))
        self.pushButton_save_data.setObjectName("pushButton_save_data")
        self.gridLayout_6.addWidget(self.pushButton_save_data, 0, 10, 1, 1)
        self.pushButton_open = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)
        self.pushButton_open.setMinimumSize(QtCore.QSize(110, 32))
        self.pushButton_open.setObjectName("pushButton_open")
        self.gridLayout_6.addWidget(self.pushButton_open, 0, 0, 1, 1)
        self.pushButton_save_desc = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_desc.sizePolicy().hasHeightForWidth())
        self.pushButton_save_desc.setSizePolicy(sizePolicy)
        self.pushButton_save_desc.setMinimumSize(QtCore.QSize(110, 32))
        self.pushButton_save_desc.setObjectName("pushButton_save_desc")
        self.gridLayout_6.addWidget(self.pushButton_save_desc, 0, 2, 1, 1)
        self.pushButton_rules_global = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rules_global.sizePolicy().hasHeightForWidth())
        self.pushButton_rules_global.setSizePolicy(sizePolicy)
        self.pushButton_rules_global.setMinimumSize(QtCore.QSize(110, 32))
        self.pushButton_rules_global.setObjectName("pushButton_rules_global")
        self.gridLayout_6.addWidget(self.pushButton_rules_global, 0, 6, 1, 1)
        self.pushButton_new = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_new.sizePolicy().hasHeightForWidth())
        self.pushButton_new.setSizePolicy(sizePolicy)
        self.pushButton_new.setMinimumSize(QtCore.QSize(110, 32))
        self.pushButton_new.setObjectName("pushButton_new")
        self.gridLayout_6.addWidget(self.pushButton_new, 0, 1, 1, 1)
        self.pushButton_run_game = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_run_game.sizePolicy().hasHeightForWidth())
        self.pushButton_run_game.setSizePolicy(sizePolicy)
        self.pushButton_run_game.setMinimumSize(QtCore.QSize(110, 32))
        self.pushButton_run_game.setObjectName("pushButton_run_game")
        self.gridLayout_6.addWidget(self.pushButton_run_game, 0, 7, 1, 2)
        self.pushButton_setting = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_setting.sizePolicy().hasHeightForWidth())
        self.pushButton_setting.setSizePolicy(sizePolicy)
        self.pushButton_setting.setMinimumSize(QtCore.QSize(110, 32))
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.gridLayout_6.addWidget(self.pushButton_setting, 0, 3, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 2)
        self.label_about = QtWidgets.QLabel(self.centralwidget)
        self.label_about.setObjectName("label_about")
        self.gridLayout_7.addWidget(self.label_about, 3, 0, 1, 1)
        self.groupBox_help = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_help.setMinimumSize(QtCore.QSize(440, 0))
        self.groupBox_help.setMaximumSize(QtCore.QSize(600, 200))
        self.groupBox_help.setObjectName("groupBox_help")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_help)
        self.gridLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser_help = QtWidgets.QTextBrowser(self.groupBox_help)
        self.textBrowser_help.setObjectName("textBrowser_help")
        self.gridLayout_3.addWidget(self.textBrowser_help, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_help, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_display_table_box = QtWidgets.QCheckBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_display_table_box.sizePolicy().hasHeightForWidth())
        self.checkBox_display_table_box.setSizePolicy(sizePolicy)
        self.checkBox_display_table_box.setMinimumSize(QtCore.QSize(70, 28))
        self.checkBox_display_table_box.setObjectName("checkBox_display_table_box")
        self.gridLayout_2.addWidget(self.checkBox_display_table_box, 0, 8, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(10, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.label_type_icon = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_type_icon.sizePolicy().hasHeightForWidth())
        self.label_type_icon.setSizePolicy(sizePolicy)
        self.label_type_icon.setMinimumSize(QtCore.QSize(28, 28))
        self.label_type_icon.setObjectName("label_type_icon")
        self.gridLayout_2.addWidget(self.label_type_icon, 0, 0, 1, 1)
        self.lineEdit_name_desc = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_name_desc.sizePolicy().hasHeightForWidth())
        self.lineEdit_name_desc.setSizePolicy(sizePolicy)
        self.lineEdit_name_desc.setMinimumSize(QtCore.QSize(40, 0))
        self.lineEdit_name_desc.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_name_desc.setObjectName("lineEdit_name_desc")
        self.gridLayout_2.addWidget(self.lineEdit_name_desc, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 13, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 3, 1, 1)
        self.label_sectionName = QtWidgets.QLabel(self.groupBox_2)
        self.label_sectionName.setMinimumSize(QtCore.QSize(40, 0))
        self.label_sectionName.setStyleSheet("color: rgb(255, 85, 0);")
        self.label_sectionName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_sectionName.setObjectName("label_sectionName")
        self.gridLayout_2.addWidget(self.label_sectionName, 0, 4, 1, 2)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.pushButton_jump_left = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_jump_left.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton_jump_left.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 85, 0);\n"
"    text-decoration:underline;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_jump_left.setObjectName("pushButton_jump_left")
        self.gridLayout_11.addWidget(self.pushButton_jump_left, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy)
        self.line_4.setMinimumSize(QtCore.QSize(10, 22))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_11.addWidget(self.line_4, 0, 1, 1, 1)
        self.pushButton_jump_right = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_jump_right.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton_jump_right.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_jump_right.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"    color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 85, 0);\n"
"    text-decoration:underline;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"    color: rgb(170, 0, 0);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    color: rgb(100, 100, 100);\n"
"}")
        self.pushButton_jump_right.setObjectName("pushButton_jump_right")
        self.gridLayout_11.addWidget(self.pushButton_jump_right, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_11, 0, 6, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.table_options = QtWidgets.QTableWidget(self.widget_2)
        self.table_options.setObjectName("table_options")
        self.table_options.setColumnCount(0)
        self.table_options.setRowCount(0)
        self.gridLayout_5.addWidget(self.table_options, 1, 0, 1, 1)
        self.gridLayout_13.addWidget(self.widget_2, 1, 0, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_optin_find = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_optin_find.sizePolicy().hasHeightForWidth())
        self.label_optin_find.setSizePolicy(sizePolicy)
        self.label_optin_find.setMinimumSize(QtCore.QSize(30, 30))
        self.label_optin_find.setObjectName("label_optin_find")
        self.gridLayout_10.addWidget(self.label_optin_find, 0, 0, 1, 1)
        self.comboBox_option_find = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_option_find.sizePolicy().hasHeightForWidth())
        self.comboBox_option_find.setSizePolicy(sizePolicy)
        self.comboBox_option_find.setMinimumSize(QtCore.QSize(80, 0))
        self.comboBox_option_find.setObjectName("comboBox_option_find")
        self.gridLayout_10.addWidget(self.comboBox_option_find, 0, 1, 1, 1)
        self.lineEdit_option_find = QtWidgets.QLineEdit(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_option_find.sizePolicy().hasHeightForWidth())
        self.lineEdit_option_find.setSizePolicy(sizePolicy)
        self.lineEdit_option_find.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_option_find.setObjectName("lineEdit_option_find")
        self.gridLayout_10.addWidget(self.lineEdit_option_find, 0, 2, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_option_reset = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_option_reset.sizePolicy().hasHeightForWidth())
        self.pushButton_option_reset.setSizePolicy(sizePolicy)
        self.pushButton_option_reset.setMinimumSize(QtCore.QSize(100, 28))
        self.pushButton_option_reset.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_option_reset.setObjectName("pushButton_option_reset")
        self.gridLayout_4.addWidget(self.pushButton_option_reset, 0, 0, 1, 1)
        self.pushButton_option_add = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_option_add.sizePolicy().hasHeightForWidth())
        self.pushButton_option_add.setSizePolicy(sizePolicy)
        self.pushButton_option_add.setMinimumSize(QtCore.QSize(100, 28))
        self.pushButton_option_add.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_option_add.setObjectName("pushButton_option_add")
        self.gridLayout_4.addWidget(self.pushButton_option_add, 0, 1, 1, 1)
        self.pushButton_option_remove = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_option_remove.sizePolicy().hasHeightForWidth())
        self.pushButton_option_remove.setSizePolicy(sizePolicy)
        self.pushButton_option_remove.setMinimumSize(QtCore.QSize(100, 28))
        self.pushButton_option_remove.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_option_remove.setObjectName("pushButton_option_remove")
        self.gridLayout_4.addWidget(self.pushButton_option_remove, 0, 2, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_4, 0, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem5, 0, 1, 1, 2)
        self.gridLayout_13.addLayout(self.gridLayout_12, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_2, 1, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "目录"))
        self.pushButton_section_find.setText(_translate("MainWindow", "  查找更多"))
        self.label_item_find.setText(_translate("MainWindow", "icon"))
        self.checkBox_display_find.setText(_translate("MainWindow", "独显搜索结果"))
        self.pushButton_section_add.setText(_translate("MainWindow", " 新建单位"))
        self.pushButton_section_remove.setText(_translate("MainWindow", " 移除此项"))
        self.pushButton_section_replay.setText(_translate("MainWindow", " 还原此项"))
        self.pushButton_section_back.setText(_translate("MainWindow", " 备份此项"))
        self.pushButton_save_new.setText(_translate("MainWindow", "  另存为"))
        self.pushButton_save_data.setText(_translate("MainWindow", "  保存修改"))
        self.pushButton_open.setText(_translate("MainWindow", " 打开规则"))
        self.pushButton_save_desc.setText(_translate("MainWindow", " 保存描述"))
        self.pushButton_rules_global.setText(_translate("MainWindow", " 全局设置"))
        self.pushButton_new.setText(_translate("MainWindow", " 新建规则"))
        self.pushButton_run_game.setText(_translate("MainWindow", " 启动游戏"))
        self.pushButton_setting.setText(_translate("MainWindow", " 软件设置"))
        self.label_about.setText(_translate("MainWindow", "关于"))
        self.groupBox_help.setTitle(_translate("MainWindow", "提示"))
        self.groupBox_2.setTitle(_translate("MainWindow", "编辑"))
        self.checkBox_display_table_box.setText(_translate("MainWindow", "专业模式"))
        self.label_type_icon.setText(_translate("MainWindow", "icon"))
        self.label_sectionName.setText(_translate("MainWindow", "E1"))
        self.pushButton_jump_left.setText(_translate("MainWindow", "LEFT"))
        self.pushButton_jump_right.setText(_translate("MainWindow", "RIGHT"))
        self.label_optin_find.setText(_translate("MainWindow", "icon"))
        self.pushButton_option_reset.setText(_translate("MainWindow", "重置此修改"))
        self.pushButton_option_add.setText(_translate("MainWindow", " 新建值"))
        self.pushButton_option_remove.setText(_translate("MainWindow", " 移除此值"))
