#!/usr/bin/python3
# -*- coding: UTF-8 -*- 
# filename: g.py

from ghost import Ghost, Session
from bs4 import BeautifulSoup

ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
ua_m = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0 Mobile/15B150 Safari/604.1'
header = {'User-Agent':ua_mo}

gh = Ghost()

se = Session(gh, user_agent=ua_mo, wait_timeout=20, wait_callback=None, display=True, viewport_size=(375, 553), download_images=True)



def help():
    print('''
    -----Desktop-----
    header = {\'User-Agent\':ua}
    -----Mobile-----
    Default
    header = {\'User-Agent\':ua_m}
    -----Size-----
    se = Session(gh, user_agent=ua, wait_timeout=20, wait_callback=None, display=True, viewport_size=(800, 680), download_images=True)
    -----Command-----
    url = 
    se.open(url)
    -----BeautifulSoup-----
    html = se.content
    soup = BeautifulSoup(html, "html.parser")
    ''')

help()

import code
code.interact(banner = "", local = locals())
