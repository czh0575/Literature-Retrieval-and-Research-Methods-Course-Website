# -*- coding: utf-8 -*-
"""调用宝塔面板自身的 AddSite 接口建站，保证站点在面板里可见可管。

在服务器上用面板自带的解释器执行：
    /www/server/panel/pyenv/bin/python3 /root/add_site.py
"""
import json
import sys

sys.path.insert(0, '/www/server/panel/class')
sys.path.insert(0, '/www/server/panel')

import public          # noqa: E402
import panelSite       # noqa: E402

DOMAIN = 'wxjs.czhweb.cn'
PATH = '/www/wwwroot/' + DOMAIN
PS = '文献检索与研究方法课程网站'


def make_obj():
    """面板内部的参数对象，支持属性访问。"""
    if hasattr(public, 'dict_obj'):
        obj = public.dict_obj()
    else:
        class _Obj(object):
            pass
        obj = _Obj()
    obj.webname = json.dumps({
        'domain': DOMAIN,
        'domainlist': [],
        'count': 0,
    })
    obj.path = PATH
    obj.port = '80'
    obj.type_id = '0'
    obj.version = '00'          # 00 = 纯静态，不挂 PHP
    obj.ps = PS
    obj.ftp = 'false'
    obj.sql = 'false'
    obj.codeing = 'utf8'
    return obj


if __name__ == '__main__':
    site = panelSite.panelSite()
    result = site.AddSite(make_obj())
    print('AddSite 返回: %s' % result)
