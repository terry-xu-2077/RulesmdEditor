from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import sys

class myComboBox_checkList(QComboBox):
    model_normal = 0
    model_checkbox = 1
    selection_changed = QtCore.pyqtSignal(list)
    def __init__(self,parent=None):
        super(myComboBox_checkList, self).__init__(parent)
        self.activated.connect(self.ChangedEvent)
        self.myWidgetsList = []
        self.option = ''
        self.itemsValue = []

    def addCheckBoxes(self,items,select_list=None):
        self.model = self.model_checkbox
        self.myLineEdit = QLineEdit()
        self.setLineEdit(self.myLineEdit)
        self.myLineEdit.mouseReleaseEvent = self.myclicked
        self.items = items
        self.rowCount = len(items)
        self.myWidgetsList = []
        self.listView = QListWidget()
        for i, text in enumerate(self.items):
            self.myWidgetsList.append(QCheckBox())
            self.myWidgetsList[i].setText(text[1])
            self.itemsValue.append(text[0])

            if select_list is not None:
                if text[1] in select_list or i in select_list:
                    self.myWidgetsList[i].setChecked(True)

            self.myWidgetsList[i].clicked.connect(self.show_selection)
            self.myWidgetsList[i].mouseReleaseEvent = self.item_clicked
            list_item = QListWidgetItem(self.listView)
            self.listView.setItemWidget(list_item, self.myWidgetsList[i])
        self.setModel(self.listView.model())
        self.setView(self.listView)
        self.show_selection()

    def ChangedEvent(self,event=None):
        if self.myWidgetsList:
            self.selection_changed.emit([self.option,self.get_selection_value()])
        else:
            self.selection_changed.emit([self.option, self.get_selection_value()])

    def get_selection(self, num=False):
        selection_list = []
        if self.model == self.model_checkbox:
            for i in range(self.rowCount):
                item = self.myWidgetsList[i]
                if item.isChecked():
                    if num:
                        selection_list.append(i)
                    else:
                        selection_list.append(item.text())
            return selection_list
        else:
            index = self.currentIndex()
            if num:
                return [index]
            else:
                return [self.currentText()]
        return []

    def get_selection_value(self):
        index = self.get_selection(True)
        value = []
        for i in index:
            value.append(self.itemsValue[i])
        return ','.join(value)

    def show_selection(self):
        if self.model == self.model_checkbox:
            self.myLineEdit.clear()
            self.myLineEdit.setReadOnly(False)
            names = []
            for i in self.get_selection(True):
                item = self.myWidgetsList[i]
                names.append(item.text())
            if names:
                self.myLineEdit.setText(', '.join(names))
            else:
                self.myLineEdit.setText('未选择')
            self.myLineEdit.setReadOnly(True)

    def item_clicked(self, event):
        item = self.myWidgetsList[self.listView.currentIndex().row()]
        if self.model == self.model_checkbox:
            item.setChecked(not item.isChecked())
            self.show_selection()
            self.ChangedEvent()

    def myclicked(self, event):
        self.showPopup()

    def addItems(self, items):
        self.itemsValue.clear()
        for i in items:
            self.addItemValue(i)

    def addItemValue(self, item):
        self.itemsValue.append(item[0])
        self.addItem(item[1])

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        e.ignore()
        pass

