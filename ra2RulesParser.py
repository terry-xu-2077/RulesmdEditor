import re
import random
import os


def isItem(txt):
    try:
        if txt[0] in ';#；*':
            return False
        my_re = re.compile(r'.=', re.S)
        res = re.findall(my_re, txt)
        if len(res):
            return True
        else:
            return False
    except:
        return False


def isSection(txt):
    try:
        if txt[0] == '[':
            my_re = re.compile(r'\[.*?\]', re.S)
            res = re.findall(my_re, txt)
            if len(res):
                return True
            else:
                return False
        else:
            return False
    except:
        return False


def get_section_name(txt):
    data = [re.findall(r'\[(.*?)\]', txt)[0], '']
    if ';' in txt:
        data[1] = txt.split(';')[1].strip()
    return data


class rulesParser:
    def __init__(self, fileName='', readDesc=False):
        self.rawList = []
        self.rawDict = {}
        self.descDict = {}
        self.file = ''
        self.head = None
        self.readDesc = readDesc
        self.encoding = 'utf-8'
        if fileName:
            self.read_file(fileName)

    def read_file(self, fileName):
        self.file = fileName
        if not os.path.exists(fileName):
            return
        try:
            with open(fileName, 'r', encoding=self.encoding) as f:
                self.rawList = f.readlines()
                f.close()
        except:
            self.encoding = 'gbk'
            with open(fileName, 'r', encoding=self.encoding) as f:
                self.rawList = f.readlines()
                f.close()
        self.__parser()
        self.rawList.clear()

    def read_lines(self, line_list):
        self.rawList = line_list
        self.__parser()
        self.rawList.clear()

    def __parser(self):
        self.head = None
        self.rawDict.clear()
        self.descDict.clear()
        skip = 0
        rawLen = len(self.rawList)
        for i in range(rawLen):
            if i + skip >= rawLen:
                break
            line = self.rawList[i + skip]
            if isSection(line):
                if self.head is None:
                    self.head = self.rawList[:i]
                sectionData = get_section_name(line)
                section = sectionData[0]
                section_name = section
                option_lines_id = []
                for x in range(i + skip + 1, rawLen):
                    if x + 1 < rawLen and isSection(self.rawList[x + 1]):
                        if self.rawList[x][0] == ';':
                            next_section = self.rawList[x + 1][1:-2]
                            self.descDict.setdefault(next_section, {'section': self.rawList[x][1:-1]})
                        else:
                            option_lines_id.append(x)
                        skip = x - i
                        break
                    option_lines_id.append(x)
                if self.rawDict.get(section_name):
                    section_name += ':{}'.format(random.randint(0, 1000))
                if sectionData[1]:
                    self.descDict.setdefault(section_name, {'section': sectionData[1]})
                optionsData = self.__get_option_data(option_lines_id)
                self.descDict.setdefault(section_name, {'options': optionsData[1]})
                self.rawDict.setdefault(section_name, {'name': section, 'options': optionsData[0]})

    def __get_option_data(self, lines_id):
        optionsDict = {}
        optionsDesc = {}
        for i in lines_id:
            strData = self.__line_to_data(i)
            if strData:
                optionsDict.setdefault(strData[0], strData[1])
                if len(strData) == 3:
                    optionsDesc.setdefault(strData[0], strData[2])

        return [optionsDict, optionsDesc]

    def __line_to_data(self, num):
        strData = self.rawList[num].rstrip()
        if isItem(strData):
            sp = strData.split('=')
            option = sp[0]
            value = sp[1]
            desc = ''
            if ';' in sp[1]:
                x = sp[1].split(';')
                value = x[0].rstrip()
                desc = x[1].rstrip()
            return [option, value, desc]
        else:
            if self.readDesc:
                return ['rules:{}'.format(random.randint(0, 1000)), strData]
            else:
                return []

    def __bool__(self):
        return bool(self.rawDict)

    def __getitem__(self, key):
        items = {}
        if self.rawDict.get(key) is None:
            return None
        for k in self.rawDict[key]['options'].keys():
            if k.split(':')[0] == 'rules':
                continue
            items.setdefault(k, self.rawDict[key]['options'][k])
        return items

    def __setitem__(self, key, value):
        self.rawDict[key]['options'] = value

    def __delitem__(self, key):
        del self.rawDict[key]

    def setboolean(self, section, option, value):
        if value:
            self.rawDict[section]['options'][option] = 'true'
        elif not value:
            self.rawDict[section]['options'][option] = 'false'
        else:
            print('错误，不是布尔值')

    def getboolean(self, section, option):
        try:
            b = self.rawDict[section]['options'][option].lower()
            if b in ['true', '1', 'yes']:
                return True
            elif b in ['false', '0', 'no']:
                return False
            else:
                print('不是布尔值')
                return None
        except Exception as err:
            print(err)
            return None

    def get_section_desc(self, section):
        try:
            return self.descDict[section]['section']
        except:
            return None

    def get_option_desc(self, section, option):
        try:
            return self.descDict[section]['options'][option]
        except:
            return ''

    def sections(self):
        return list(self.rawDict.keys())

    def options(self, section):
        return list(self.rawDict[section]['options'].keys())

    def items(self, section):
        items = []
        for k in self.rawDict[section]['options'].keys():
            if k.split(':')[0] == 'rules':
                continue
            items.append([k.strip(), self.rawDict[section]['options'][k].strip()])
        return items

    def has_section(self, section):
        return section in self.rawDict

    def has_option(self, section, option):
        try:
            return option in self.rawDict[section]['options']
        except:
            return False

    def get(self, section, option):
        try:
            return self.rawDict[section]['options'][option].strip()
        except:
            return None

    def set(self, section, option, value=None, desc=''):
        try:
            self.rawDict[section]['options'][option] = value
        except:
            self.rawDict.setdefault(section, {'name': section, 'options': {option: value}})
        if desc:
            section_desc = self.descDict.get(section)
            if section_desc.get('options'):
                section_desc['options'][option] = desc
            else:
                section_desc.setdefault('options', {option: desc})

    def add_section(self, section, desc=''):
        self.rawDict[section] = {'name': section, 'options': {}}
        if desc:
            self.descDict.setdefault(section, {'section': desc})

    def remove_section(self, section):
        del self.rawDict[section]

    def remove_option(self, section, option):
        del self.rawDict[section]['options'][option]

    @staticmethod
    def __options_to_list(options, optionDesc=None):
        optionsList = []
        for k in options.keys():
            if k.split(':')[0] == 'rules':
                optionsList.append(options[k] + '\n')
                continue
            strData = k + '=' + options[k]
            if optionDesc:
                desc = optionDesc.get(k)
                if desc:
                    strData += '        ; {}'.format(desc)
            strData += '\n'
            optionsList.append(strData)
        if optionsList[-1] == '\n':
            return optionsList[:-1]
        else:
            return optionsList

    def __dict_to_list(self, key):
        lines = []
        try:
            lines.append(';{}\n'.format(self.descDict[key]['section']))
        except:
            pass
        lines.append('[{}]\n'.format(self.rawDict[key]['name']))
        try:
            desc = self.descDict.get(key).get('options')
        except:
            desc = None
        lines.extend(self.__options_to_list(self.rawDict[key]['options'], desc))
        lines.append('\n')
        return lines

    def write_file(self, fileName='', ):
        if not self.rawDict:
            return
        file_lines = []
        if isinstance(self.head, list):
            file_lines.extend(self.head)
        for k in self.rawDict.keys():
            file_lines.extend(self.__dict_to_list(k))
        file = self.file
        if fileName:
            file = fileName
        with open(file, 'w', encoding=self.encoding) as f:
            f.writelines(file_lines)
            f.close()

    def export_section_lines(self, section):
        file_lines = self.__dict_to_list(section)
        return file_lines

    def replace_section(self, section, ini_object):
        self.__setitem__(section, ini_object[section])
        self.descDict[section] = ini_object.descDict[section]


if __name__ == '__main__':
    ini = rulesParser('Resources/OptionsDesc.ini')
    print(ini.rawDict)
