import base64
import os
import re

# name = "贴图链接小工具 - Terry徐制作"
# name2 = base64.b64encode(name.encode('utf-8')).decode("utf-8")
# print(name2)
# print(base64.b64decode(name2).decode('utf-8'))
texDir = r"E:\Assets\UserDownloaded\www_modown_cn_JZ_05\tex"
texFiles = []

names = ["AE17_05_roof",'AE17_05_roof_ornaments_2', 'AE17_05_Ulmus002', 'AE17_05_Ulmus002_001']

def reFix(text):
    try:
        int(text[-1])
        x = re.findall(r'\d+', text, )[-1]
        p = text.rfind(x)
        n = text[:p]
        if n[-1] == '_': n = n[:-1]
        return n
    except:
        return text


for n in names:
    n2 = n
    n2 = reFix(n)
    n2 = reFix(n2)
    print(n2)
