# -*- coding: utf-8 -*-
"""开启站点强制 HTTPS 跳转（宝塔面板自带方法 HttpToHttps）。

在服务器上执行：
    /www/server/panel/pyenv/bin/python3 /root/force_https.py
"""
import sys

sys.path.insert(0, '/www/server/panel/class')
sys.path.insert(0, '/www/server/panel')

import public          # noqa: E402
import panelSite       # noqa: E402

o = public.dict_obj()
o.siteName = 'wxjs.czhweb.cn'
print('HttpToHttps:', panelSite.panelSite().HttpToHttps(o))
