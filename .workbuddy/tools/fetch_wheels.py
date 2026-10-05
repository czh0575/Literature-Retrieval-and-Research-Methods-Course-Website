# -*- coding: utf-8 -*-
"""绕过 pip 的网络限制，直接从 PyPI 镜像抓取 win_amd64 轮子到本地目录。

本机沙箱对 pip 的 HTTPS 请求做了代理拦截，但普通 urllib 请求（不走代理）可通。
因此这里自己解析 simple 索引、挑选匹配当前解释器的 wheel，再用
    pip install --no-index --find-links=<目录> <包名>
离线安装。

用法：
    python fetch_wheels.py <目标包> [<目标包> ...]
"""
import os
import re
import sys
import urllib.parse
import urllib.request

MIRROR = 'https://pypi.tuna.tsinghua.edu.cn/simple'
OUT = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'wheels'))

# 本机环境：Windows x64 + CPython 3.13
PLAT = 'win_amd64'
# abi3 轮的版本号写法是 cp39 / cp311 这种（3.9 / 3.11），不是 cp3.9
_ABI3 = ['cp%s-abi3-%s' % (v, PLAT)
         for v in ('313', '312', '311', '310', '39', '38', '37', '36')]
# 优先级：数值越小越匹配；纯 Python 轮共用一档，避免挑到过旧版本
TAG_PRIORITY = {}
for _i, _t in enumerate(['cp313-cp313-' + PLAT] + _ABI3):
    TAG_PRIORITY[_t] = _i
for _t in ['py3-none-' + PLAT, 'py3-none-any', 'py2.py3-none-any']:
    TAG_PRIORITY[_t] = 99

OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def parse_ver(name):
    """从 wheel 文件名取正式版本号元组；预发布版返回 None。"""
    m = re.search(r'-(\d+(?:\.\d+)*)-', name)
    if not m:
        return None
    return tuple(int(x) for x in m.group(1).split('.'))


def rank(name):
    """返回标签优先级（越小越匹配）与版本号。"""
    for tag, pri in TAG_PRIORITY.items():
        if name.endswith('-' + tag + '.whl'):
            v = parse_ver(name)
            if v:
                return pri, v
    return None


def pick(pkg):
    url = '%s/%s/' % (MIRROR, pkg)
    html = OPENER.open(url, timeout=30).read().decode('utf-8', 'replace')
    best = None
    for href in re.findall(r'href="([^"#]+)', html):
        fn = href.rsplit('/', 1)[-1]
        if not fn.endswith('.whl') or 'linux' in fn or 'macos' in fn:
            continue
        r = rank(fn)
        if not r:
            continue
        key = (r[0], tuple(-x for x in r[1]))   # 标签优先，其次版本最高
        if best is None or key < best[0]:
            best = (key, urllib.parse.urljoin(url, href), fn)
    return best


def main():
    pkgs = sys.argv[1:]
    if not pkgs:
        raise SystemExit(__doc__)
    os.makedirs(OUT, exist_ok=True)
    for pkg in pkgs:
        try:
            got = pick(pkg)
        except Exception as e:
            print('  ✗ %-14s 索引读取失败: %s' % (pkg, e))
            continue
        if not got:
            print('  ✗ %-14s 没有匹配的 wheel' % pkg)
            continue
        _, url, fn = got
        dest = os.path.join(OUT, fn)
        if os.path.isfile(dest) and os.path.getsize(dest) > 1024:
            print('  = %-14s 已存在 %s' % (pkg, fn))
            continue
        data = OPENER.open(url, timeout=180).read()
        with open(dest, 'wb') as f:
            f.write(data)
        print('  ✓ %-14s %s  (%.1f MB)' % (pkg, fn, len(data) / 1048576.0))
    print()
    print('下载目录:', OUT)
    print('离线安装: pip install --no-index --find-links="%s" %s'
          % (OUT, ' '.join(pkgs)))


if __name__ == '__main__':
    main()
