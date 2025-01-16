from configparser3 import ConfigParser as Cfg
import configparser

class myConfig(Cfg):
    file = ''
    def __init__(self, file='',encoding='utf-8'):
        super(myConfig, self).__init__(defaults=None, strict=False, interpolation=None, allow_no_value=True)
        if file:
            self.file = file
            self.read(file,encoding=encoding)

    def optionxform(self, optionstr: str) -> str:
        return optionstr

    def write_file(self, file=None):
        if file == None:
            file = self.file
        self.write(open(file, 'w'), space_around_delimiters=False)

class RA2_INI():
    '''
    iniType: 0 原版，1 ares, 2 npse
    '''
    iniType = 0
    def __init__(self,ini_file):
        #self.iniData = myConfig(ini_file,encoding='utf-8')
        self.iniData = configparser.ConfigParser().read(ini_file)

    def test(self):
        for k in self.iniData.keys():
            print(self.iniData[k])

if __name__ == '__main__':
    ini = RA2_INI('XXX/rulesmd-x.ini')
    ini.test()