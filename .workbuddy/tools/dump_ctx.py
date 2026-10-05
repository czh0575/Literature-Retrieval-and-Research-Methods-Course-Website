# -*- coding: utf-8 -*-
"""按标记类别输出命中行的上下文，便于逐处判断与修改。"""
import os
import re
import sys

DOCS = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'

TARGETS = {
    'dash': r'——',
    'bushi': r'不是[^，。；\n]{2,20}，?而是|并非[^，。；\n]{2,20}，而是|不仅[^，。；\n]{2,20}，(?:更|也)是',
    'meta': r'(?:本节|本章|本页|本文|下面|接下来)[^。\n]{0,6}(?:将|会|要)?(?:介绍|讲|说明|讨论|给出|展开|围绕)|需要(?:先)?(?:明确|说明|强调)的是',
    'word': r'本质上|意味着什么|这意味着|至关重要|不可或缺|影响深远|意义重大|不言而喻|说白了|归根结底',
    'conn': r'(?<![，。、])此外[，,]|(?<![，。、])然而[，,]|(?<![，。、])因此[，,]|值得注意的是|不难(?:发现|看出)|综上所述|总而言之|总的来说|由此可见|换言之|换句话说|也就是说|首先[^。\n]{2,30}[，,].{0,60}其次|不可否认|毋庸置疑|毫无疑问|众所周知|显而易见|在(?:当今|如今|当下)|随着[^。\n]{2,20}的(?:不断|持续|日益|快速)(?:发展|推进|深入)|基于以上分析',
}


def strip_code_lines(lines):
    """返回掩码数组：True 表示该行属于代码块或行内代码外可检查的正文。"""
    mask = []
    inblock = False
    for ln in lines:
        s = ln.strip()
        if s.startswith('```'):
            inblock = not inblock
            mask.append(False)
            continue
        mask.append(not inblock)
    return mask


def main():
    key = sys.argv[1]
    pat = TARGETS[key]
    skip = sys.argv[2] if len(sys.argv) > 2 else None
    for sub in sorted(os.listdir(DOCS)):
        if sub == '01-course-introduction':
            continue
        if skip and sub != skip:
            continue
        d = os.path.join(DOCS, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'):
                continue
            p = os.path.join(d, f)
            lines = open(p, encoding='utf-8').read().split('\n')
            mask = strip_code_lines(lines)
            printed = False
            for i, line in enumerate(lines):
                if not mask[i]:
                    continue
                # 去掉行内代码再匹配
                plain = re.sub(r'`[^`\n]*`', '', line)
                if re.search(pat, plain):
                    if not printed:
                        print('\n########## %s/%s' % (sub, f))
                        printed = True
                    for j in range(max(0, i - 1), min(len(lines), i + 2)):
                        print('  %s%4d| %s' % ('>>' if j == i else '  ', j + 1, lines[j][:150]))


if __name__ == '__main__':
    main()
