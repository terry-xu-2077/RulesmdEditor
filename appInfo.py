import json
import os.path
import random
from datetime import datetime
from threading import Thread

import requests
import wmi
import hashlib


def get_platform_hash():
    info = []
    name = ''
    m = hashlib.md5()
    w = wmi.WMI()
    #
    # for x in w.Win32_Processor():
    #     info2.append(x.Name)

    for x in w.Win32_DiskDrive():
        info.append(x.Caption)
        info.append(x.Size)
        break

    for x in w.Win32_NetworkAdapterConfiguration(DHCPEnabled='TRUE', IPEnabled='TRUE'):
        info.append(x.Description)
        info.append(x.MACAddress)
        name = x.DNSHostName
        break

    for x in w.Win32_BIOS():
        info.append(x.SerialNumber)
        info.append(' '.join(x.BIOSVersion))

    m.update(' '.join(info).encode())
    return [m.hexdigest(), name]


def read_hash_info():
    path = os.environ['tmp'] + '/appInfoHash.json'
    if os.path.exists(path):
        # print('read')
        with open(path, 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
            f.close()
            return data['hash_info']
    else:
        # print('write')
        data = {'hash_info': get_platform_hash()}
        with open(path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data))
            f.close()
            return data['hash_info']


user_hash = read_hash_info()
#host = '127.0.0.1:7788'
host = 'teri.work:7788'
post_url = 'rules_editor_info'


def get_now_time_name():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def get_now_timestamp():
    return datetime.now().strftime("%Y%m%d-%H:%M:%S")


def td_requests(info, code):
    req = None
    try:
        if code == 'json':
            info['title'] = get_now_time_name()
            req = requests.post('http://{}/{}'.format(host, post_url), data=json.dumps(info).encode())

        elif code == 'log':
            info['title'] = get_now_time_name()
            req = requests.post('http://{}/{}'.format(host, post_url), data=json.dumps(info).encode())

        elif code == 'file':
            fileName = '{}={}'.format(info['user'][0], os.path.split(info['fileName'])[1])
            req = requests.post(
                'http://{}/pr_subtitler'.format(host),
                files={'file': (fileName, open(info['fileName'], 'rb'))},
            )
        if req: print(req.text)

    except Exception as e:
        print(e)


def send_to_server(info, code='json'):
    Thread(target=td_requests, args=(info, code)).start()


if __name__ == '__main__':
    #print(read_hash_info())
    for i in range(10):
        print(random.random())
