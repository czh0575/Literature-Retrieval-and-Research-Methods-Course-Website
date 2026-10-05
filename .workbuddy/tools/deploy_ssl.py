# -*- coding: utf-8 -*-
"""把申请到的证书部署到站点（写入证书文件 + 在 nginx 配置里开启 443）。

在服务器上执行：
    /www/server/panel/pyenv/bin/python3 /root/deploy_ssl.py
"""
import json
import sys

sys.path.insert(0, '/www/server/panel/class')
sys.path.insert(0, '/www/server/panel')

import public          # noqa: E402
import panelSite       # noqa: E402

DOMAIN = 'wxjs.czhweb.cn'

with open('/root/acme_result.json') as f:
    d = json.load(f)

cert_pem = d['cert'].strip() + '\n' + d['root'].strip() + '\n'
key_pem = d['private_key'].strip() + '\n'

o = public.dict_obj()
o.siteName = DOMAIN
o.first_domain = DOMAIN
o.key = key_pem
o.csr = cert_pem

res = panelSite.panelSite().SetSSL(o)
print('SetSSL 返回: %s' % res)
