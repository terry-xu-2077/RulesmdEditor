from os.path import exists
from json import dumps as js_dumps
from json import loads as js_loads
from PyQt5 import QtCore, QtGui


def dictToQSS(item):
    return str(item).replace("'", '').replace(",", ';')[1:-1] + ';'


class myJson(dict):
    def __init__(self, json_file):
        self.json_file = json_file
        json_data = {}
        if exists(self.json_file):
            with open(self.json_file, 'r', encoding='utf-8') as f:
                json_data = js_loads(f.read())
                f.close()
        super(myJson, self).__init__(json_data)

    def save(self):
        with open(self.json_file, 'w', encoding='utf-8') as f:
            f.write(js_dumps(self, indent=4, ensure_ascii=False))
            f.close()


class myQTheme():
    def __init__(self, config='', icons='', icon_size=0):
        self.color = myJson(config)
        self.iconsRaw = None
        self.iconsFile = icons
        self.icon_size = icon_size

        if not exists(config):
            self.__init_color()

        if self.iconsFile:
            self.iconsRaw = QtGui.QImage(self.iconsFile)
            self.icon_Max_pos = [self.iconsRaw.width() // self.icon_size, self.iconsRaw.height() // self.icon_size]

    def set_Widget_icon(self, widget, icon_pos):
        widget.setIcon(QtGui.QIcon(self.get_icon_pixmap(icon_pos)))

    def get_checkbox_QSS(self, color=True):
        if color:
            pos1 = 6, 1
            pos2 = 5, 1
        else:
            pos1 = 1, 4
            pos2 = 0, 4

        qss_image = '''
        QCheckBox::indicator:unchecked{{ {0} }}
        QCheckBox::indicator:checked{{ {1} }}
        '''

        image1 = 'border-image: url({0}) {1}; ' \
                 'border: -2px; width: 32px; height: 32px;'.format(self.iconsFile, self.__get_icon_clip(pos1))

        image2 = 'border-image: url({0}) {1}; ' \
                 'border: -2px; width: 32px; height: 32px;'.format(self.iconsFile, self.__get_icon_clip(pos2))

        qss_image = qss_image.format(image1,image2)

        qss_color = ''
        if color:
            qss_color ='''
            QCheckBox{{ color:{0}; }}
            QCheckBox:hover{{ color:{1}; }}
            '''
            qss_color  = qss_color.format(self.color['win-text-color'], self.color['win-light-color'])
        return qss_image + qss_color

    def get_button_QSS(self, key=False, keyNmae='key'):
        if key:
            btn = {
                "font-size": '14px',
                "font-weight": "normal",
                "background": self.color['key-button-bg-color'],
                "color": self.color['key-button-color'],
            }
            btn_hover = {
                "background": self.color['key-button-hover-color'],
                "color": self.color['key-button-color'],
            }
            qss = '''
                QPushButton[name={0}]{{ {1} }}
                QPushButton[name={0}]:hover{{ {2} }}
                '''.format(keyNmae, dictToQSS(btn), dictToQSS(btn_hover))
        else:
            btn = {
                "font-size": '12px',
                "font-weight": "normal",
                "background": self.color['button-bg-color'],
                "color": self.color['button-color'],
            }
            btn_hover = {
                "background": self.color['button-hover-color'],
                "color": self.color['button-color'],
            }
            qss = '''
                QPushButton{{ {0} }}
                QPushButton:hover{{ {1} }}
                '''.format(dictToQSS(btn), dictToQSS(btn_hover))
        return qss

    def get_menu_QSS(self, tail=False, tailNmae='value'):
        menubar = {
            "background-color": self.color['button-bg-color'],
            "selection-background-color": self.color['button-hover-color'],
            "selection-color": self.color['button-color'],
            "color": self.color['button-color'],
        }
        if tail:
            menu = {
                "background-color": '#ffffff',
                "selection-background-color": '#de5004',
                "selection-color": '#ffffff',
                "color": '#000000',
            }
            qss = '''
            QMenu[name={0}]{{ {1} }}
            QMenu{{ {2} }}
            '''.format(tailNmae, dictToQSS(menu), dictToQSS(menubar))
        else:
            qss = 'QMenu{{ {0} }}'.format(dictToQSS(menubar))
        return qss

    def get_table_qss(self):
        # QTablewidget只显示横分割线，不显示竖分割线
        # 思路就是隐藏自带的分割线，设置每个item的下边线的颜色
        qss_QTableWidget = {
            "border-style": "solid",
            "border-width": "1px",
            'border-color': self.color['win-border-color']
        }
        qss_QTableWidget_item = {
            'border': '1px solid rgb(255,0,0)',
            'border-bottom': '1px solid rgb(255,0,0)'
        }
        qss = '''
        QTableWidget{{ {0} }}
        QTableWidget::Item{{ {1} }}
        '''.format(dictToQSS(qss_QTableWidget), dictToQSS(qss_QTableWidget_item))
        return qss


    def get_combobox_QSS(self):

        box = {
            "background-color": self.color['combobox-bg-color'],
            "color": self.color['combobox-fg-color'],
        }

        qss = 'QComboBox{{ {0} }}'.format(
            dictToQSS(box),
        )
        return qss

    def get_icon_pixmap(self, icon_pos=(0, 0),scale=None):
        rect = QtCore.QRect(
            self.icon_size * icon_pos[0],
            self.icon_size * icon_pos[1],
            self.icon_size,
            self.icon_size
        )
        icon = QtGui.QPixmap.fromImage(self.iconsRaw.copy(rect))
        if scale != None:
            return icon.scaled(*scale, QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.SmoothTransformation)
        else:
            return icon

    def get_Qicon(self,icon_pos):
        return QtGui.QIcon(self.get_icon_pixmap(icon_pos))

    def get_ALL_QSS(self):
        qss_Qwidget = {
            "background-color": self.color['win-bg-color'],
            "selection-background-color": self.color['win-selection-bg-color'],
            "selection-color": self.color['win-selection-fg-color'],
            "color": self.color['win-text-color'],
            "font-family": self.color['win-font-family']
        }
        qss_QLineEdit = {
            "border-style": "solid",
            "border-width": "1px",
            'color': self.color['win-text-color'],
            'border-color': self.color['win-border-color']
        }
        qss_QTextBrowser = {
            "border-style": "solid",
            "border-width": "1px",
            "font-size": '14px',
            'color': self.color['win-text-color'],
        }

        all_QSS = '''
        *{{ {0} }}
        QTextBrowser{{ {1} }}
        QLineEdit,QTextBrowser,QtextEdit{{ {2} }}
        '''.format(dictToQSS(qss_Qwidget),
                   dictToQSS(qss_QTextBrowser),dictToQSS(qss_QLineEdit))

        all_QSS += self.get_checkbox_QSS()
        all_QSS += self.get_button_QSS()
        all_QSS += self.get_button_QSS(True)
        all_QSS += self.get_combobox_QSS()
        all_QSS += self.get_menu_QSS()
        all_QSS += self.get_table_qss()
        all_QSS += self.get_menu_QSS(True)
        result_list = []
        for i in all_QSS.split('\n'):
            if i != '':
                result_list.append(i.strip().replace('\n', '') + '\n')
        result = ''.join(result_list).replace('{ ', '{\n').replace('; ', ';\n').replace(' }', '\n}')
        return result

    def __get_icon_clip(self, icon_pos):
        clip_top = icon_pos[1] * self.icon_size
        clip_right = (self.icon_Max_pos[0] - icon_pos[0] - 1) * self.icon_size
        clip_down = (self.icon_Max_pos[1] - icon_pos[1] - 1) * self.icon_size
        clip_left = icon_pos[0] * self.icon_size
        return '{} {} {} {}'.format(clip_top, clip_right, clip_down, clip_left)

    def __init_color(self):
        # 全局
        self.color['win-border-color'] = "#9c9b9c"
        self.color['win-statusbar-color'] = "#FF9DEA"
        self.color['win-bg-color'] = "#242c47"
        self.color['win-light-color'] = "#c9c900"
        self.color['win-text-color'] = "#B3EFE6"
        self.color['win-selection-bg-color'] = "#182244"
        self.color['win-selection-fg-color'] = "#efef00"
        self.color['win-font-family'] = 'Microsoft Yahei'
        # section
        self.color['section-bg-color'] = '#36426b'
        self.color['section-fg-color'] = '#FFFFFF'

        # option
        self.color['option-bg-color'] = '#1b2b65'
        self.color['option-fg-color'] = '#FFFFFF'

        # 主按钮
        self.color['key-button-bg-color'] = '#1b2b65'
        self.color['key-button-hover-color'] = "#2d4bb3"
        self.color['key-button-color'] = "#FFFFFF"
        # 按钮
        self.color['button-bg-color'] = '#1b2b65'
        self.color['button-hover-color'] = "#2d4bb3"
        self.color['button-color'] = "#FFFFFF"

        # option_combobox
        self.color['combobox-bg-color'] = self.color['key-button-bg-color']
        self.color['combobox-fg-color'] = '#FFFFFF'
        # self.color['combobox-selection-bg-color'] = self.color['key-button-color']
        # self.color['combobox-selection-fg-color'] = '#FFFFFF'

        #self.color.save()
