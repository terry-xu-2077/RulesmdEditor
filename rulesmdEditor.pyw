from functools import partial
from UiFrame.main_win_x_ui import *
from myWidgets import myComboBox_checkList
from myINIClass import myIniClass, typesDict
from myTheme import myQTheme
from mySubWin import *
from threading import Thread
from subprocess import Popen
from myTools import *
from LinkNode import linkNode
from baiduFanyi import baidu_Translate
from ra2RulesParser import rulesParser
from appInfo import send_to_server, user_hash
from appInfo import get_now_timestamp
import webbrowser
import sys
import os
import re
import requests


def get_OptionCategory():
    op = rulesParser('Resources/OptionCategory.ini')
    result = {
        '全部': '',
        '通用': op['UnitOptions']['General'].split(','),
        '阵营': op['UnitOptions']['Owner'].split(','),
        '武器': op['UnitOptions']['Weapon'].split(','),
        '运动': op['UnitOptions']['MoveType'].split(','),
        '视觉': op['UnitOptions']['Visual'].split(','),
        '声音': op['UnitOptions']['Audio'].split(','),
        '特殊': ''
    }
    return result


changed_data = []
changed_temp = {}

my_config = rulesParser('Resources/Config.ini')
optionCategoryDict = get_OptionCategory()
icons = './Resources/icons-normal.png'
my_theme = myQTheme(
    config='./Resources/Theme.ini',
    icons=icons,
    icon_size=56
)

qss_menubar = my_theme.get_menu_QSS()
qss_menu = my_theme.get_menu_QSS(True)
qss_checkbox = my_theme.get_checkbox_QSS(False)
qss_table = my_theme.get_table_qss()
qss_all = my_theme.get_ALL_QSS()
btn_icon_size = QtCore.QSize(22, 22)
key_icon_size = QtCore.QSize(28, 28)
jump_icon_size = QtCore.QSize(20, 20)
cfgName = 'RulesmdEditor-Teri'

table_columns_option = 0
table_columns_desc = 1
table_columns_value = 2

type_icon_dict = {
    'InfantryTypes': (0, 3),
    'VehicleTypes': (1, 3),
    'AircraftTypes': (2, 3),
    'BuildingTypes': (3, 3),
    'SuperWeaponTypes': (4, 3),
    'Weapons': (5, 3),
    'Warheads': (6, 3),
    'Projectiles': (3, 4)
}


