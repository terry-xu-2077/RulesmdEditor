from configobj import ConfigObj as cfgObj


class myConfigObj(cfgObj):
    def __init__(self, file=''):
        try:
            super(myConfigObj, self).__init__(file, write_empty_values=True)
        except:
            try:
                super(myConfigObj, self).__init__(file, write_empty_values=True, encoding='gbk')
            except:
                pass

    def get(self, section, option):
        '''
        获取section中option的值,没有返回 None
        :param section:
        :param option:
        :return:
        '''
        return self[section][option]

    def set(self, section, option, value):
        '''
        设置section下的option的值，如果此option不存在，则新建
        :param section:
        :param option:
        :param value:
        :return:
        '''
        self[section][option] = value

    def items(self, section):
        '''
        返回section下的所有键值对(option,value)
        :param section:
        :return:
        '''
        return self[section].items()

    def sections(self):
        '''
        返回所有section名称
        :return:
        '''
        return self.keys()

    def has_option(self, section, option):
        '''
        名为section中指定option是否存在
        :param section:
        :param option:
        :return:
        '''
        try:
            if self[section][option]:
                return True
        except:
            return False

    def has_section(self, section):
        '''
        section是否存在
        :param section:
        :return:
        '''
        try:
            if self[section]:
                return True
        except:
            return False

    def add_section(self, section):
        '''
        添加新section
        :param section:
        :return:
        '''
        self[section] = {}

    def remove_section(self, section):
        '''
        删除section
        :param section:
        :return:
        '''
        del self[section]

    def remove_option(self, section, option):
        '''
        删除option
        :param section:
        :param option:
        :return:
        '''
        del self[section][option]

    def writ_file(self, file=None):  # 写入到文件，如果参数指定了文件名，则使用，反之用读取的地址
        if file != None:
            self.filename = file
        self.write()
