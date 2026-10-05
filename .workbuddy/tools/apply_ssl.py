# -*- coding: utf-8 -*-
"""调用宝塔面板自身的 ACME 接口为站点申请 Let's Encrypt 证书（文件验证）。

第一步只申请并把返回结构打印出来，确认无误后再部署到站点。

在服务器上用面板解释器执行：
    /www/server/panel/pyenv/bin/python3 /root/apply_ssl.py
"""
import json
import sys

sys.path.insert(0, '/www/server/panel/class')
sys.path.insert(0, '/www/server/panel')

import public          # noqa: E402
import acme_v2         # noqa: E402

SITE_ID = '44'
DOMAIN = 'wxjs.czhweb.cn'


def arg_obj():
    if hasattr(public, 'dict_obj'):
        o = public.dict_obj()
    else:
        class _O(object):
            pass
        o = _O()
    o.id = SITE_ID
    o.domains = json.dumps([DOMAIN])
    o.auth_type = 'http'
    o.auth_to = '0'
    return o


def main():
    acme = acme_v2.acme_v2()
    res = acme.apply_cert_api(arg_obj())
    if isinstance(res, dict):
        print('返回字段:', sorted(res.keys()))
        print('status:', res.get('status'), '| msg:', res.get('msg'))
        for k in res:
            v = res[k]
            if isinstance(v, str) and len(v) > 120:
                print('  %-12s <str %d 字符> %s...' % (k, len(v), v[:60].replace('\n', ' ')))
            else:
                print('  %-12s %s' % (k, v))
        with open('/root/acme_result.json', 'w') as f:
            json.dump(res, f, ensure_ascii=False)
        print('完整结果已存 /root/acme_result.json')
    else:
        print('返回:', res)


if __name__ == '__main__':
    main()