class rulesmdEditor(Ui_MainWindow, QtWidgets.QMainWindow, myIniClass):
    def __init__(self):
        super(rulesmdEditor, self).__init__(callback=self.show_msgbox)
        self.app_icon = QtGui.QIcon('Resources/app.ico')
        self.setupUi(self)
        self.resize(1800, 1000)
        self.setWindowTitle('rulesmd编辑器')
        self.setWindowIcon(self.app_icon)

        self.tree_levels = {}
        self.forceClose = False
        self.rules_files = ''
        self.current_section_name = ''
        self.current_item = None
        self.current_section = []
        self.save_new_file = False
        self.updated = False
        self.new_rules = False
        self.table_ready = False
        self.find_index = -1
        self.table_index = -1
        self.table_widgets = {}
        self.tree_find_list = []
        self.myTranslator = None
        self.fanyiText = ''

        Thread(target=self.init_translator_TD).start()
        self.TD_ready = False

        self.linkNode = linkNode()
        self.show_jump_widgets('hide')

        self.name_desc_edited = False
        self.option_desc_edited = []
        self.copy_options = None
        self.copy_value = ''
        if not os.path.exists(my_config.file):
            self.setting_config(True)

        self.theme_qss = '*{font-family:Microsoft Yahei;}' + qss_checkbox + qss_table

        self.set_theme()
        self.init_subWin()
        self.init_widgets()
        self.init_connect()
        self.set_icons()

    def init_translator_TD(self):
        try:
            self.myTranslator = baidu_Translate()
            self.rulesGlobal_win.myTranslator = self.myTranslator
        except:
            pass
            # print('翻译初始化失败，可能是没有网络连接')

    def setting_config(self, init=False):
        print('初始化设置文件')
        if init:
            init_list = [
                ['lastFile', ''],
                ['gamePath', ''],
                ['tableMode', 'False'],
                ['useTheme', 'False'],
                ['autoSaveRules', 'False'],
                ['autoSaveDesc', 'False']
            ]
            my_config.add_section(cfgName)
            for s in init_list:
                my_config.set(cfgName, *s)
            my_config.write_file()
        else:
            my_config.set(cfgName, 'gamePath', self.setting_win.lineEdit_game.text())
            my_config.setboolean(cfgName, 'tableMode', self.setting_win.checkBox_pro.checkState())
            my_config.setboolean(cfgName, 'useTheme', self.setting_win.checkBox_use_theme.checkState())
            my_config.setboolean(cfgName, 'autoSaveRules', self.setting_win.checkBox_auto_save_rules.checkState())
            my_config.setboolean(cfgName, 'autoSaveDesc', self.setting_win.checkBox_auto_save_desc.checkState())
            self.game_path = my_config[cfgName]['gamePath']
            my_config.write_file()

    # todo 初始化控件
    def init_widgets(self):
        # 设置控件文本
        self.label_sectionName.setText('')
        self.label_sectionName.adjustSize()
        self.label_about.setText('Teri')
        self.label_about.setStyleSheet('color:#4e4760;font-size:15px')
        self.lineEdit_option_find.setToolTip('按回车开始查找')
        self.lineEdit_item_find.setToolTip('按回车开始查找')
        self.lineEdit_name_desc.setToolTip('此文本仅用来描述，不会写入ini')
        self.pushButton_jump_left.setToolTip('向前跳转')
        self.pushButton_jump_right.setToolTip('向后跳转')

        # 隐藏跳转按钮
        self.show_jump_widgets('hide')

        # 设置树状表
        self.tree_sections.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tree_sections.keyReleaseEvent = self.tree_keyRelease
        self.tree_sections.setColumnCount(3)
        self.tree_sections.setHeaderLabels(['描述', '名称', '注册ID'])
        self.tree_sections.setColumnWidth(0, 260)
        self.tree_sections.setColumnWidth(1, 180)
        self.tree_sections.setColumnWidth(2, 40)
        self.tree_Set_Nodes()
        # 设置表格
        self.table_options.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # self.table_options.setShowGrid(False)
        self.table_reset()
        # 设置下拉列表
        self.comboBox_option_find.addItems(optionCategoryDict.keys())

    def init_subWin(self):
        # 初始化子窗口
        self.find_win = win_find()
        self.find_win.setStyleSheet(self.theme_qss)
        self.find_win.setWindowTitle('查找单位')
        self.find_win.lineEdit_find.returnPressed.connect(self.tree_find_line)
        self.find_win.pushButton_find.clicked.connect(self.tree_find_line)
        self.find_win.pushButton_up.clicked.connect(self.btn_find_other)
        self.find_win.pushButton_down.clicked.connect(self.btn_find_other)

        self.setting_win = win_setting()
        self.setting_win.setStyleSheet(self.theme_qss)
        self.setting_win.setWindowTitle('设置')
        self.setting_win.setWindowIcon(self.app_icon)
        self.setting_win.pushButton_sure.clicked.connect(self.btn_setting_save)
        self.setting_win.pushButton_cancel.clicked.connect(self.setting_win.close)
        # self.checkBox_display_table_box.setChecked(True)

        self.rulesGlobal_win = win_rules_global(
            get_widget=self.table_get_widgets,
            get_optionDesc=self.rulesmd_get_option_desc,
            showHelp=self.show_help_info,
            set_desc=self.set_user_option_desc,
            find_items=self.global_find_items)
        self.rulesGlobal_win.setStyleSheet(self.theme_qss)
        self.rulesGlobal_win.setWindowIcon(self.app_icon)
        # self.rulesGlobal_win.setWindowModality(QtCore.Qt.ApplicationModal)
        # self.rulesGlobal_win.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # self.rulesGlobal_win.setParent(self)

        self.add_option_win = win_add_option(
            showHelp=self.show_help_info,
            showMsg=self.show_msgbox)
        self.add_option_win.setStyleSheet(self.theme_qss)
        self.add_section_win = win_add_section(
            showHelp=self.show_help_info,
            showMsg=self.show_msgbox,
            get_TypeIcon=self.table_get_type_icon,
            get_sectionID=self.get_rules_section_newID
        )
        self.add_section_win.setStyleSheet(self.theme_qss)

        self.image_win = win_setValue_image()
        self.image_win.setStyleSheet(self.theme_qss)
        self.sound_win = win_setValue_sound()
        self.sound_win.setStyleSheet(self.theme_qss)
        self.weapon_win = win_setValue_weapon(self.add_section_win.show_for_subWin)
        self.weapon_win.setStyleSheet(self.theme_qss)
        self.warhead_win = win_setValue_warhead(self.add_section_win.show_for_subWin)
        self.warhead_win.setStyleSheet(self.theme_qss)
        self.projectile_win = win_setValue_projectile(self.add_section_win.show_for_subWin)
        self.projectile_win.setStyleSheet(self.theme_qss)
        self.verses_win = win_set_verses()
        self.verses_win.setStyleSheet(self.theme_qss)

        self.pushButton_option_reset.hide()

        self.image_win.call_back.connect(self.table_widgets_clicked)
        self.sound_win.call_back.connect(self.table_widgets_clicked)
        self.weapon_win.call_back.connect(self.table_widgets_clicked)
        self.warhead_win.call_back.connect(self.table_widgets_clicked)
        self.projectile_win.call_back.connect(self.table_widgets_clicked)
        self.verses_win.call_back.connect(self.table_widgets_clicked)
        self.add_option_win.call_back.connect(self.table_add_options)
        self.add_section_win.call_back.connect(self.tree_add_section)

    # todo 初始化链接
    def init_connect(self):
        self.pushButton_open.clicked.connect(self.btn_open_files)
        self.pushButton_new.clicked.connect(self.btn_new_rules)
        self.pushButton_setting.clicked.connect(self.btn_setting)
        self.pushButton_section_find.clicked.connect(self.btn_find_win)
        self.pushButton_section_find.setHidden(True)  # 查找按钮
        self.pushButton_rules_global.clicked.connect(self.rulesGlobal_win.show_win)
        self.lineEdit_item_find.returnPressed.connect(self.tree_find_line)
        self.checkBox_display_table_box.clicked.connect(self.table_display_checkbox_clicked)
        self.lineEdit_option_find.returnPressed.connect(self.option_find_line)
        self.lineEdit_name_desc.textEdited.connect(self.name_desc_changed)
        self.comboBox_option_find.currentIndexChanged.connect(self.table_comboBox_changed)
        self.comboBox_section_find.currentIndexChanged.connect(self.tree_combobox_changed)

        self.pushButton_save_desc.clicked.connect(self.btn_save_desc)
        self.pushButton_section_replay.clicked.connect(self.btn_replace_section)
        self.pushButton_save_data.clicked.connect(self.btn_save_rules)
        self.pushButton_section_back.clicked.connect(self.btn_save_section)
        self.pushButton_save_new.clicked.connect(self.btn_save_new)
        self.pushButton_run_game.clicked.connect(self.btn_run_game)
        self.pushButton_option_remove.clicked.connect(self.table_remove_options)
        self.pushButton_section_add.clicked.connect(self.btn_add_section)
        self.pushButton_section_remove.clicked.connect(self.tree_remove_section)

        self.tree_sections.clicked.connect(self.tree_clicked)
        self.table_options.itemSelectionChanged.connect(self.table_set_selection)
        self.table_options.cellChanged.connect(self.table_text_changed)
        self.table_options.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_options.customContextMenuRequested.connect(self.table_menu)
        self.tree_sections.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree_sections.customContextMenuRequested.connect(self.tree_menu)
        self.textBrowser_help.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textBrowser_help.customContextMenuRequested.connect(self.help_menu)
        self.checkBox_display_find.clicked.connect(self.tree_show_find)
        self.pushButton_option_add.clicked.connect(self.btn_option_new_clicked)

        self.pushButton_jump_left.clicked.connect(partial(self.btn_jump_clicked, direction=-1))
        self.pushButton_jump_right.clicked.connect(partial(self.btn_jump_clicked, direction=1))

    def set_theme(self):
        if not my_config.getboolean(cfgName, 'useTheme'):
            self.section_bg = '#d4e2ed'
            self.section_fg = '#000000'
            self.option_bg = '#595959'
            self.option_fg = '#ffffff'
            self.setStyleSheet(self.theme_qss)
            return
        self.pushButton_open.setProperty('name', 'key')
        self.pushButton_new.setProperty('name', 'key')
        self.pushButton_run_game.setProperty('name', 'key')
        self.pushButton_setting.setProperty('name', 'key')
        self.pushButton_save_data.setProperty('name', 'key')
        self.pushButton_save_new.setProperty('name', 'key')
        self.pushButton_save_desc.setProperty('name', 'key')
        self.textBrowser_help.setProperty('name', 'help')

        self.section_bg = my_theme.color['section-bg-color']
        self.section_fg = my_theme.color['section-fg-color']
        self.option_bg = my_theme.color['option-bg-color']
        self.option_fg = my_theme.color['option-fg-color']

        self.setStyleSheet(qss_all)
        # self.theme_qss = qss_all

    def set_icons(self):
        self.item_add_icon = my_theme.get_Qicon((1, 1))
        self.item_remove_icon = my_theme.get_Qicon((2, 1))
        self.desc_icon = my_theme.get_Qicon((4, 0))

        lookup_icon = my_theme.get_icon_pixmap([3, 0], [28, 28])
        self.label_item_find.setPixmap(lookup_icon)
        self.label_optin_find.setPixmap(lookup_icon)
        self.find_win.setWindowIcon(QtGui.QIcon(lookup_icon))
        self.rulesGlobal_win.label_icon.setPixmap(lookup_icon)
        self.add_option_win.label_icon.setPixmap(lookup_icon)

        self.pushButton_section_find.setIcon(QtGui.QIcon(lookup_icon))
        self.pushButton_section_find.setIconSize(btn_icon_size)

        self.pushButton_section_add.setIcon(self.item_add_icon)
        self.pushButton_section_add.setIconSize(btn_icon_size)
        self.pushButton_section_remove.setIcon(self.item_remove_icon)
        self.pushButton_section_remove.setIconSize(btn_icon_size)
        self.pushButton_section_replay.setIcon(my_theme.get_Qicon((3, 1)))
        self.pushButton_section_replay.setIconSize(btn_icon_size)
        self.pushButton_section_back.setIcon(my_theme.get_Qicon((4, 1)))
        self.pushButton_section_back.setIconSize(btn_icon_size)

        self.pushButton_option_add.setIcon(self.item_add_icon)
        self.pushButton_option_add.setIconSize(btn_icon_size)
        self.pushButton_option_remove.setIcon(self.item_remove_icon)
        self.pushButton_option_remove.setIconSize(btn_icon_size)

        # self.pushButton_jump_left.setIcon(my_theme.get_Qicon((4, 4)))
        # self.pushButton_jump_left.setIconSize(jump_icon_size)
        # self.pushButton_jump_right.setIcon(my_theme.get_Qicon((5, 4)))
        # self.pushButton_jump_right.setIconSize(jump_icon_size)

        self.pushButton_run_game.setIcon(my_theme.get_Qicon((6, 6)))
        self.pushButton_run_game.setIconSize(key_icon_size)
        self.pushButton_setting.setIcon(my_theme.get_Qicon((2, 0)))
        self.pushButton_setting.setIconSize(key_icon_size)
        self.pushButton_open.setIcon(my_theme.get_Qicon((0, 0)))
        self.pushButton_open.setIconSize(key_icon_size)
        self.pushButton_new.setIcon(my_theme.get_Qicon((1, 0)))
        self.pushButton_new.setIconSize(key_icon_size)
        self.pushButton_save_desc.setIcon(self.desc_icon)
        self.pushButton_save_desc.setIconSize(key_icon_size)
        self.pushButton_save_new.setIcon(my_theme.get_Qicon((5, 0)))
        self.pushButton_save_new.setIconSize(key_icon_size)
        self.pushButton_save_data.setIcon(my_theme.get_Qicon((6, 0)))
        self.pushButton_save_data.setIconSize(key_icon_size)
        self.pushButton_rules_global.setIcon(my_theme.get_Qicon((0, 6)))
        self.pushButton_rules_global.setIconSize(key_icon_size)

        self.add_section_win.setWindowIcon(my_theme.get_Qicon((3, 4)))
        self.add_option_win.setWindowIcon(my_theme.get_Qicon((3, 4)))

        self.btn_image_icon = my_theme.get_Qicon([3, 2])
        self.btn_sound_icon = my_theme.get_Qicon([2, 2])
        self.btn_weapon_icon = my_theme.get_Qicon(type_icon_dict['Weapons'])
        self.btn_warhead_icon = my_theme.get_Qicon(type_icon_dict['Warheads'])
        self.btn_projectile_icon = my_theme.get_Qicon(type_icon_dict['Projectiles'])
        self.btn_verses_icon = my_theme.get_Qicon((3, 4))

        self.image_win.setWindowIcon(self.btn_image_icon)
        self.sound_win.setWindowIcon(self.btn_sound_icon)

        self.weapon_win.setWindowIcon(self.btn_weapon_icon)
        self.warhead_win.setWindowIcon(self.btn_warhead_icon)
        self.projectile_win.setWindowIcon(self.btn_projectile_icon)

        self.weapon_win.pushButton_add.setIcon(self.item_add_icon)
        self.warhead_win.pushButton_add.setIcon(self.item_add_icon)
        self.projectile_win.pushButton_add.setIcon(self.item_add_icon)

        self.verses_win.setWindowIcon(self.btn_verses_icon)

        self.btn_jump_icon = my_theme.get_Qicon((6, 4))
        self.label_type_icon.setPixmap(my_theme.get_icon_pixmap([3, 4], [28, 28]))

        self.rulesGlobal_win.desc_icon = self.desc_icon
        self.rulesGlobal_win.jump_icon = self.pushButton_jump_right.icon()

    # todo 跳转部件设置
    def show_jump_widgets(self, info, text=''):

        if info == 'left.show':
            self.pushButton_jump_left.setDisabled(False)
            self.pushButton_jump_left.setText('<<' + text)
            return

        elif info == 'right.show':
            self.pushButton_jump_right.setDisabled(False)
            self.pushButton_jump_right.setText(text + '>>')
            return

        elif info == 'left.hide':
            self.pushButton_jump_left.setDisabled(True)
            self.pushButton_jump_left.setText('')
            return

        elif info == 'right.hide':
            self.pushButton_jump_right.setDisabled(True)
            self.pushButton_jump_right.setText('')
            return

        elif info == 'hide':
            self.pushButton_jump_right.setDisabled(True)
            self.pushButton_jump_right.setText('')
            self.pushButton_jump_left.setDisabled(True)
            self.pushButton_jump_left.setText('')
            return

    def btn_jump_clicked(self, direction):  # todo < > 箭头按钮
        desc_name = self.rulesmd_get_UIName_desc(self.current_section_name)
        if not desc_name:
            desc_name = self.current_section_name

        node = self.linkNode.get_next(direction=direction)
        if not node:
            return
        section, item = node
        test_right = self.linkNode.get_next(direction=1, test=True)
        test_left = self.linkNode.get_next(direction=-1, test=True)

        if test_right:
            name = self.rulesmd_get_UIName_desc(test_right[0])
            self.show_jump_widgets('right.show', name if name else test_right[0])
        else:
            self.show_jump_widgets('right.hide')

        if test_left:
            name = self.rulesmd_get_UIName_desc(test_left[0])
            self.show_jump_widgets('left.show', name if name else test_left[0])
        else:
            self.show_jump_widgets('left.hide')

        if self.tree_sections.currentItem() == item:  # 是当前项就什么也不做
            return

        self.tree_sections.setCurrentItem(item)
        self.tree_sections.setFocus()
        self.tree_goto_section(self.tree_sections.currentIndex())

    def jump_to_section(self, option):  # todo 表格中的跳转按钮
        value = ''
        for x in self.current_section:
            if x[0] == option:
                value = x[1]
                break
        if not value:
            return

        desc_name = self.rulesmd_get_UIName_desc(self.current_section_name)
        if not desc_name:
            desc_name = self.current_section_name

        target = self.tree_find_section(value, True)
        if target:

            sectionItem = [self.current_section_name, self.tree_sections.currentItem()]
            valueItem = [value, target[0]]

            self.show_jump_widgets('hide')
            if self.linkNode.index != -1:  # 存在link
                self.linkNode.get_next(valueItem)
                self.show_jump_widgets('left.show', desc_name)
                if self.linkNode.get_next(valueItem, direction=1, test=True):
                    self.show_jump_widgets('right.show')
            else:  # 新link
                self.linkNode.set(sectionItem, valueItem)
                self.show_jump_widgets('left.show', desc_name)

            self.tree_sections.setCurrentItem(target[0])
            self.tree_sections.setFocus()
            self.tree_goto_section(self.tree_sections.currentIndex())
        else:
            self.show_msgbox(info='无法跳转，因为没有发现此项')

    def init_data_TD(self):  # todo 多线程获取数据
        self.TD_ready = False
        for i in [self.image_dict, self.weapon_dict, self.sound_dict, self.add_options_dict, self.building_list,
                  self.add_section_dict, self.warhead_dict, self.projectile_dict, self.side_dict]:
            i.clear()

        self.building_list = self.get_building_list()
        self.image_dict = self.get_unitName_dict(True)
        self.weapon_dict = self.get_weapons_dict()

        self.warhead_dict = self.get_warheads_dict()
        self.projectile_dict = self.get_projectile_dict()

        self.sound_dict = self.get_voiceSound_dict()
        self.add_options_dict = self.get_options_dict()
        self.add_section_dict = self.get_section_dict()

        self.image_win.init(self.image_dict)
        self.weapon_win.init(self.weapon_dict)
        self.warhead_win.init(self.warhead_dict)
        self.projectile_win.init(self.projectile_dict)
        self.sound_win.init(self.sound_dict)
        self.add_option_win.init(self.add_options_dict)
        self.add_section_win.init(self.add_section_dict, self.rulesmdINI, self.optionsDescINI)
        self.rulesGlobal_win.init(self.rulesmdINI)
        self.side_dict = self.rulesmd_get_side_dict()
        self.comboBox_section_find.clear()
        self.comboBox_section_find.addItems(self.side_dict.keys())
        self.TD_ready = True

    def tree_add_item(self, item, look=False):  # todo: tree添加项
        typeName, name_desc, section, obj_id = item
        level = self.tree_levels.get(typeName)
        tree_item = QtWidgets.QTreeWidgetItem(level)
        # 获取中文名
        name_desc = self.rulesmd_get_UIName_desc(section)
        if not name_desc:
            name_desc = self.get_Name(section)
        # 获取所属阵营
        tree_item.setText(0, name_desc)
        tree_item.setText(1, section)
        tree_item.setText(2, obj_id)
        if look:
            self.tree_sections.setCurrentItem(tree_item)
            self.tree_sections.setFocus()
            self.tree_clicked(self.tree_sections.currentIndex())

    def tree_Set_Nodes(self):
        if not self.rulesmdINI:
            return

        self.rulesGlobal_win.close()
        self.tree_levels.clear()
        Thread(target=self.init_data_TD).start()

        # 设置节点
        self.tree_sections.clear()

        root_dict = self.get_rules_TypeListSections()

        for i, root_key in enumerate(root_dict.keys()):

            level_name = root_key
            level_list = root_dict[root_key]

            tree_level = QtWidgets.QTreeWidgetItem(self.tree_sections)
            tree_level.setIcon(0, my_theme.get_Qicon(type_icon_dict[level_name]))
            tree_level.setText(0, self.get_type_sectionDesc(level_name))
            tree_level.setText(1, level_name)
            tree_level.setText(2, '数量 {}'.format(len(level_list)))

            self.tree_levels.setdefault(level_name, tree_level)

            for i in range(3):
                tree_level.setBackground(i, QtGui.QColor(self.section_bg))
                tree_level.setForeground(i, QtGui.QColor(self.section_fg))

            for x, item in enumerate(level_list):
                if type(item) == list:
                    section = item[0]
                    obj_id = item[1]
                else:
                    section = item
                    obj_id = '*'

                if self.rulesmdINI.has_section(section):
                    name_desc = self.rulesmd_get_UIName_desc(section)
                    if not name_desc:
                        name_desc = self.get_Name(section)
                    self.tree_add_item([level_name, name_desc, section, obj_id])

            self.tree_sections.addTopLevelItem(tree_level)
        self.tree_sections.setStyleSheet('QTreeWidget::item{height:30px;}')

    def tree_keyRelease(self, event):
        index = self.tree_sections.currentIndex()
        self.tree_clicked(index)

    def tree_clicked(self, index):  # todo tree点击
        self.linkNode.clear()
        self.show_jump_widgets('hide')
        self.tree_goto_section(index)

    def tree_goto_section(self, index):
        item = self.tree_sections.currentItem()
        if item.text(1) not in self.root_sections:
            if self.table_index != index.row():  # 防止连续点击刷新
                self.table_index = index.row()
                if not self.updated:
                    self.update_data()
                    self.update_desc()
                self.textBrowser_help.setText('')
                self.current_item = item
                self.table_set_Items(item.text(1))

    def tree_add_section(self, item):  # todo 新增单位
        type_name, type_id, section_name, nameDesc, items, fromSubwin = item
        self.rulesmd_add_unit(item[:-1])
        self.dict_update(type_name, section_name, nameDesc)

        data = [type_name, nameDesc, section_name, '*' if not type_id else type_id]
        if fromSubwin:
            self.tree_add_item(data)
        else:
            self.tree_add_item(data, True)
        changed_data.append('{0}|新增单位：{1}，描述：{2}'.format(get_now_timestamp(), section_name, nameDesc))

    def dict_update(self, type_name, section_name, nameDesc):  # todo 更新菜单字典
        name = typesDict[type_name]
        if not nameDesc:
            nameDesc = section_name
        if name in ['武器类', '弹头类', '弹体类']:
            item_dict = {nameDesc + ' . ' + section_name: section_name}

            if name == '武器类':
                if self.weapon_dict.get('未分类') != None:
                    self.weapon_dict['未分类'].setdefault(nameDesc, item_dict)
            elif name == '弹头类':
                if self.warhead_dict.get('弹头类') != None:
                    self.warhead_dict['弹头类'].setdefault(nameDesc, item_dict)
            elif name == '弹体类':
                if self.projectile_dict.get('弹体类') != None:
                    self.projectile_dict['弹体类'].setdefault(nameDesc, item_dict)

    def tree_remove_section(self):  # todo 移除单位
        item = self.tree_sections.currentItem()
        section = item.text(1)
        nameDesc = item.text(0)
        rep = self.show_msgbox(sure='你确定要移除这个单位吗？\n{0} {1}'.format(nameDesc, section), button=[(0, '确定'), (-1, '取消')])
        if rep == 0:
            if self.rulesmdINI.has_section(section):
                self.clear_rules_section(section)
                self.rulesmdINI.remove_section(section)
            parent = item.parent()
            parent.removeChild(item)
            changed_data.append('{0}|移除单位：{1}，描述：{2}'.format(get_now_timestamp(), section, nameDesc))

    def tree_menu(self, pos):  # todo tree右键菜单
        if self.rulesmdINI:

            current_item = self.tree_sections.currentItem()
            parent = current_item.parent()
            menu_items = []
            menu = QtWidgets.QMenu()
            # menu.setStyleSheet(qss_menu)

            if parent != None:
                item = QtWidgets.QAction('复制此名称 : {}'.format(current_item.text(1)))
                item.setIcon(parent.icon(0))
                menu_items.append(item)
                menu.addAction(menu_items[-1])
                menu.addSeparator()

            item = QtWidgets.QAction('全部展开')
            menu_items.append(item)
            menu.addAction(menu_items[-1])
            item = QtWidgets.QAction('全部折叠')
            menu_items.append(item)
            menu.addAction(menu_items[-1])

            if menu_items:
                action = menu.exec_(self.tree_sections.mapToGlobal(pos))
                if action != None:
                    if '复制此名称' in action.text():
                        self.copy_value = current_item.text(1)
                        myTools.addToClipboard(self.copy_value)
                    elif action.text() == '全部展开':
                        self.tree_sections.expandAll()
                    elif action.text() == '全部折叠':
                        self.tree_sections.collapseAll()

    def tree_find_line(self, section=None):
        sender = self.sender().objectName()
        if section == None or type(section) == bool:
            if sender == 'lineEdit_item_find':
                find_text = self.lineEdit_item_find.text()
            else:
                pass
                # find_text = self.find_win.lineEdit_find.text()
        else:
            find_text = section

        self.tree_find_list = self.tree_find_section(find_text)

        self.find_index = 0
        if self.tree_find_list:
            self.tree_show_find()
            # self.find_win.label_info.setText('找到{0}项，当前第{1}项'.format(len(self.tree_find_list), self.find_index + 1))
            self.look_at_item()

    def tree_get_parent_index(self, item):
        parent = item.parent()
        return self.tree_sections.indexFromItem(parent)

    def tree_hide_all(self, hide=False):
        for p in range(self.tree_sections.topLevelItemCount()):
            parent = self.tree_sections.topLevelItem(p)
            child_count = parent.childCount()
            for i in range(child_count):
                index = self.tree_get_parent_index(parent.child(i))
                self.tree_sections.setRowHidden(i, index, hide)

    def tree_show_find(self):
        if self.checkBox_display_find.isChecked():
            if self.tree_find_list:
                self.tree_hide_all(True)
                for item in self.tree_find_list:
                    parent = item.parent()
                    if parent != None:
                        row = parent.indexOfChild(item)
                        index = self.tree_get_parent_index(item)
                        self.tree_sections.setRowHidden(row, index, False)
        else:
            self.tree_hide_all(False)

    def tree_find_section(self, text, strict=False):
        if strict:
            find_list = self.tree_sections.findItems(text, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive, 1)
        else:
            find_list = self.tree_sections.findItems(text,
                                                     QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive, 1)
            if not find_list:
                find_list = self.tree_sections.findItems(text,
                                                         QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive, 0)
        return find_list

    def tree_find_all(self, section_list):
        self.tree_find_list.clear()
        for item in section_list:
            find_list = self.tree_find_section(item, True)
            if find_list:
                self.tree_find_list.append(find_list[0])

    # todo tree下拉框
    def tree_combobox_changed(self):
        if self.TD_ready:
            key = self.comboBox_section_find.currentText()
            if self.side_dict[key] != None:
                self.checkBox_display_find.setChecked(True)
                section_list = []
                for section in ['BuildingTypes', 'InfantryTypes', 'VehicleTypes', 'AircraftTypes', 'SuperWeaponTypes']:
                    section_list.extend(self.side_dict[key][section])
                if section_list:
                    self.tree_find_all(section_list)
                    self.tree_show_find()
                    self.tree_sections.expandAll()
                    return
            self.tree_hide_all()
            self.tree_sections.collapseAll()

    def global_find_items(self, text):
        self.checkBox_display_find.setChecked(True)
        self.tree_find_all(text.split(','))
        if self.tree_find_list:
            self.tree_show_find()
            self.tree_sections.expandAll()
        else:
            self.show_msgbox(info='未找到此单位：\n' + text)

    def table_set_selection(self):
        item = self.table_options.currentItem()
        if item != None:
            option = self.table_options.item(item.row(), table_columns_option).text()
            self.show_help_info(option)

    def table_display_checkbox_clicked(self):
        if self.current_section_name:
            self.table_set_Items()

    def table_set_Items(self, section=''):  # todo 表格加入数据
        self.updated = False
        if section:
            self.quote_dict.clear()
            self.quote_dict = self.get_quote_section(section)
            self.current_section_name = section
            self.current_section.clear()

            type_name = self.tree_sections.currentItem().parent().text(1)
            self.label_type_icon.setPixmap(self.table_get_type_icon(type_name))

            name = self.rulesmd_get_UIName_desc(section)
            if not name:
                name = self.get_Name(section)
            self.lineEdit_name_desc.setText(name)

            if self.rulesmdINI.has_section(section):
                self.current_section = self.rulesmdINI.items(section)

        self.table_reset()
        self.table_options.setRowCount(len(self.current_section))
        self.label_sectionName.setText(self.current_section_name)
        for i, item in enumerate(self.current_section):
            option, value = item
            table_item = QtWidgets.QTableWidgetItem(self.rulesmd_get_option_desc(self.current_section_name, option))
            table_item.setTextAlignment(2 | 4)
            self.table_options.setItem(i, table_columns_desc, table_item)

            table_item = QtWidgets.QTableWidgetItem(value)
            self.table_options.setItem(i, table_columns_value, table_item)

            table_item = QtWidgets.QTableWidgetItem(option)
            # table_item.setForeground(QtGui.QColor(self.option_fg))
            # table_item.setBackground(QtGui.QColor(self.option_bg))
            # table_item.setFlags(QtCore.Qt.ItemIsSelectable) #表格不可编辑部分
            self.table_options.setItem(i, table_columns_option, table_item)

            self.table_options.setRowHeight(i, 24)
            if value:
                color = QtGui.QColor('#ff3f3f')  # 数字颜色
                is_number = myTools.is_number(value)
                if is_number != -1:
                    self.table_options.item(i, table_columns_value).setForeground(color)
                    self.table_options.item(i, table_columns_value).setFont(
                        QtGui.QFont('Times', 10, QtGui.QFont.Medium))

            if not self.checkBox_display_table_box.checkState():
                table_widget = self.table_get_widgets(option, value)

                if table_widget != None:
                    self.table_options.item(i, table_columns_value).setText('')
                    table_widget.setProperty('name', 'table_widget')

                    # self.table_options.item(i, table_desc).setForeground(QtGui.QColor(self.option_fg))
                    # for x in range(3):
                    #     self.table_options.item(i, x).setBackground(QtGui.QColor(self.option_bg))

                    self.table_options.setCellWidget(i, table_columns_value, table_widget)
        self.table_ready = True
        self.table_comboBox_changed()

    def table_get_widgets(self, option, value):  # todo 表格获取控件
        # 伤害百分比
        if option == 'Verses':
            set_btn = QtWidgets.QPushButton()
            set_btn.setStyleSheet("QPushButton { text-align: left; }")
            set_btn.setIconSize(btn_icon_size)
            set_btn.setIcon(self.btn_verses_icon)
            set_btn.setText(' ' + value)
            set_btn.clicked.connect(partial(self.verses_win.show_win, [option, set_btn.text, set_btn.setText]))
            return set_btn

        # 武器弹头
        if option in self.weapon_options or option in ['Projectile', 'Warhead']:
            # todo 跳转按钮 加入单位
            layout = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.LeftToRight)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(0)
            set_btn = QtWidgets.QPushButton()
            set_btn.setStyleSheet("QPushButton { text-align: left; }")
            set_btn.setIconSize(btn_icon_size)
            if option == 'Warhead':
                set_btn.setIcon(self.btn_warhead_icon)
            elif option == 'Projectile':
                set_btn.setIcon(self.btn_projectile_icon)
            else:
                set_btn.setIcon(self.btn_weapon_icon)
            set_btn.setText(' ' + value)
            box_index = []
            if value:
                name_path = self.weapon_dict.find_value_index(value)
                if name_path != None:
                    set_btn.setText(name_path[0][-1])
                    box_index = name_path[1]
            else:
                set_btn.setText('空')

            if option in self.weapon_options:
                set_btn.clicked.connect(partial(self.weapon_win.show_win, [option, box_index, set_btn.setText]))
            elif option == 'Warhead':
                set_btn.clicked.connect(partial(self.warhead_win.show_win, [option, box_index, set_btn.setText]))
            elif option == 'Projectile':
                set_btn.clicked.connect(partial(self.projectile_win.show_win, [option, box_index, set_btn.setText]))

            layout.addWidget(set_btn)
            jump_btn = QtWidgets.QPushButton()
            jump_btn.setMaximumSize(QtCore.QSize(40, 16777215))
            jump_btn.setIconSize(btn_icon_size)
            jump_btn.setIcon(self.btn_jump_icon)
            jump_btn.clicked.connect(partial(self.jump_to_section, option))

            layout.addWidget(jump_btn)
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)
            return widget

        # 单位跳转
        if option in ['DeploysInto', 'UndeploysInto', 'FreeUnit', 'Spawns', 'SuperWeapon', 'Enslaves']:
            jump_btn = QtWidgets.QPushButton()
            jump_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
            jump_btn.setStyleSheet("QPushButton { text-align: right; }")
            # jump_btn.setMaximumSize(QtCore.QSize(200, 16777215))
            jump_btn.setIconSize(btn_icon_size)
            jump_btn.setIcon(self.btn_jump_icon)
            name = self.rulesmd_get_UIName_desc(value)
            if not name:
                name = value
            jump_btn.setText(name)
            jump_btn.clicked.connect(partial(self.jump_to_section, option))
            return jump_btn

        # 菜单
        for i, v in enumerate(['Image', 'Sound', 'Voice']):
            if v in option:
                set_btn = QtWidgets.QPushButton()
                set_btn.setStyleSheet("QPushButton { text-align: left; }")
                set_btn.setIconSize(btn_icon_size)
                set_btn.setText(' ' + value)
                box_index = []
                if option == 'Image':
                    if value:
                        name_path = self.image_dict.find_value_index(value)
                        if name_path != None:
                            set_btn.setText(name_path[0][-1])
                            box_index = name_path[1]
                    else:
                        set_btn.setText('空')
                    set_btn.clicked.connect(partial(self.image_win.show_win, [option, box_index, set_btn.setText]))
                    set_btn.setIcon(self.btn_image_icon)
                    return set_btn
                elif 'Sound' in option or 'Voice' in option:
                    if value:
                        name_path = self.sound_dict.find_value_index(value)
                        if name_path != None:
                            set_btn.setText(name_path[0][-1])
                            box_index = name_path[1]
                    else:
                        set_btn.setText('空')
                    set_btn.clicked.connect(partial(self.sound_win.show_win, [option, box_index, set_btn.setText]))
                    set_btn.setIcon(self.btn_sound_icon)
                    return set_btn

        # 单选
        if value.lower() in ['yes', 'no'] or value.lower() in ['true', 'false']:
            checkbox = QtWidgets.QCheckBox()
            checkbox.clicked.connect(partial(self.table_widgets_clicked, (option, checkbox.isChecked)))
            if value.lower() == 'yes' or value.lower() == 'true':
                checkbox.setChecked(True)
            return checkbox

        # 多选
        model = ''
        if option in self.Country_options:
            model = 'Country'
        elif option in self.Abilities_options:
            model = 'Abilities'
        elif option in self.Buildings_options:
            model = 'Buildings'

        op_list = self.rulesmd_get_option_menu(model)
        if model:
            combobox = myComboBox_checkList()
            combobox.option = option
            combobox.selection_changed.connect(self.table_widgets_clicked)
            select_list = []
            if model == 'Buildings':
                value_list = value.upper().split(',')
            else:
                value_list = value.split(',')
            for i, v in enumerate(op_list):
                if v[0] in value_list:
                    select_list.append(i)
            if not select_list:
                return None
            combobox.addCheckBoxes(op_list, select_list)
            combobox.show_selection()
            return combobox

        # 列表
        op_list = self.rulesmd_get_option_menu(option)
        if op_list:
            combobox = myComboBox_checkList()
            combobox.option = option
            combobox.selection_changed.connect(self.table_widgets_clicked)
            for i, v in enumerate(op_list):
                if v[1]:
                    op = v
                else:
                    op = [v[0], v[0]]
                combobox.addItemValue(op)
                if value.lower() == v[0].lower():
                    combobox.setCurrentIndex(i)
            return combobox
        return None

    def table_widgets_clicked(self, info):  # todo 表格小部件点击
        for i, op in enumerate(self.current_section):
            if info[0] == op[0]:
                value = op[1]
                if type(info[1]) == str:
                    value = info[1]
                    item = self.tree_find_section(value, True)
                    if item and self.linkNode.index + 1 < len(self.linkNode.link):
                        self.linkNode.set_next([value, item[0]])
                        name = self.rulesmd_get_UIName_desc(value)
                        self.show_jump_widgets('right.show', name if name else value)
                else:
                    boolText = ['yes', 'no'] if value in 'yes,no' else ['true', 'false']
                    value = boolText[0] if info[1]() else boolText[1]
                self.current_section[i] = [op[0], value]
                changed_temp[self.current_section_name + "_" + op[0]] = '{0}|修改单位：{1}{2}，键名：{3}{4}，值变化：{5}>{6}'.format(
                    get_now_timestamp(),
                    self.current_section_name,
                    self.get_UIName_desc(self.current_section_name),
                    op[0],
                    self.get_option_desc(op[0]),
                    op[1],
                    value)
                break

    def table_text_changed(self):  # todo 表格内容更改
        if self.table_ready:

            row = self.table_options.currentRow()
            option = self.table_options.item(row, table_columns_option).text()
            desc = self.table_options.item(row, table_columns_desc).text()
            if desc != self.rulesmd_get_option_desc(self.current_section, option):
                self.option_desc_edited.append([option, desc])

            for i, op in enumerate(self.current_section):
                new_value = self.table_options.item(i, table_columns_value).text()
                if new_value:
                    value = op[1]
                    if new_value != value:
                        changed_temp[
                            self.current_section_name + "_" + op[0]] = '{0}|修改单位：{1}{2}，键名：{3}{4}，值变化：{5}>{6}'.format(
                            get_now_timestamp(),
                            self.current_section_name,
                            self.get_UIName_desc(self.current_section_name),
                            option,
                            desc,
                            value,
                            new_value)
                        self.current_section[i] = [op[0], new_value]

    # todo 删除数据
    def table_remove_options(self):
        if self.current_section:
            self.clear_rules_section(self.current_section_name)
            items_count = len(self.current_section)
            index_list = self.table_get_selection()
            del_items = []
            for i in index_list:
                try:
                    del_items.append(self.current_section.pop(i))
                except:
                    pass

            changed_temp[self.current_section_name] = '{0}|修改单位:{1}{2},删除数据{3}'.format(
                get_now_timestamp(),
                self.current_section_name,
                self.get_UIName_desc(self.current_section_name),
                del_items)

            self.update_data()
            self.table_set_Items()

    # todo 插入数据
    def table_add_options(self, items):
        self.clear_rules_section(self.current_section_name)
        current_index = self.table_options.currentIndex().row() + 1
        if current_index == 1:
            current_index = self.table_options.rowCount()

        select_index = current_index - 1
        for item in items:
            self.current_section.insert(current_index, item)
            select_index += 1

        self.update_data()
        self.table_set_Items()
        self.table_options.selectRow(select_index)
        self.table_options.setFocus()

        changed_temp[self.current_section_name] = '{0}|修改单位:{1}{2},插入数据{3}'.format(
            get_now_timestamp(),
            self.current_section_name,
            self.get_UIName_desc(self.current_section_name),
            items)

    def table_get_selection(self):
        index_list = [index.row() for index in self.table_options.selectedIndexes()]
        return sorted(set(index_list), key=index_list.index)

    # todo 帮助右键
    def help_menu(self, pos):
        op_item = self.table_options.item(self.table_options.currentIndex().row(), 0)
        if op_item:
            menu_items = []
            menu = QtWidgets.QMenu()

            name_1 = '打开 modenc 网站查看详情'
            item = QtWidgets.QAction(name_1)
            item.setIcon(self.desc_icon)
            menu_items.append(item)
            menu.addAction(menu_items[-1])

            name_2 = '从 modenc 获取说明信息'
            item = QtWidgets.QAction(name_2)
            item.setIcon(self.item_add_icon)
            menu_items.append(item)
            menu.addAction(menu_items[-1])

            action = menu.exec_(self.textBrowser_help.mapToGlobal(pos))
            if action != None:
                if name_1 == action.text():
                    webbrowser.open('https://www.modenc.renegadeprojects.com/' + op_item.text())
                if name_2 == action.text():
                    try:
                        response = requests.get('https://www.modenc.renegadeprojects.com/' + op_item.text())
                        text = \
                            re.findall("</td></tr></table><br clear=\"all\" /><br />\n<p>(.*?)</p>", response.text,
                                       re.S)[0]
                        text = re.sub('<.*?>', '', text)
                        if self.myTranslator != None:
                            text = self.myTranslator.fanyi(text)
                        self.textBrowser_help.setText(text)
                    except:
                        pass

    # todo 表格右键
    def table_menu(self, pos):
        if self.current_section_name:
            menu = QtWidgets.QMenu()
            # menu.setStyleSheet(qss_menu)
            index_list = self.table_get_selection()
            menu_items = []
            jump_items = []
            jump_value = ''

            if len(index_list) == 1:
                item = QtWidgets.QAction('在此插入新项')
                item.setIcon(self.item_add_icon)
                menu_items.append(item)
                menu.addAction(menu_items[-1])
                menu.addSeparator()

            if index_list:
                item = QtWidgets.QAction('删除选中项：{0}'.format(len(index_list)))
                item.setIcon(self.item_remove_icon)
                menu_items.append(item)
                menu.addAction(menu_items[-1])
                item = QtWidgets.QAction('复制选中项：{0}'.format(len(index_list)))
                item.setIcon(self.item_add_icon)
                menu_items.append(item)
                menu.addAction(menu_items[-1])

            if len(index_list) == 1:
                menu.addSeparator()
                item = QtWidgets.QAction('复制此值')
                item.setIcon(self.item_add_icon)
                menu_items.append(item)
                menu.addAction(menu_items[-1])

            if self.copy_options:
                menu.addSeparator()
                item = QtWidgets.QAction('粘贴已复制项：{0}'.format(len(self.copy_options)))
                item.setIcon(self.item_add_icon)
                menu_items.append(item)
                menu.addAction(menu_items[-1])

            if self.copy_value:
                if len(index_list) == 1:
                    item = QtWidgets.QAction('粘贴此值：{0}'.format(self.copy_value))
                    item.setIcon(self.item_add_icon)
                    menu_items.append(item)
                    menu.addAction(menu_items[-1])

            if self.quote_dict:
                quote_menu = menu.addMenu(self.pushButton_jump_left.icon(), '跳转到引用单位')
                for key in self.quote_dict.keys():
                    jump_items.append(QtWidgets.QAction(key))
                quote_menu.addActions(jump_items)

            if len(index_list) == 1:
                jump_value = self.current_section[index_list[0]][1]
                if myTools.is_number(jump_value) == -1:

                    if not jump_value.lower() in ['yes', 'no'] and not jump_value.lower() in ['true', 'false']:
                        menu.addSeparator()
                        item = QtWidgets.QAction('跳转到此单位：{0}'.format(jump_value))
                        item.setIcon(self.btn_jump_icon)
                        menu_items.append(item)
                        menu.addAction(menu_items[-1])

            self.fanyiText = ''
            if self.myTranslator != None:
                if len(index_list) == 1:
                    menu.addSeparator()
                    self.fanyiText = self.current_section[index_list[0]][0]
                    item = QtWidgets.QAction('翻译此项到描述：{0}'.format(self.fanyiText))
                    item.setIcon(self.desc_icon)
                    menu_items.append(item)
                    menu.addAction(menu_items[-1])

            action = menu.exec_(self.table_options.mapToGlobal(pos))
            if action != None:
                if '在此插入新项' in action.text():
                    self.btn_option_new_clicked()

                elif '删除选中项' in action.text():
                    rep = self.show_msgbox(sure='你确定要删除这个值吗？', button=[(0, '确定'), (-1, '取消')])
                    if rep == 0:
                        self.table_remove_options()

                elif '复制此值' in action.text():
                    self.copy_value = self.current_section[index_list[0]][1]
                    myTools.addToClipboard(self.copy_value)

                elif '粘贴此值' in action.text():
                    option = self.current_section[index_list[0]][0]
                    value = self.copy_value
                    self.current_section[index_list[0]] = (option, value)
                    self.table_set_Items()
                    self.update_data()

                elif '复制选中项' in action.text():
                    self.copy_options = []
                    for i in index_list:
                        self.copy_options.append(self.current_section[i])

                elif '粘贴已复制项' in action.text():
                    # rep = self.show_msgbox(sure='你确定要在此粘贴这个值吗？', button=[(0, '确定'), (-1, '取消')])
                    # if rep == 0:
                    self.table_add_options(self.copy_options)
                elif action.text() in self.quote_dict.keys():
                    section = self.quote_dict[action.text()]
                    self.tree_find_line(section)

                elif '翻译此项到描述' in action.text():
                    text = myTools.space_text(self.fanyiText)
                    fanyi = self.myTranslator.fanyi(text).replace(' ', '')
                    self.set_user_option_desc(self.fanyiText, fanyi)
                    self.table_set_Items()

                elif '跳转到此单位' in action.text():
                    self.global_find_items(jump_value)

    # todo 重置表格
    def table_reset(self):
        self.table_ready = False
        self.table_widgets.clear()
        self.table_options.clear()
        self.table_options.setColumnCount(3)
        self.table_options.setHorizontalHeaderLabels(['键名', '描述', '值', ])
        self.table_options.setColumnWidth(table_columns_option, 180)
        self.table_options.setColumnWidth(table_columns_desc, 180)
        self.table_options.setColumnWidth(table_columns_value, 240)
        self.table_options.horizontalHeader().setStretchLastSection(True)
        # self.table_options.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)

    def table_show_all(self):
        for i in range(self.table_options.rowCount()):  # 全部显示
            self.table_options.setRowHidden(i, False)

    # todo 筛选表格
    def table_find(self, find_text='', invert=False):
        find_list = []
        if find_text:
            if not isinstance(find_text, list):
                find_text = [find_text]
            for text in find_text:
                if text:
                    find_list += self.table_options.findItems(
                        text, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive | QtCore.Qt.MatchCaseSensitive)
                if find_list:
                    if not invert:
                        for i in range(self.table_options.rowCount()):  # 先隐藏
                            self.table_options.setRowHidden(i, not invert)
                    for item in find_list:
                        self.table_options.setRowHidden(item.row(), invert)
        else:
            self.table_show_all()

    def table_comboBox_changed(self, index=None):
        key = self.comboBox_option_find.currentText()
        if optionCategoryDict.get(key) != None:
            if key == '特殊':
                self.table_show_all()
                for k in optionCategoryDict.keys():
                    if k not in ['全部', '特殊']:
                        self.table_find(optionCategoryDict[k], True)

            else:
                self.table_find(optionCategoryDict[key])
        else:
            self.lineEdit_find.setText('')

    def table_get_type_icon(self, type_name):
        return my_theme.get_icon_pixmap(type_icon_dict[type_name], [28, 28])

    def show_help_info(self, option):
        self.groupBox_help.setWindowTitle('提示：' + option)
        text = self.get_help_info(option)
        if not text:
            text = self.rulesmdINI.get_option_desc(self.current_section, option)
            if text:
                text = '文件注释:\n' + text
        self.textBrowser_help.setText(text)

    # todo 更新数据
    def update_data(self):
        if not self.rulesmdINI:
            return
        self.updated = True  # 更新rulesmd
        for i, op in enumerate(self.current_section):
            option = op[0]
            value = op[1]
            if self.rulesmdINI.has_section(self.current_section_name):
                self.rulesmdINI.set(self.current_section_name, option, value)

    def update_desc(self):
        # 更新option描述
        if self.option_desc_edited:
            for i in self.option_desc_edited:
                print(i)
                self.set_user_option_desc(*i)
            self.option_desc_edited.clear()

        # 更新名称
        if self.name_desc_edited:
            name_option = self.current_section_name
            name_desc = self.lineEdit_name_desc.text()
            if name_option:
                self.set_user_Name_desc(name_option, name_desc)
            self.name_desc_edited = False

    def btn_save_desc(self):
        self.update_desc()
        self.save_desc_INI()

    def btn_save_rules(self):
        if not self.rulesmdINI:
            return
        self.update_data()
        rules_file = self.rules_files
        if self.save_new_file or self.new_rules:
            filter_text = 'rulesmd.ini'
            if not rules_file:
                rules_file = 'rulesmd.ini'
            full_name = QtWidgets.QFileDialog.getSaveFileName(self, caption='另存为', directory=rules_file,
                                                              filter=filter_text)
            if full_name:
                rules_file = full_name[0]
                self.rules_files = full_name[0]
                self.save_new_file = False
                self.new_rules = False

        if rules_file:
            self.rulesmdINI.write_file(rules_file)

    def btn_save_new(self):
        self.save_new_file = True
        self.btn_save_rules()

    def btn_new_rules(self):  # todo 新建规则
        self.new_rules = True
        self.open_rules_file('Resources/rulesmd.pre')
        self.tree_Set_Nodes()

    def btn_find_win(self):
        pos = QtGui.QCursor.pos().x() - 450, QtGui.QCursor.pos().y() + 60
        self.find_win.lineEdit_find.setText(self.lineEdit_item_find.text())
        self.find_win.move(*pos)
        self.find_win.show()

    def btn_setting(self):
        self.setting_win.checkBox_pro.setChecked(my_config.getboolean(cfgName, 'tableMode'))
        self.setting_win.checkBox_use_theme.setChecked(my_config.getboolean(cfgName, 'useTheme'))
        self.setting_win.checkBox_auto_save_rules.setChecked(my_config.getboolean(cfgName, 'autoSaveRules'))
        self.setting_win.checkBox_auto_save_desc.setChecked(my_config.getboolean(cfgName, 'autoSaveDesc'))
        self.setting_win.lineEdit_game.setText(my_config[cfgName]['gamePath'])
        self.setting_win.show()

    def btn_setting_save(self):
        self.setting_config()
        self.setting_win.close()

    def btn_add_section(self):  # todo 新增单位
        if not self.rulesmdINI:
            return
        self.add_section_win.show()

    def look_at_item(self):
        self.tree_sections.setCurrentItem(self.tree_find_list[self.find_index])
        self.tree_sections.setFocus()
        self.tree_clicked(self.tree_sections.currentIndex())

    def btn_find_other(self):
        if self.tree_find_list:
            sender = self.sender().objectName()
            if sender == 'pushButton_up':
                if self.find_index > 0:
                    self.find_index -= 1
            else:
                if self.find_index + 1 < len(self.tree_find_list):
                    self.find_index += 1
            self.find_win.label_info.setText('找到{0}项，当前第{1}项'.format(len(self.tree_find_list), self.find_index + 1))
            self.look_at_item()

    def option_find_line(self, section=None):
        find_text = self.lineEdit_option_find.text()
        self.table_find_list = self.table_options.findItems(
            find_text, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive | QtCore.Qt.MatchCaseSensitive)

        if self.table_find_list:
            self.table_options.setCurrentItem(self.table_find_list[0])
            self.table_options.setFocus()
            row = self.table_find_list[0].row()
            self.show_help_info(self.table_options.item(row, 0).text())

    def name_desc_changed(self):  # todo 名字被改变
        self.name_desc_edited = True
        name = self.lineEdit_name_desc.text()
        self.current_item.setText(0, name)

    def btn_open_files(self):  # todo 打开文件
        filter_text = '*.ini'
        folder = my_config[cfgName]['lastFile']
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        self.rules_files = dialog.getOpenFileName(self, '打开规则文件', folder, filter_text)[0]
        if self.rules_files:
            my_config.set(cfgName, 'lastFile', self.rules_files)
            self.new_rules = False
            self.open_rules_file(self.rules_files)
            self.tree_Set_Nodes()

    def btn_run_game(self):
        game_path = my_config.get(cfgName, 'gamePath')
        if game_path:
            cwd = os.path.split(game_path[1:-1])[0]
            Popen(game_path, cwd=cwd)
            self.show_msgbox(info='游戏已启动...')

    def btn_option_new_clicked(self):
        if self.current_section:
            unitType = self.tree_sections.currentItem().parent().text(1)
            if typesDict.get(unitType):
                self.add_option_win.show_win(self.current_section, typesDict[unitType])

    def btn_save_section(self):
        if self.tree_sections.currentItem() != None:
            section = self.tree_sections.currentItem().text(1)
            desc = self.tree_sections.currentItem().text(0)
            timeStr = myTools.get_current_timeStr()
            fileName = '[backup][{0}][{1}]{2}.ini'.format(desc, section, timeStr)
            filter_text = '配置文件(*.ini)'
            full_name = QtWidgets.QFileDialog.getSaveFileName(self, caption='保存：{}{}'.format(section, desc),
                                                              directory=fileName, filter=filter_text)
            if full_name[0]:
                self.save_rules_section_backup(section, full_name[0])

    def btn_replace_section(self):
        if self.tree_sections.currentItem() != None:
            section = self.tree_sections.currentItem().text(1)
            desc = self.tree_sections.currentItem().text(0)
            filter_text = '配置文件(*.ini)'
            fileName = QtWidgets.QFileDialog.getOpenFileName(self, caption='还原：{}{}'.format(section, desc),
                                                             filter=filter_text)
            if fileName:
                if fileName[0]:
                    rep = self.replace_from_file(section, fileName[0])
                    if rep:
                        self.updated = True
                        self.table_index = -1
                        self.tree_clicked(self.tree_sections.currentIndex())

    def show_msgbox(self, **kwargs):
        if kwargs.get('debug'):
            QtWidgets.QMessageBox.warning(self, '发生错误', kwargs['debug'])
            with open('debug.txt', 'a') as f:
                info_text = myTools.get_current_timeStr() + '\n' + str(kwargs['debug']) + '\n'
                f.write(info_text)
                f.close()
        elif kwargs.get('error'):
            QtWidgets.QMessageBox.warning(self, '错误', kwargs['error'])

        elif kwargs.get('info'):
            QtWidgets.QMessageBox.information(self, '提示', kwargs['info'])

        elif kwargs.get('sure'):
            msgbox = QtWidgets.QMessageBox(self)
            btn_list = []
            for i in kwargs.get('button'):
                btn = msgbox.addButton(QtWidgets.QMessageBox.Yes)
                btn.setText(i[1])
                btn_list.append([btn, i[0]])
            msgbox.setDefaultButton(btn_list[0][0])
            msgbox.setWindowTitle('提示')
            msgbox.setText(kwargs['sure'])
            msgbox.exec()
            result = msgbox.clickedButton()
            for btn in btn_list:
                if btn[0] == result:
                    return btn[1]
        else:
            print(kwargs)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        if not self.forceClose:
            rep = self.show_msgbox(sure='确定要退出本软件吗？', button=[(0, '确定'), (-1, '取消')])
            if rep == 0:
                if my_config.getboolean(cfgName, 'autoSaveDesc'):
                    self.btn_save_desc()
                if not self.new_rules and not self.save_new_file:
                    if my_config.getboolean(cfgName, 'autoSaveRules'):
                        self.btn_save_rules()
                my_config.write_file()
                if self.myTranslator != None:
                    self.myTranslator.close()
                self.rulesGlobal_win.close()

                data = get_changed_data()
                if data: send_to_server({'text': data, 'user': user_hash}, code='log')

                a0.accept()
            else:
                a0.ignore()
        else:
            a0.accept()


