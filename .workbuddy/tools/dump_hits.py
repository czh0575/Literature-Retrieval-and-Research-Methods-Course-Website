# -*- coding: utf-8 -*-
"""按 scan_deep 的命中位置，输出每处的上下文（前后各 2 行），便于逐处改写。"""
import os
import re

DOCS = r'F:\02教学\教学课程\文献检索与研究方法\课件\web\docs\course'
SKIP = {'01-course-introduction'}

HITS = {
    '04-opening-report/methods-and-roadmap.md': [15],
    '05-cnki-retrieval/cnki-interface.md': [10, 111, 245, 272],
    '05-cnki-retrieval/core-journals.md': [184, 212],
    '05-cnki-retrieval/keyword-system.md': [24, 179, 223, 255, 257],
    '05-cnki-retrieval/research-trace.md': [219],
    '05-cnki-retrieval/retrieval-log.md': [30],
    '05-cnki-retrieval/screening-and-export.md': [10, 59, 148],
    '05-cnki-retrieval/search-strategy.md': [186, 268],
    '05-foreign-retrieval/preparation.md': [217],
    '05-foreign-retrieval/sci-ssci-and-jcr.md': [39],
    '05-foreign-retrieval/sciencedirect-refine.md': [93, 206, 211],
    '05-foreign-retrieval/sciencedirect-search.md': [8, 48, 218, 252],
    '05-foreign-retrieval/trace-and-cheatsheet.md': [26, 106],
    '05-foreign-retrieval/wos-retrieval.md': [67],
    '06-zotero/backup-and-workflow.md': [85, 298, 312],
    '06-zotero/capture-and-download.md': [8, 216, 233, 322],
    '06-zotero/install-and-connector.md': [421],
    '06-zotero/interface.md': [8, 169, 354, 358],
    '06-zotero/library-organization.md': [246],
    '06-zotero/metadata-and-reading.md': [239, 259, 263],
    '06-zotero/what-is-zotero.md': [42, 85, 92, 294, 309, 334, 392],
    '07-literature-review/writing-practice.md': [37],
}


def main():
    for key, nums in HITS.items():
        sub, f = key.split('/')
        p = os.path.join(DOCS, sub, f)
        lines = open(p, encoding='utf-8').read().split('\n')
        print('=' * 78)
        print('### %s   （共 %d 行）' % (key, len(lines)))
        for n in nums:
            lo = max(1, n - 3)
            hi = min(len(lines), n + 3)
            print('--- 附近 L%d' % n)
            for i in range(lo, hi + 1):
                mark = '>>' if i == n else '  '
                print('%s L%-4d %s' % (mark, i, lines[i - 1]))
            print()


if __name__ == '__main__':
    main()
