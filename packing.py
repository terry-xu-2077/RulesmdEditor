import os
import shutil
import time
from PyInstaller.__main__ import run

if __name__ == '__main__':
    '''
    -F, --onefile Py代码只有一个文件
    -D, --onedir Py代码放在一个目录中（默认是这个）
    -K, --tk 包含TCL/TK
    -d, --debug 生成debug模式的exe文件
    -w, --windowed, --noconsole 窗体exe文件(Windows Only)
    -c, --nowindowed, --console 控制台exe文件(Windows Only)
    -o DIR, --out=DIR 设置spec文件输出的目录，默认在PyInstaller同目录
    --icon=<FILE.ICO> 加入图标（Windows Only）
    -v FILE, --version=FILE 加入版本信息文件
    --upx-dir, 压缩可执行程序
    
    pipenv shell 进入虚拟环境
    pipenv run python 进入虚拟环境中的python
    '''
    shutil.rmtree('dist/RulesEditor')

    py_name = 'RulesEditor.pyw'
    time_key = '最终编译时间'
    time_str = time.strftime('%Y-%m-%d %H:%M')

    with open('main.pyw', 'r', encoding='utf-8') as f:
        py_file = f.read()
        f.close()

    with open(py_name, 'w', encoding='utf-8') as f:
        f.write(py_file.replace(time_key, 'Terry ' + time_str))
        f.close()

    opts = [py_name, '-D', '-w', '--icon=Resources/app.ico']
    run(opts)

    shutil.copytree('Resources', 'dist/RulesEditor/Resources')