class myComboBox_sliderList(QComboBox):
    model_normal = 0
    model_checkbox = 1
    selection_changed = QtCore.pyqtSignal(list)
    def __init__(self,parent=None):
        super(myComboBox_sliderList, self).__init__(parent)
        self.activated.connect(self.ChangedEvent)
        self.myWidgetsList = []
        self.option = ''
        self.itemsValue = []

    def addCheckBoxes(self,items,select_list=None):
        self.model = self.model_checkbox
        self.myLineEdit = QLineEdit()
        self.setLineEdit(self.myLineEdit)
        self.myLineEdit.mouseReleaseEvent = self.myclicked
        self.items = items
        self.rowCount = len(items)
        self.myWidgetsList = []
        self.listView = QListWidget()
        for i, text in enumerate(self.items):
            self.myWidgetsList.append(QCheckBox())
            self.myWidgetsList[i].setText(text[1])
            self.itemsValue.append(text[0])

            if select_list is not None:
                if text[1] in select_list or i in select_list:
                    self.myWidgetsList[i].setChecked(True)

            self.myWidgetsList[i].clicked.connect(self.show_selection)
            self.myWidgetsList[i].mouseReleaseEvent = self.item_clicked
            list_item = QListWidgetItem(self.listView)
            self.listView.setItemWidget(list_item, self.myWidgetsList[i])
        self.setModel(self.listView.model())
        self.setView(self.listView)
        self.show_selection()

    def ChangedEvent(self,event=None):
        if self.myWidgetsList:
            self.selection_changed.emit([self.option,self.get_selection_value()])
        else:
            self.selection_changed.emit([self.option, self.get_selection_value()])

    def get_selection(self, num=False):
        selection_list = []
        if self.model == self.model_checkbox:
            for i in range(self.rowCount):
                item = self.myWidgetsList[i]
                if item.isChecked():
                    if num:
                        selection_list.append(i)
                    else:
                        selection_list.append(item.text())
            return selection_list
        else:
            index = self.currentIndex()
            if num:
                return [index]
            else:
                return [self.currentText()]
        return []

    def get_selection_value(self):
        index = self.get_selection(True)
        value = []
        for i in index:
            value.append(self.itemsValue[i])
        return ','.join(value)

    def show_selection(self):
        if self.model == self.model_checkbox:
            self.myLineEdit.clear()
            self.myLineEdit.setReadOnly(False)
            names = []
            for i in self.get_selection(True):
                item = self.myWidgetsList[i]
                names.append(item.text())
            if names:
                self.myLineEdit.setText(', '.join(names))
            else:
                self.myLineEdit.setText('未选择')
            self.myLineEdit.setReadOnly(True)

    def item_clicked(self, event):
        item = self.myWidgetsList[self.listView.currentIndex().row()]
        if self.model == self.model_checkbox:
            item.setChecked(not item.isChecked())
            self.show_selection()
            self.ChangedEvent()

    def myclicked(self, event):
        self.showPopup()

    def addItems(self, items):
        self.itemsValue.clear()
        for i in items:
            self.addItemValue(i)

    def addItemValue(self, item):
        self.itemsValue.append(item[0])
        self.addItem(item[1])

    def wheelEvent(self, e: QtGui.QWheelEvent) -> None:
        e.ignore()
        pass


class test_win(QWidget):
    def __init__(self):
        super(test_win, self).__init__()
        self.setWindowTitle('自定义下拉框测试')
        self.resize(500, 250)
        items = [['value_%d'%i,'第{}项'.format(i)] for i in range(10)]

        self.mylayout = QGridLayout()
        self.combobox = myComboBox_checkList()
        self.combobox.addCheckBoxes(items)
        self.combobox.selection_changed.connect(self.combobox_changed)
        self.combobox2 = myComboBox_checkList()
        self.combobox2.addItems(items)
        self.combobox2.selection_changed.connect(self.combobox_changed)
        self.btn = QPushButton(self)
        self.btn.setText('显示')
        self.btn.clicked.connect(self.btn_clicked)
        self.btn.setMaximumSize(QtCore.QSize(120, 30))
        space1 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.mylayout.addWidget(self.combobox, 0, 0)
        self.mylayout.addWidget(self.btn, 0, 1)
        self.mylayout.addWidget(self.combobox2, 1, 0, 1, 0)
        self.mylayout.addItem(space1, 2, 0)
        self.setLayout(self.mylayout)

    def btn_clicked(self):
        print(self.combobox.get_selection(False))

    def combobox_changed(self,info):
        print(info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setStyle('Fusion')
    gui = test_win()
    gui.show()
    sys.exit(app.exec_())
