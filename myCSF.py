from ctypes import *
from os.path import exists


# https://pan.baidu.com/s/1hmR5HtLFpFcoKbCYsquhZw#list/path=%2F
# 9qhg

# todo:https://blog.csdn.net/qiximenghu/article/details/127171188

class myCSF():
    stateDict = {
        0: 'CSF被正常读取',
        32767: '正常读取且仅读取了主CSF且加载成功',
        114514: '无效的主CSF路径或不是绝对路径',
        1919810: '在加载额外CSF时额外CSF路径无效或不是绝对路径'
    }

    autoSave_id = 1
    closeFile_id = 2
    editFile_id = 3
    initCSF_id = 4
    sortList_id = 5
    getStr_id = 6

    csf_ready = False
    ares_num = 0

    def __init__(self):
        self.CSFDLL = cdll.LoadLibrary('.\Resources\CSFDLL.dll')

    def AutoSave(self):
        '''
        :return: 保存，失败返回-1
        '''
        self.CSFDLL[self.autoSave_id].restypes = c_int
        return self.CSFDLL[self.autoSave_id]()

    def CloseCSFFile(self):
        '''
        :return: 正常为0，关闭失败为不定非0数值
        '''
        self.CSFDLL[self.closeFile_id].restypes = c_int
        return self.CSFDLL[self.closeFile_id]()

    def EditCSFFile(self, mode, Label, UT):
        '''
        :param mode:整型，0为添加或修改，1为删除，撤销和重做（参数＞1的整数时，重做，参数1为 n 时重做 n-1 步，参数＜0整数时，撤销，撤销 -n 步）
        :param Label:操作对象标签，是字符指针
        :param UT:操作对象存入字符串，内容为Unicode格式，必须以Unicode字串的默认结尾00 00结尾，是字符指针，仅参数1为0时有效，建议在给参数时才由Unicode字符串转为普通字符指针
        :return: 当参数1为0或1时，返回操作次数计数器的数值，如果溢出最大值，返回-1
        '''
        self.CSFDLL[self.editFile_id].argtypes = [c_int, POINTER(c_char_p), POINTER(c_char_p)]
        self.CSFDLL[self.editFile_id].restypes = c_int
        return self.CSFDLL[self.editFile_id](mode, bytes(Label, encoding='utf-8'),
                                             bytes(UT.encode('unicode_escape').decode(), encoding='utf-8'))

    def InitCSFFile(self, file, model=0, extPath=''):
        '''
        :param file: CSF的绝对路径
        :param model:
            0 只加载主要CSF
            1 加载主要CSF和同目录的Ares的增强CSF
            2 加载主要CSF和额外CSF，额外CSF是由第三个参数指定绝对路径的一个CSF
            3 同时加载所有的主要CSF，Ares增强CSF，额外CSF
        :param extPath: 指定额外CSF的绝对路径的，格式同参数1
        '''
        if exists(file):
            if file.rfind('.csf') != -1:
                self.CSFDLL[self.initCSF_id].argtypes = [c_char_p, c_int, c_char_p]
                self.CSFDLL[self.initCSF_id].restypes = c_int
                state_id = self.CSFDLL[self.initCSF_id](bytes(file, encoding='utf-8'), model, extPath)
                self.state = state_id
                if state_id != 0 and state_id != 32767:
                    raise Exception(self.stateDict.get(state_id), state_id)
                else:
                    self.csf_ready = True
                    self.ares_num = state_id
                return

        raise Exception('csf文件地址不正确', file)

    def SortList(self):
        pass

    def GetStringValue(self, UIName):
        '''
        :param UIName: 待查找的CSF条目的名称
        :return:返回查询的字符串
        '''
        self.CSFDLL[self.getStr_id].argtypes = [POINTER(c_char_p)]
        self.CSFDLL[self.getStr_id].restypes = POINTER(c_char_p)

        try:
            p = self.CSFDLL[self.getStr_id](bytes('Name:' + UIName, encoding='utf-8'))
        except:
            raise Exception('获取失败，可能是CSF文件地址有误。')

        try:
            result = wstring_at(p)
            return result
        except:
            if p == 0:
                raise Exception('获取失败，找不到相关信息。', 0)
            else:
                raise Exception('获取失败：', p)


if __name__ == '__main__':

    edit_csf = myCSF()
    print('初始化完成，准备就绪')
    csf_file = r'E:\Pojects\Python\Teri\rulesmd_Editer\ra2md.csf'  # input('请输入一个csf文件的路径：')
    edit_csf.InitCSFFile(csf_file)

    # NAREFN 毛子礦場

    if edit_csf.csf_ready:
        while True:
            text = input('请输入要修改的Name：')
            try:
                value = edit_csf.GetStringValue(text)
                print('当前：{} = {}'.format(text, value))
                new = input('请输入一个新的值以替换：')
                rep = edit_csf.EditCSFFile(0, text, new)
            except Exception as e:
                print(e)
                new = input('没有找到此标签，输入一个值以新建：')
                input('确定新建吗？：{} = {}'.format(text, new))
                rep = edit_csf.EditCSFFile(0, text, new)
            print('EditCSFFile', rep)
            print('AutoSave', edit_csf.AutoSave())
            print('CloseCSFFile', edit_csf.CloseCSFFile())
            break
