# /usr/bin/env python3.5
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import os
import random
import urllib

# 创建一个文件夹
img_dir = 'jiandanxxoo1207'
if not os.path.isdir(img_dir):
    os.mkdir(img_dir)

headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Cooike':'Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1480941570; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1481092056; Hm_lvt_80cbcbf4e9167bc878bc1158463bab9d=1481091389; Hm_lpvt_80cbcbf4e9167bc878bc1158463bab9d=1481101033; _ga=GA1.2.1971724788.1480941570; jdna=01b0531fab6a989460dd1b231010b496#1481123304513'
}

def main():
    ran = random.randint(1,2000)
    for page in range(ran):
        time.sleep(5)
        url = 'http://i.jandan.net/ooxx/page-{}'.format(page)
        wb_data = requests.get(url, headers = headers)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        imgs = soup.select('p > img')

        for img_url in imgs:
            url = img_url.get('src')
            print(url)

def download(url):
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        return
    filename = url.split('.')[2].split('/')[-2]

    target = './{}.jpg'.format(filename)

    with open(target, 'wb') as fs:
        fs.write(r.content)

    print('%s => $s'%(url, target))

if __name__ == '__main__':
    main()