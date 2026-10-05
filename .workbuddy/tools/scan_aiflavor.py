# -*- coding: utf-8 -*-
"""扫描讲义中的 AI 味标记，输出每页命中统计与具体位置。"""
import os
import re
import sys

DOCS = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
SKIP = {'01-course-introduction'}

# (标记名, 正则, 说明)
PATTERNS = [
    ('不是而是', r'不是[^，。；\n]{2,20}，?而是', '最高优先级'),
    ('不是而是', r'不仅[^，。；\n]{2,20}，(?:更|也)是', '否定排比变体'),
    ('不是而是', r'并非[^，。；\n]{2,20}，而是', '变体'),
    ('假靶子', r'你以为[^，。；\n]{2,25}[，,]?\s*实际上', '把读者当傻子'),
    ('假靶子', r'很多人以为[^，。；\n]{2,25}[，,]?\s*(?:其实|实际上)', '假靶子'),
    ('自问自答', r'[？?]\s*\n\s*\n?\s*\S{2,12}[。，]', '老师腔，需人工核对'),
    ('元评论', r'(?:本节|本章|本页|本文|这部分|下面|接下来|接下来我们将|我们将)(?:将|会|要)?(?:介绍|讲|说明|讨论|给出|展开|围绕)', '提前宣布要讲什么'),
    ('元评论', r'需要(?:先)?(?:明确|说明|强调)的是', '元评论'),
    ('过渡连接词', r'(?<![，。、])此外[，,]', 'AI 连接词'),
    ('过渡连接词', r'(?<![，。、])然而[，,]', 'AI 连接词'),
    ('过渡连接词', r'(?<![，。、])因此[，,]', 'AI 连接词'),
    ('过渡连接词', r'值得注意的是', '套话'),
    ('过渡连接词', r'不难(?:发现|看出)', '套话'),
    ('过渡连接词', r'综上所述|总而言之|总的来说|一言以蔽之', '套话'),
    ('过渡连接词', r'由此可见|换言之|换句话说|也就是说', '书面腔'),
    ('过渡连接词', r'首先[^。\n]{2,30}[，,].{0,60}其次', '三段式'),
    ('过渡连接词', r'一方面.{0,60}另一方面', '对仗'),
    ('过渡连接词', r'不可否认|毋庸置疑|毫无疑问|众所周知|显而易见', '套话'),
    ('过渡连接词', r'在(?:当今|如今|当下)[^。\n]{0,12}(?:时代|背景|社会)', '教科书开头'),
    ('过渡连接词', r'随着[^。\n]{2,20}的(?:不断|持续|日益|快速)(?:发展|推进|深入)', '空话'),
    ('过渡连接词', r'在[^。\n]{2,20}的大背景下', '空话'),
    ('过渡连接词', r'基于以上分析|经过以上分析', '套话'),
    ('判词', r'本质上|归根结底|说到底', '太学术/口头禅'),
    ('判词', r'说白了', 'AI 高频'),
    ('判词', r'这意味着', 'AI 标志'),
    ('判词', r'意味着什么', 'AI 标志'),
    ('判词', r'从某种意义上说|在某种程度上', '模糊限定'),
    ('判词', r'至关重要|不可或缺|举足轻重|意义重大|影响深远|不言而喻', '空泛大词'),
    ('判词', r'为[^。\n]{2,20}提供了有力(?:支撑|保障)|奠定[了]?坚实基础', '夸大'),
    ('升华结尾', r'这一刻|这就是[^。\n]{0,15}的意义|终于(?:明白|意识到)|(?:才)?(?:真正)(?:理解|懂得)了', '升华句'),
    ('排比堆叠', r'(?:又|既|并)?(?:能|可以|能够)[^。\n]{2,12}[、，][^。\n]{2,12}[、，][^。\n]{2,12}[、，]', '三项以上堆叠需核对'),
    ('破折号', r'——', '标点禁令'),
    ('半角括号中英混排', r'[\u4e00-\u9fff]\([A-Za-z]', '需核对括号规范'),
    ('完美三段', r'第一步.{0,80}第二步.{0,80}第三步', '模板化流程'),
    ('空泛要旨', r'为(?:后续|今后|下一步)[^。\n]{0,10}打下(?:了)?(?:良好|坚实)的?基础', '套话'),
    ('万能状语', r'，带着[^，。\n]{2,15}', 'AI 状语'),
    ('形容词堆砌', r'(?:高效|便捷|直观|清晰|完整|系统|全面|深入|重要|关键|核心)(?:、|和|与)(?:高效|便捷|直观|清晰|完整|系统|全面|深入|重要|关键|核心)', '连续形容词'),
]


def strip_code(text):
    """把代码块与行内代码替换成等长占位，避免误报。"""
    def blank(m):
        return '\n' * m.group(0).count('\n') + ' ' * (len(m.group(0)) - m.group(0).count('\n'))
    text = re.sub(r'```[\s\S]*?```', blank, text)
    text = re.sub(r'`[^`\n]*`', lambda m: ' ' * len(m.group(0)), text)
    return text


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    grand = {}
    detail = []
    for sub in sorted(os.listdir(DOCS)):
        if sub in SKIP:
            continue
        if only and sub != only:
            continue
        d = os.path.join(DOCS, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if not f.endswith('.md'):
                continue
            p = os.path.join(d, f)
            raw = open(p, encoding='utf-8').read()
            text = strip_code(raw)
            lines = text.split('\n')
            hits = {}
            for name, pat, _note in PATTERNS:
                for i, line in enumerate(lines, 1):
                    # 跳过纯标题行与表格分隔行
                    s = line.strip()
                    if s.startswith('#') or set(s) <= set('-|: '):
                        continue
                    for m in re.finditer(pat, line):
                        hits.setdefault(name, []).append((i, m.group(0)))
            n = sum(len(v) for v in hits.values())
            grand.setdefault(sub, []).append((f, len(lines), n))
            if n:
                detail.append((sub, f, len(lines), n, hits))
    print('=== 每页命中数（按密度排序）===')
    rows = []
    for sub, items in grand.items():
        for f, ln, n in items:
            rows.append((n / max(ln, 1) * 100, n, ln, sub, f))
    rows.sort(reverse=True)
    for dens, n, ln, sub, f in rows:
        print('%6.2f/百行  %3d 处  %4d 行  %s/%s' % (dens, n, ln, sub, f))
    print()
    print('=== 各标记总命中 ===')
    tot = {}
    for _, _, _, _, hits in detail:
        for k, v in hits.items():
            tot[k] = tot.get(k, 0) + len(v)
    for k, v in sorted(tot.items(), key=lambda x: -x[1]):
        print('%5d  %s' % (v, k))
    print()
    print('=== 具体命中位置（前 12 页）===')
    detail.sort(key=lambda x: -x[3])
    for sub, f, ln, n, hits in detail[:12]:
        print('--- %s/%s' % (sub, f))
        for k, v in sorted(hits.items(), key=lambda x: -len(x[1])):
            for i, g in v[:6]:
                print('    L%-4d [%s] %s' % (i, k, g[:70]))


if __name__ == '__main__':
    main()
