# -*- coding: utf-8 -*-
"""去掉站点配置里重复的 #HTTP_TO_HTTPS 块（只保留第一处）。

宝塔的 HttpToHttps 用 str.replace 替换所有匹配点，若配置里存在两个
'#error_page 404/404.html;' 就会写入两遍。功能上无害，但配置不整洁。

在服务器上执行：
    /www/server/panel/pyenv/bin/python3 /root/fix_dup.py
"""
import re
import shutil
import subprocess

CONF = '/www/server/panel/vhost/nginx/wxjs.czhweb.cn.conf'
BAK = CONF + '.bak_dedup'

BLOCK = re.compile(
    r'[ \t]*#HTTP_TO_HTTPS_START\n.*?[ \t]*#HTTP_TO_HTTPS_END\n',
    re.S)

with open(CONF) as f:
    text = f.read()

found = BLOCK.findall(text)
print('找到 HTTP_TO_HTTPS 块: %d 个' % len(found))

if len(found) > 1:
    shutil.copy(CONF, BAK)
    first = [True]

    def keep_first(m):
        if first[0]:
            first[0] = False
            return m.group(0)
        return ''

    new = BLOCK.sub(keep_first, text)
    with open(CONF, 'w') as f:
        f.write(new)
    print('已删除多余块，备份:', BAK)
else:
    print('无需处理')

print('--- nginx -t ---')
print(subprocess.run(['nginx', '-t'], capture_output=True, text=True)
      .stderr.strip())
