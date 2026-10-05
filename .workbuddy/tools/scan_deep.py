# -*- coding: utf-8 -*-
"""深层 AI 味扫描：找扫描器漏掉的元评论、预告口吻、模板块、隐喻、说教腔。"""
import os
import re
import sys

DOCS = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
SKIP = {'01-course-introduction'}

PATTERNS = [
    ('元评论-下面', r'下面(?:以|用|按|逐|分别|把|通过|先|再|给出|列出|介绍|说明|从)[^，。\n]{0,14}'),
    ('元评论-自我指涉', r'(?:本页|本节|本章|本文|这部分|全书|全章)(?:将|会|要|先|再|讲|介绍|说明|讨论|给出|围绕|的)'),
    ('预告', r'下一页|下一节|下一章|接下来(?:我们|将|会)|即将(?:进入|学习)'),
    ('模板块', r'要点回顾|下一步预告|本页小结|本部分小结|本节小结|本章小结|至此(?:结束|完成)|学完本页'),
    ('衔接语', r'与(?:下|本)(?:一)?(?:页|节|章)(?:的)?衔接|进入\s*[0-9]\.[0-9]\s*前'),
    ('说教腔', r'请(?:带着|记住|务必|注意|大家)|建议你|希望(?:你|大家)|你应该|你需要(?:记住|注意)'),
    ('我们', r'我们(?:将|会|要|可以|需要|来看|先|再|已经|也)'),
    ('隐喻', r'[^，。\n]{0,8}(?:的大门|的钥匙|的窗口|的基石|的抓手|的利器|的桥梁|的温床|的第二本能)'),
    ('隐喻', r'各就各位|请进门|工位|口诀|一句话(?:说|概括)|打个比方|好比|就像是'),
    ('升华', r'(?:才|终于)(?:真正)?(?:理解|明白|意识到)|这就是[^，。\n]{0,12}的意义|这一刻'),
    ('空泛', r'长远的?意义|深远的影响|无限的?可能|大有(?:\u4f5c\u4e3a|可为)'),
    ('模糊限定', r'从某种意义上|在某种程度上|可以说|在很大程度上'),
    ('排比三连', r'(?:\u3001[^，。；\n]{2,10}){2}[，。]'),
    ('冗余引导', r'(?:如下|以下)(?:表|所示|步骤|清单)'),
    ('评价腔', r'非常(?:重要|关键|有用|实用)|极其(?:重要|关键)|十分(?:重要|关键)'),
]


def strip_code(text):
    def blank(m):
        return '\n' * m.group(0).count('\n') + ' ' * (len(m.group(0)) - m.group(0).count('\n'))
    text = re.sub(r'```[\s\S]*?```', blank, text)
    text = re.sub(r'`[^`\n]*`', lambda m: ' ' * len(m.group(0)), text)
    return text


def main():
    for sub in sorted(os.listdir(DOCS)):
        if sub in SKIP:
            continue
        d = os.path.join(DOCS, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'):
                continue
            p = os.path.join(d, f)
            raw = open(p, encoding='utf-8').read()
            lines = strip_code(raw).split('\n')
            out = []
            for name, pat in PATTERNS:
                for i, line in enumerate(lines, 1):
                    s = line.strip()
                    if s.startswith('#') or (s and set(s) <= set('-|: ')):
                        continue
                    for m in re.finditer(pat, line):
                        out.append((i, name, m.group(0)))
            if out:
                print('--- %s/%s  (%d 处)' % (sub, f, len(out)))
                for i, name, g in out:
                    print('    L%-4d [%s] %s' % (i, name, g[:60]))


if __name__ == '__main__':
    main()
