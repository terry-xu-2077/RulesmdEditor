from json import dumps as js_dumps
from json import loads as js_loads
import os
import time
import re

class myTools():
    @staticmethod
    def is_number(text: str):
        try:
            float(text)
            if '.' in text:
                return 0  # 浮点
            else:
                return 1  # 整数
        except:
            if '%' in text:
                return 2  # 百分比
            else:
                try:
                    float(text.replace(',', ''))
                    return 1  # 整数
                except:
                    pass
        return -1

    @staticmethod
    def format_time(seconds):
        sec = int(seconds)
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        return "%02d时:%02d分:%02d秒" % (h, m, s)

    @staticmethod
    def is_chinese(text):
        for ch in text:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False

    @staticmethod
    def format_dict(item):
        return str(item).replace("'", '').replace(",", ';')[1:-1]

    @staticmethod
    def progressbar(total, temp, text='', lenght=40):
        if not text:
            text = '总计:{0},当前:{1} &&'.format(total, temp)
        content = '\r' + text.strip().replace('&&', '[{0}{1}]{2}%')
        percentage = round(temp / total * 100, 2)
        a = round(temp / total * lenght)
        b = lenght - a
        print(content.format('■' * a, '□' * b, percentage), end='')

    @staticmethod
    def get_current_timeStr():
        return time.strftime('%Y-%m-%d-%H-%M', time.localtime())

    @staticmethod
    def addToClipboard(string):
        from tkinter import Tk
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(string)
        r.update()
        r.destroy()

    @staticmethod
    def getClipboard():
        "返回剪贴板上的内容"
        from tkinter import Tk
        r = Tk()
        r.withdraw()
        tmp = r.clipboard_get()
        r.destroy()
        return tmp

    @staticmethod
    def space_text(text):
        pattern = '[A-Z]'
        newText = re.sub(pattern, lambda x: ' ' + x.group(0), text)
        return newText

class myJson(dict):
    def __init__(self, json_file=None, data=None):
        self.json_file = json_file

        json_data = {}
        if data != None:
            json_data = data

        if json_file != None:
            if os.path.exists(self.json_file):
                with open(self.json_file, 'r', encoding='utf-8') as f:
                    json_data = js_loads(f.read())
                    f.close()
        super(myJson, self).__init__(json_data)

    def save(self, file=None):
        if file != None:
            self.json_file = file
        with open(self.json_file, 'w', encoding='utf-8') as f:
            f.write(js_dumps(self, indent=4, ensure_ascii=False))
            f.close()

    def find_value_index(self, key):
        result = self.__find_value(key)
        if result != None:
            for item in result:
                item.reverse()
            return result
        return None

    def __find_value(self, key, subDict=None, path=None, index=None):
        if subDict == None:
            key_path = []
            key_index = []
            for i, k in enumerate(self.items()):

                value = self.__find_value(key, subDict=k[1], path=key_path, index=key_index)
                if value:
                    key_path.append(k[0])
                    key_index.append(i)
                    return value
        else:
            if type(subDict) == dict:
                for i, k in enumerate(subDict.items()):
                    if type(k[1]) != dict:
                        if key == k[1].split('.')[-1]:
                            path.append(k[0])
                            index.append(i)
                            return [path, index]
                    else:
                        value = self.__find_value(key, subDict=k[1], path=path, index=index)
                        if value:
                            path.append(k[0])
                            index.append(i)
                            return value