def get_changed_data():
    data = changed_data
    for item in changed_temp.items():
        data.append(item[1])
    data.sort(key=lambda t: t.split("|")[0])
    return data


if __name__ == '__main__':
    send_to_server({'start': user_hash})
    os.chdir(os.path.split(sys.argv[0])[0])
    translator = QtCore.QTranslator()
    translator.load('./Resources/qt_zh_CN.qm')
    app = QtWidgets.QApplication(sys.argv)
    app.installTranslator(translator)
    app.setStyle('Fusion')
    gui = rulesmdEditor()
    gui.label_about.setText('最终编译时间')
    help_info = '''
    <p style=\"font-weight:bold; color:#00b0ff;font-size:15px;\">使用说明：</p>
    1. 打开规则：浏览文件夹，并打开一个rulesmd.ini文件以开始编辑<br>
    2. 新建规则：新建一个全新的rulesmd.ini文件以开始编辑<br>
    3. 保存描述：将表格中描述部分的修改保存到本软件<br>
    4. 全局设置：rulesmd.ini里的游戏全局设置，如初始金钱，战争迷雾等<br>
    5. 另存为：将当前修改的rulesmd.ini另存为一个文件<br>
    6. 保存修改：将当前修改保存到打开的rulesmd.ini中<br>
    '''
    gui.textBrowser_help.setText(help_info)
    gui.show()
    sys.exit(app.exec_())
