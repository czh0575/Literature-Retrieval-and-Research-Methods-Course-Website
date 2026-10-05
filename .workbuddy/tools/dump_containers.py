# -*- coding: utf-8 -*-
"""导出标题笼统的容器（注意 / 小贴士 / 提高效率的做法 / 易错点）及其内容。"""
import os
import re

D = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
SUBS = ['05-cnki-retrieval', '05-foreign-retrieval', '06-zotero']
GENERIC = re.compile(r'^:::\s*(tip|warning)\s*(注意|小贴士|提高效率的做法|易错点|提醒|小提示)\s*$')

n = 0
for sub in SUBS:
    d = os.path.join(D, sub)
    for f in sorted(os.listdir(d)):
        p = os.path.join(d, f)
        lines = open(p, encoding='utf-8').read().split('\n')
        i = 0
        while i < len(lines):
            m = GENERIC.match(lines[i])
            if m:
                n += 1
                j = i + 1
                body = []
                while j < len(lines) and not lines[j].startswith(':::'):
                    if lines[j].strip():
                        body.append(lines[j].strip())
                    j += 1
                print('[%02d] %s L%d  <%s %s>' % (n, f, i + 1, m.group(1), m.group(2)))
                for b in body:
                    print('      | ' + b[:150])
                i = j
            i += 1
print('总计 %d 处' % n)
