# -*- coding: utf-8 -*-
"""用无头 Chrome 截取站点页面，用于人工核对渲染效果。"""
import os
import subprocess
import sys

WEB = r'F:\02教学\教学课程\文献检索与研究方法\课件\web'
OUT = os.path.join(WEB, '.workbuddy', 'shots')
CHROME = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
PROFILE = os.path.join(WEB, '.workbuddy', 'chrome-profile')

PAGES = [
    ('live', 'https://wxjs.czhweb.cn/', '1440,960'),
    ('live-chapter', 'https://wxjs.czhweb.cn/course/06-zotero/interface.html', '1440,1000'),
    ('home', 'http://localhost:4321/', '1440,960'),
    ('home-full', 'http://localhost:4321/', '1440,1600'),
    ('footer', 'http://localhost:4321/', '1440,2600'),
    ('outline', 'http://localhost:4321/course-outline', '1440,1000'),
    ('chapter', 'http://localhost:4321/course/06-zotero/capture-and-download', '1440,1000'),
    ('logo', 'http://localhost:4321/logo.svg', '512,512'),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    only = sys.argv[1:] or None
    for name, url, size in PAGES:
        if only and name not in only:
            continue
        png = os.path.join(OUT, name + '.png')
        if os.path.isfile(png):
            os.remove(png)
        cmd = [CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars',
               '--no-first-run', '--no-default-browser-check',
               '--force-device-scale-factor=1',
               '--user-data-dir=' + PROFILE,
               '--window-size=' + size,
               '--virtual-time-budget=6000',
               '--screenshot=' + png, url]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        ok = os.path.isfile(png)
        size_kb = round(os.path.getsize(png) / 1024.0, 1) if ok else 0
        print('%-11s %-58s -> %s  %s KB' % (
            name, url, 'OK' if ok else 'FAIL', size_kb))
        if not ok:
            print('    rc=%s  %s' % (r.returncode, (r.stderr or '')[-260:]))


if __name__ == '__main__':
    main()
