from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets
from myTools import myTools
from myINIClass import typesID_Dict
from ra2RulesParser import rulesParser as myConfig
from UiFrame.find_ui import Ui_Form as Ui_find
from UiFrame.setting_ui import Ui_Form as Ui_setting
from UiFrame.set_value_ui import Ui_Form as ui_setValue
from UiFrame.add_option_ui import Ui_Form as ui_add_option
from UiFrame.add_section_ui import Ui_Form as ui_add_section
from UiFrame.set_value_verses_ui import Ui_Form as ui_verses
from UiFrame.global_rules_ui import Ui_Form as ui_global


def get_checkbox(index: int, item: tuple, connect: object):
    option, value = item
    if value:
        if value.lower() in ['yes', 'no'] or value.lower() in ['true', 'false']:
            checkbox = QtWidgets.QCheckBox()
            checkbox.clicked.connect(partial(connect, (index, option, checkbox.checkState)))
            if value.lower() == 'yes' or value.lower() == 'true':
                checkbox.setChecked(True)
            return checkbox


class win_find(Ui_find, QtWidgets.QWidget):
    def __init__(self):
        super(win_find, self).__init__()
        self.setupUi(self)
        self.setFixedSize(450, 150)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.hide()


class win_setting(Ui_setting, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(win_setting, self).__init__()
        if parent != None:
            self.set_location_pos(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.setFixedSize(520, 240)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.pushButton_open.clicked.connect(self.btn_open)
        self.hide()

    def btn_open(self):
        filter_text = '应用程序(*.exe)'
        folder = ''
        game_path = QtWidgets.QFileDialog.getOpenFileName(self, '设置游戏程序', folder, filter_text)[0]
        if game_path:
            self.lineEdit_game.setText('"{}"'.format(game_path))

    def set_location_pos(self, parent: QtWidgets.QMainWindow):
        pass


class win_setValue_sound(ui_setValue, QtWidgets.QWidget):
    call_back = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(win_setValue_sound, self).__init__(parent=parent)
        self.setupUi(self)
        self.setFixedSize(420, 220)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_sure.clicked.connect(self.btn_ok)
        self.pushButton_add.setHidden(True)
        self.setWindowTitle('声音选择菜单')
        self.option = ''
        self.hide()
        self.itemDict = {}
        self.value_list = []

    def init(self, itemDict):
        self.comboBox_type.clear()
        self.comboBox_unit.clear()
        self.comboBox_attribute.clear()
        self.itemDict = itemDict
        self.comboBox_type.addItems(self.itemDict.keys())
        self.comboBox_type.currentIndexChanged.connect(self.unit_refresh)
        self.comboBox_unit.currentIndexChanged.connect(self.attribute_refresh)
        self.unit_refresh()

    def btn_clicked(self, event):
        print(event)

    def unit_refresh(self, key=''):
        if type(key) == int:
            key = ''
        if not key:
            key = self.comboBox_type.currentText()
        if key:
            try:
                self.comboBox_unit.clear()
                self.comboBox_unit.addItems(self.itemDict[key].keys())
            except:
                pass

    def attribute_refresh(self, keyA='', keyB=''):
        if type(keyA) == int:
            keyA = ''
        if not keyA and not keyB:
            keyA = self.comboBox_type.currentText()
            keyB = self.comboBox_unit.currentText()
        if keyA and keyB:
            try:
                value = self.itemDict[keyA][keyB]
                self.value_list = value
                self.comboBox_attribute.clear()
                self.comboBox_attribute.addItems(value.keys())
            except:
                pass

    def get_value(self):
        if self.value_list:
            key = self.comboBox_attribute.currentText()
            return self.value_list[key].split('.')[-1]

    def get_btn_text(self):
        return self.comboBox_attribute.currentText()

    def btn_ok(self, new=None):
        if isinstance(new, list):
            name, desc = new
            self.call_back.emit([self.option, name])
            self.set_btn_text((desc if desc else name) + ' . ' + name)
        else:
            value = self.get_value()
            self.call_back.emit([self.option, value])
            self.set_btn_text(self.get_btn_text())
        self.close()

    def show_win(self, value):
        self.option = value[0]
        index = value[1]
        self.set_btn_text = value[2]
        if len(index) > 1:
            self.comboBox_type.setCurrentIndex(index[0])
            keyA = self.comboBox_type.itemText(index[0])

            self.unit_refresh(keyA)
            self.comboBox_unit.setCurrentIndex(index[1])
            keyB = self.comboBox_unit.itemText(index[1])

            self.attribute_refresh(keyA, keyB)
            if len(index) == 3:
                self.comboBox_attribute.setCurrentIndex(index[2])
        self.show()


class win_setValue_image(win_setValue_sound):
    def __init__(self, parent=None):
        super(win_setValue_image, self).__init__(parent)
        self.setWindowTitle('外观选择菜单')

    def attribute_refresh(self, keyA='', keyB=''):
        if type(keyA) == int:
            keyA = ''
        if not keyA and not keyB:
            keyA = self.comboBox_type.currentText()
            keyB = self.comboBox_unit.currentText()
        if keyA and keyB:
            value = self.itemDict[keyA][keyB]
            self.value_list = {value: value}
            self.comboBox_attribute.clear()
            self.comboBox_attribute.addItem(value)

    def get_btn_text(self):
        return self.comboBox_unit.currentText()


class win_setValue_weapon(win_setValue_sound):
    def __init__(self, show_add_section, parent=None):
        super(win_setValue_weapon, self).__init__(parent)
        self.setWindowTitle('武器选择菜单')
        self.pushButton_add.setHidden(False)
        self.pushButton_add.setText(' 新建武器到此项')
        self.pushButton_add.clicked.connect(self.add_section)
        self.show_add_section = show_add_section

    def add_section(self):
        self.show_add_section(0, self.btn_ok)


class win_setValue_warhead(win_setValue_sound):
    def __init__(self, show_add_section, parent=None):
        super(win_setValue_warhead, self).__init__(parent)
        self.setWindowTitle('弹头选择菜单')
        self.label_2.setText('描述')
        self.pushButton_add.setHidden(False)
        self.pushButton_add.setText(' 新建弹头到此项')
        self.pushButton_add.clicked.connect(self.add_section)
        self.show_add_section = show_add_section

    def add_section(self):
        self.show_add_section(1, self.btn_ok)


class win_setValue_projectile(win_setValue_sound):
    def __init__(self, show_add_section, parent=None):
        super(win_setValue_projectile, self).__init__(parent)
        self.setWindowTitle('抛射体选择菜单')
        self.label_2.setText('描述')
        self.pushButton_add.setHidden(False)
        self.pushButton_add.setText(' 新建抛射体到此项')
        self.pushButton_add.clicked.connect(self.add_section)
        self.show_add_section = show_add_section

    def add_section(self):
        self.show_add_section(2, self.btn_ok)


class win_add_option(ui_add_option, QtWidgets.QWidget):
    call_back = QtCore.pyqtSignal(list)
    table_option = 0
    table_desc = 1
    table_value = 2

    def __init__(self, showHelp, showMsg, parent=None, ):
        super(win_add_option, self).__init__(parent=parent)
        self.setupUi(self)
        self.setFixedSize(520, 640)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_sure.clicked.connect(self.btn_ok)
        self.comboBox_type.currentIndexChanged.connect(self.combobox_type_changed)
        self.table_options.itemSelectionChanged.connect(self.table_clicked)
        self.table_options.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_options.horizontalHeader().setStretchLastSection(True)
        self.lineEdit_find.textChanged.connect(self.table_find)
        self.setWindowTitle('添加属性菜单')
        self.hide()
        self.itemDict = {}
        self.main_table = []
        self.showHelp = showHelp
        self.showMsg = showMsg

    def init(self, itemDict):
        self.comboBox_type.clear()
        self.itemDict = itemDict
        self.comboBox_type.addItems(self.itemDict.keys())

    def btn_ok(self):
        if self.lineEdit_value.text():
            option, value = self.lineEdit_value.text().split('=')
            self.call_back.emit([(option, value)])
            self.hide()

            self.lineEdit_value.clear()

        else:
            items = []
            index_list = [index.row() for index in self.table_options.selectedIndexes()]
            index_list = sorted(set(index_list), key=index_list.index)
            for i in index_list:
                option = self.table_options.item(i, self.table_option).text()
                desc = self.table_options.item(i, self.table_desc).text()
                value = self.table_options.item(i, self.table_value).text()
                items.append((option, value))
            if items:
                self.call_back.emit(items)
                self.hide()
            else:
                self.showMsg(info='什么也没加!')

    def table_find(self, event=None):
        find_text = self.lineEdit_find.text()
        if find_text:
            find_list = self.table_options.findItems(find_text,
                                                     QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive)
            if find_list:
                for i in range(self.table_options.rowCount()):  # 先隐藏
                    self.table_options.setRowHidden(i, True)
                for item in find_list:
                    self.table_options.setRowHidden(item.row(), False)
        else:
            for i in range(self.table_options.rowCount()):  # 全部显示
                self.table_options.setRowHidden(i, False)

    def combobox_type_changed(self, index):
        key = self.comboBox_type.currentText()
        self.table_set_items(key)

    def table_reset(self):
        self.table_options.clear()
        self.table_options.setColumnCount(3)
        self.table_options.setHorizontalHeaderLabels(['键名', '描述', '值'])
        self.table_options.setColumnWidth(self.table_option, 160)
        self.table_options.setColumnWidth(self.table_desc, 180)
        self.table_options.setColumnWidth(self.table_value, 180)
        self.table_options.horizontalHeader().setStretchLastSection(True)

    def table_set_items(self, unitType):
        self.table_reset()
        table_items = []
        for x in self.itemDict[unitType].items():
            option = list(x[1].keys())[0]
            desc = x[0]
            value = x[1][option]
            if option not in self.main_table:
                table_items.append([option, desc, value])

        self.table_options.setRowCount(len(table_items))
        for i, item in enumerate(table_items):
            option, desc, value = item
            # option
            item = QtWidgets.QTableWidgetItem(option)
            # item.setFlags(QtCore.Qt.NoItemFlags)  # 表格不可编辑部分
            self.table_options.setItem(i, self.table_option, item)
            # 描述
            item = QtWidgets.QTableWidgetItem(desc)
            item.setTextAlignment(2 | 4)
            self.table_options.setItem(i, self.table_desc, item)
            # 值
            item = QtWidgets.QTableWidgetItem(value)
            self.table_options.setItem(i, self.table_value, item)
            # 行高
            self.table_options.setRowHeight(i, 24)
        self.table_find()

    def table_clicked(self, index=None):
        item = self.table_options.currentItem()
        if item != None:
            option = self.table_options.item(item.row(), self.table_option).text()
            self.showHelp(option)

    def show_win(self, table, unitType=None):
        self.show()
        self.main_table = [i[0] for i in table]
        self.table_set_items(unitType)
        self.comboBox_type.setCurrentText(unitType)


class win_add_section(ui_add_section, QtWidgets.QWidget):
    call_back = QtCore.pyqtSignal(list)

    table_option = 0
    table_desc = 1
    table_value = 2
    table_check = 3

    from_subWin = False
    sub_back = None

    def __init__(self, showHelp, showMsg, get_TypeIcon, get_sectionID, parent=None):
        super(win_add_section, self).__init__(parent=parent)
        self.setupUi(self)
        self.setFixedSize(520, 640)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_sure.clicked.connect(self.sure_clicked)
        self.comboBox_type.currentIndexChanged.connect(self.unit_refresh)
        self.table_options.clicked.connect(self.table_clicked)
        self.table_options.doubleClicked.connect(self.table_checked)
        self.table_options.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_options.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton_select_all.clicked.connect(self.btn_selection)
        self.pushButton_select_clear.clicked.connect(self.btn_selection)
        self.pushButton_select_invert.clicked.connect(self.btn_selection)
        self.setWindowTitle('新增单位')
        self.hide()
        self.itemDict = {}
        self.showHelp = showHelp
        self.showMsg = showMsg
        self.get_TypeIcon = get_TypeIcon
        self.get_sectionID = get_sectionID
        self.rulesmdINI = myConfig()
        self.optionDescINI = myConfig(readDesc=False)
        self.main_table = []
        self.check_list = []
        self.comboBox_ID_type.addItems(typesID_Dict.keys())

    def init(self, itemDict, rulesmdINI, optionDescINI):
        self.comboBox_type.clear()
        self.comboBox_unit.clear()
        self.itemDict = itemDict
        self.rulesmdINI = rulesmdINI
        self.optionDescINI = optionDescINI
        self.comboBox_type.addItems(self.itemDict.keys())
        self.comboBox_unit.currentIndexChanged.connect(self.combobox_unit_changed)
        self.comboBox_ID_type.currentIndexChanged.connect(self.combobox_typeID_changed)
        self.combobox_typeID_changed()
        self.unit_refresh()

    def combobox_typeID_changed(self, index=None):
        key = self.comboBox_ID_type.currentText()
        if key not in '武器类.弹体类':
            self.lineEdit_ID.setEnabled(True)
            minID = self.get_sectionID(typesID_Dict[key])
            self.lineEdit_ID.setText(minID)
            self.lineEdit_ID.setValidator(QtGui.QIntValidator(int(minID), 999999))
        else:
            self.lineEdit_ID.clear()
            self.lineEdit_ID.setEnabled(False)

    def combobox_unit_changed(self, index=None):
        key_1 = self.comboBox_type.currentText()
        key_2 = self.comboBox_unit.currentText()
        if key_1:
            self.comboBox_ID_type.setCurrentIndex(self.comboBox_type.currentIndex())
            self.label_type_icon.setPixmap(self.get_TypeIcon(typesID_Dict[key_1]))
        try:
            self.table_set_items(self.itemDict[key_1][key_2])
        except:
            pass

    def unit_refresh(self, key=''):
        if type(key) == int:
            key = ''
        if not key:
            key = self.comboBox_type.currentText()
        if key:
            try:
                self.comboBox_unit.clear()
                self.comboBox_unit.addItems(self.itemDict[key].keys())
            except:
                pass

    def sure_clicked(self):
        key = self.comboBox_ID_type.currentText()
        type_name = typesID_Dict[key]
        type_id = self.lineEdit_ID.text()
        section_name = self.lineEdit_UIName.text()
        nameDesc = self.lineEdit_NameDesc.text()
        items = []

        for i, check in enumerate(self.check_list):
            if check.isChecked():
                option = self.table_options.item(i, self.table_option).text()
                value = self.table_options.item(i, self.table_value).text()
                items.append((option, value))

        if not items:
            self.showMsg(info='请选中表格至少一个参数')
            return

        if not section_name:
            self.showMsg(info='请输入注册名，仅限英文+数字')
            return

        if self.rulesmdINI.has_section(section_name):
            self.showMsg(info='注册名重复，请重命名')
            return

        if key not in '武器类.弹体类':
            if not type_id:
                self.showMsg(info='请输入一个新的ID数字')
                return

            if self.rulesmdINI.has_option(type_name, type_id):
                self.showMsg(info='ID重复，请重新填写')
                return
        else:
            type_id = ''

        data = [type_name, type_id, section_name, nameDesc, items, self.from_subWin]
        self.call_back.emit(data)
        if self.from_subWin:
            self.sub_back([section_name, nameDesc])
        self.close()

    def table_reset(self):
        self.check_list.clear()
        self.table_options.clear()
        self.table_options.setColumnCount(4)
        self.table_options.setHorizontalHeaderLabels(['键名', '描述', '值', '选择'])
        self.table_options.setColumnWidth(self.table_check, 30)
        self.table_options.setColumnWidth(self.table_option, 120)
        self.table_options.setColumnWidth(self.table_desc, 140)
        self.table_options.setColumnWidth(self.table_value, 140)
        self.table_options.horizontalHeader().setStretchLastSection(True)

    def table_set_items(self, unitType):
        self.table_reset()
        table_items = []
        if self.rulesmdINI.has_section(unitType):
            for option, value in self.rulesmdINI.items(unitType):
                try:
                    desc = self.optionDescINI.get('OptionDesc', option)
                except:
                    desc = ''
                if option not in self.main_table:
                    table_items.append([option, desc, value.split(';')[0].strip()])

            self.table_options.setRowCount(len(table_items))
            for i, item in enumerate(table_items):
                option, desc, value = item
                # check
                item = QtWidgets.QCheckBox()
                self.table_options.setCellWidget(i, self.table_check, item)
                self.check_list.append(item)

                # option
                item = QtWidgets.QTableWidgetItem(option)
                item.setFlags(QtCore.Qt.NoItemFlags)  # 表格不可编辑部分
                self.table_options.setItem(i, self.table_option, item)
                # 描述
                item = QtWidgets.QTableWidgetItem(desc)
                item.setTextAlignment(2 | 4)
                self.table_options.setItem(i, self.table_desc, item)
                # 值
                item = QtWidgets.QTableWidgetItem(value)
                self.table_options.setItem(i, self.table_value, item)
                # 行高
                self.table_options.setRowHeight(i, 24)
            self.pushButton_select_all.click()

    def table_checked(self, index=None):
        self.table_options.cellWidget(index.row(), self.table_check).click()

    def table_clicked(self, index=None):
        item = self.table_options.item(index.row(), self.table_option)
        self.showHelp(item.text())

    def btn_selection(self):
        sender = self.sender().objectName()
        if sender == 'pushButton_select_all':
            for check in self.check_list:
                check.setChecked(True)
        elif sender == 'pushButton_select_clear':
            for check in self.check_list:
                check.setChecked(False)
        elif sender == 'pushButton_select_invert':
            for check in self.check_list:
                if check.isChecked():
                    check.setChecked(False)
                else:
                    check.setChecked(True)

    def show_for_subWin(self, mode, callback):
        self.from_subWin = True
        self.sub_back = callback
        if mode == 0:
            self.comboBox_type.setCurrentText('武器类')
        elif mode == 1:
            self.comboBox_type.setCurrentText('弹头类')
        elif mode == 2:
            self.comboBox_type.setCurrentText('弹体类')
        self.comboBox_type.setEnabled(False)
        self.comboBox_ID_type.setEnabled(False)
        self.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.comboBox_type.setEnabled(True)
        self.comboBox_ID_type.setEnabled(True)
        self.from_subWin = False
        a0.accept()


class win_set_verses(ui_verses, QtWidgets.QWidget):
    call_back = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        super(win_set_verses, self).__init__(parent=parent)
        self.setupUi(self)
        self.setFixedSize(720, 260)
        self.setWindowTitle('伤害百分比调整')
        self.pushButton_sure.clicked.connect(self.btn_sure)
        self.pushButton_cancel.clicked.connect(self.close)
        self.box_list = [self.spinBox_1, self.spinBox_2, self.spinBox_3, self.spinBox_4, self.spinBox_5,
                         self.spinBox_6, self.spinBox_7, self.spinBox_8, self.spinBox_9, self.spinBox_10,
                         self.spinBox_11]
        self.slider_list = [self.verticalSlider_1, self.verticalSlider_2, self.verticalSlider_3, self.verticalSlider_4,
                            self.verticalSlider_5, self.verticalSlider_6, self.verticalSlider_7, self.verticalSlider_8,
                            self.verticalSlider_9, self.verticalSlider_10, self.verticalSlider_11]
        self.option = ''
        self.set_btn_text = None

    def set_value(self, value):
        value_list = value.replace('%', '').split(',')
        for i, v in enumerate(value_list):
            self.slider_list[i].setValue(int(v))
            self.box_list[i].setValue(int(v))

    def get_value(self):
        value_list = []
        for i in range(11):
            value_list.append(str(self.box_list[i].value()))
        return '%,'.join(value_list) + '%'

    def btn_sure(self):
        value = self.get_value()
        self.call_back.emit([self.option, value])
        self.set_btn_text(value)
        self.close()

    def show_win(self, item):
        self.option = item[0]
        self.set_value(item[1]())
        self.set_btn_text = item[2]
        self.show()


class win_rules_global(ui_global, QtWidgets.QWidget):
    call_back = QtCore.pyqtSignal(list)
    table_option = 0
    table_desc = 1
    table_value = 2
    section_dict = {
        '多人游戏对话框设置': 'MultiplayerDialogSettings',
        '难度设置-简单': 'Easy',
        '难度设置-普通': 'Normal',
        '难度设置-冷酷': 'Difficult',
        '奖励箱规则': 'CrateRules',
        '电脑AI设置': 'AI',
        '电脑IQ设置': 'IQ',
        'Jumpjet飞行规则': 'JumpjetControls',
        '超级武器规则': 'SpecialWeapons',
        '音频视频规则': 'AudioVisual',
        '战斗与伤害规则': 'CombatDamage',
        '辐射设置': 'Radiation',
        '颜色主题': 'Colors',
    }
    find_dict = {
        '全部': '',
        '伞兵设置': ['Para', 'Pilot', 'PParatrooper'],
        '秘密科技': 'Secret',
        '定义单位': ['Shipyard', 'RepairBay', 'BaseUnit', 'HarvesterUnit', 'PadAircraft', 'Prerequisite'],
        '老兵设置': 'Veteran',
        '随机超武': ['Meteorites', 'IonStorms'],
    }
    desc_icon = None
    jump_icon = None
    current_section = ''
    myTranslator = None

    def __init__(self, get_widget, get_optionDesc, showHelp, set_desc, find_items, parent=None):
        super(win_rules_global, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowTitle('全局设置')
        self.setFixedSize(800, 600)
        self.table_options.itemSelectionChanged.connect(self.table_clicked)
        self.table_options.itemChanged.connect(self.table_changed)
        self.table_options.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_options.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_options.customContextMenuRequested.connect(self.table_menu)
        self.lineEdit_find.returnPressed.connect(self.line_find)
        self.pushButton_sure.clicked.connect(self.btn_sure)
        self.comboBox.addItems(self.find_dict.keys())
        self.comboBox.addItems(self.section_dict.keys())
        self.comboBox.setCurrentText('全部')
        self.comboBox.currentIndexChanged.connect(self.comboBox_changed)
        self.checkBox_display.clicked.connect(self.check_display)
        self.rules = None
        self.get_widget = get_widget
        self.get_optionDesc = get_optionDesc
        self.showHelp = showHelp
        self.set_desc = set_desc
        self.find_items = find_items
        self.table_items = []
        self.table_isSet = False
        self.table_widgets = {}
        self.hide()

    def init(self, rules):
        self.rules = rules

    def table_reset(self):
        self.table_options.clear()
        self.table_options.setColumnCount(3)
        self.table_options.setHorizontalHeaderLabels(['键名', '描述', '值'])
        self.table_options.setColumnWidth(self.table_option, 160)
        self.table_options.setColumnWidth(self.table_desc, 180)
        self.table_options.setColumnWidth(self.table_value, 180)
        self.table_options.horizontalHeader().setStretchLastSection(True)
        self.table_options.setRowCount(0)
        self.table_isSet = False

    def check_display(self):
        self.comboBox_changed(display=True)
        # self.table_set_items()

    def table_set_items(self, section=''):
        if section:
            self.table_items.clear()
            self.current_section = section
            self.table_items = self.rules.items(section)
        self.table_reset()
        self.table_options.setRowCount(len(self.table_items))
        for i, ru_item in enumerate(self.table_items):
            option, value = ru_item
            desc = self.get_optionDesc(self.current_section,option)
            if value:
                value = value.split(';', 1)[0].strip()
            # option
            item = QtWidgets.QTableWidgetItem(option)
            # item.setFlags(QtCore.Qt.ItemIsSelectable)  # 表格不可编辑部分
            self.table_options.setItem(i, self.table_option, item)
            # 描述
            item = QtWidgets.QTableWidgetItem(desc)
            item.setTextAlignment(2 | 4)
            self.table_options.setItem(i, self.table_desc, item)
            # 值
            item = QtWidgets.QTableWidgetItem(value)
            self.table_options.setItem(i, self.table_value, item)

            if not self.checkBox_display.checkState():
                widget = get_checkbox(i, (option, value), self.table_widget_Clicked)
                if widget:
                    self.table_options.item(i, self.table_value).setText('')
                    widget.setProperty('name', 'table_widget')
                    self.table_options.setCellWidget(i, self.table_value, widget)
                    self.table_widgets.setdefault(option, widget)

            # 行高
            if value:
                color = QtGui.QColor('#ff3f3f')  # 数字颜色
                is_number = myTools.is_number(value)
                if is_number != -1:
                    self.table_options.item(i, self.table_value).setForeground(color)
                    self.table_options.item(i, self.table_value).setFont(QtGui.QFont('Times', 10, QtGui.QFont.Medium))

            self.table_options.setRowHeight(i, 24)
        self.table_isSet = True

    def table_clicked(self, index=None):
        item = self.table_options.currentItem()
        if item != None:
            option = self.table_options.item(item.row(), self.table_option).text()
            self.showHelp(option)

    def table_widget_Clicked(self, info):
        index, option, check = info
        item = self.table_items[index]
        value = self.get_check_value(check(), item[1])
        self.table_items[index] = (option, value)

    def table_find(self, find_text=''):
        find_list = []
        if find_text:
            if not isinstance(find_text, list):
                find_text = [find_text]
            for text in find_text:
                find_list += self.table_options.findItems(
                    text, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive | QtCore.Qt.MatchCaseSensitive)
                if find_list:
                    for i in range(self.table_options.rowCount()):  # 先隐藏
                        self.table_options.setRowHidden(i, True)
                    for item in find_list:
                        self.table_options.setRowHidden(item.row(), False)
        else:
            for i in range(self.table_options.rowCount()):  # 全部显示
                self.table_options.setRowHidden(i, False)

    def table_changed(self):
        if self.table_isSet:
            item = self.table_options.currentItem()
            if item != None:
                index = item.row()
                value = self.table_options.item(index, self.table_value).text()
                desc = self.table_options.item(index, self.table_desc).text()
                option = self.table_items[index][0]
                self.table_items[index] = (option, value)
                self.set_desc(option, desc)

    def line_find(self):
        self.table_find(self.lineEdit_find.text())

    def comboBox_changed(self, index=None, display=False):
        self.lineEdit_find.setText('')
        key = self.comboBox.currentText()
        if self.find_dict.get(key) != None:
            if self.current_section != 'General':
                self.update_data()
                self.table_set_items('General')
            elif display:
                self.table_set_items()
            self.table_find(self.find_dict[key])
        else:
            self.lineEdit_find.setText('')
            self.update_data()
            self.table_set_items(self.section_dict[key])

    def get_check_value(self, checked: bool, value: str):
        value = value.split(';', 1)[0].strip()
        boolText = ['yes', 'no'] if value in 'yes,no' else ['true', 'false']
        value = boolText[0] if checked else boolText[1]
        return value

    def update_data(self):
        if self.current_section:
            for option, value in self.table_items:
                self.rules.set(self.current_section, option, value)

    def btn_sure(self, event=None):
        self.update_data()
        self.close()

    def table_get_selection(self):
        index_list = [index.row() for index in self.table_options.selectedIndexes()]
        return sorted(set(index_list), key=index_list.index)

    def table_menu(self, pos):
        if self.current_section:
            menu = QtWidgets.QMenu()
            index_list = self.table_get_selection()
            menu_items = []
            jump_value = ''
            option = ''

            if len(index_list) == 1:
                jump_value = self.table_items[index_list[0]][1].split(';', 1)[0].strip()
                if myTools.is_number(jump_value) == -1:
                    if not jump_value.lower() in ['yes', 'no'] and not jump_value.lower() in ['true', 'false']:
                        item = QtWidgets.QAction('定位到此单位：{0}'.format(jump_value))
                        item.setIcon(self.jump_icon)
                        menu_items.append(item)
                        menu.addAction(menu_items[-1])

                if self.myTranslator != None:
                    menu.addSeparator()
                    option = self.table_items[index_list[0]][0]
                    item = QtWidgets.QAction('翻译此项到描述：{0}'.format(option))
                    item.setIcon(self.desc_icon)
                    menu_items.append(item)
                    menu.addAction(menu_items[-1])

            if menu_items:
                action = menu.exec_(self.table_options.mapToGlobal(pos))
                if action != None:
                    if '定位到此单位' in action.text():
                        self.find_items(jump_value)

                    elif '翻译此项到描述' in action.text():
                        if self.myTranslator != None:
                            text = myTools.space_text(option)
                            fanyi = self.myTranslator.fanyi(text).replace(' ', '')
                            self.set_desc(option, fanyi)
                            self.comboBox_changed(display=True)
                        else:
                            print('翻译失败')

    def show_win(self):
        if self.rules != None:
            self.table_set_items('General')
            self.show()
