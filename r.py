#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: r.py

import requests

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
ua_m = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 Mobile/15B150 Safari/604.1'
header = {'User-Agent':ua_d}
s = requests.session()
s.Keep-alive = False

print('''
-----Desktop-----
Default
-----Mobile-----
header = {\'User-Agent\':ua_m}
-----Command-----
url = 

r = s.get(url, headers=header)

''')

import code
code.interact(banner = "", local = locals())
