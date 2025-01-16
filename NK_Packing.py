import os
import shutil
import time
import subprocess

if __name__ == '__main__':
    try:
        shutil.rmtree('dist')
    except:
        pass

    py_name = 'RulesEditor.pyw'
    time_key = '最终编译时间'
    time_str = time.strftime('%Y-%m-%d %H:%M')

    with open('rulesmdEditor.pyw', 'r', encoding='utf-8') as f:
        py_file = f.read()
        f.close()

    with open(py_name, 'w', encoding='utf-8') as f:
        f.write(py_file.replace(time_key, 'Teri ' + time_str))
        f.close()

    # https://blog.csdn.net/ha_lee/article/details/124175341
    # https://zhuanlan.zhihu.com/p/133303836

    cmd = [
        'nuitka',
        '--mingw64',
        '--standalone',
        '--show-progress',
        '--show-memory',
        '--enable-plugin=pyqt5',
        '--output-dir=out',
        '--windows-icon-from-ico={}'.format('Resources/app.ico'),
        py_name
    ]
    print('打包中：', ' '.join(cmd))
    subprocess.Popen(' '.join(cmd),shell=True)
