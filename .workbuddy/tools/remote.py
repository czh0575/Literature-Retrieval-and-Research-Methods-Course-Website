# -*- coding: utf-8 -*-
"""通过 SSH 连到云服务器执行命令 / 上传文件（密码取自环境变量 SSH_PW）。

用法：
    set SSH_PW=xxx
    python remote.py run "ls -la /www/wwwroot"
    python remote.py runfile cmds.txt
    python remote.py put <本地文件> <远端路径>
    python remote.py putdir <本地目录> <远端目录>

说明：密码只从环境变量读取，不写入任何文件。
"""
import os
import posixpath
import sys
import time

import paramiko

HOST = os.environ.get('SSH_HOST', '111.231.0.202')
PORT = int(os.environ.get('SSH_PORT', '22'))
USER = os.environ.get('SSH_USER', 'root')
PW = os.environ.get('SSH_PW')


def connect():
    if not PW:
        raise SystemExit('缺少环境变量 SSH_PW')
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(HOST, port=PORT, username=USER, password=PW,
              timeout=25, banner_timeout=25, auth_timeout=25,
              look_for_keys=False, allow_agent=False)
    return c


def run(c, cmd):
    stdin, stdout, stderr = c.exec_command(cmd, timeout=300)
    out = stdout.read().decode('utf-8', 'replace')
    err = stderr.read().decode('utf-8', 'replace')
    code = stdout.channel.recv_exit_status()
    return code, out, err


def show(cmd, code, out, err):
    print('$ ' + cmd)
    if out.strip():
        print(out.rstrip())
    if err.strip():
        print('[stderr] ' + err.rstrip())
    print('[exit %s]' % code)
    print('-' * 70)


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    mode = sys.argv[1]
    c = connect()
    try:
        if mode == 'run':
            code, out, err = run(c, sys.argv[2])
            show(sys.argv[2], code, out, err)
        elif mode == 'runfile':
            with open(sys.argv[2], encoding='utf-8') as f:
                cmds = [ln.strip() for ln in f
                        if ln.strip() and not ln.strip().startswith('#')]
            for cmd in cmds:
                code, out, err = run(c, cmd)
                show(cmd, code, out, err)
        elif mode == 'put':
            local, remote = sys.argv[2], sys.argv[3]
            sftp = c.open_sftp()
            t0 = time.time()
            sftp.put(local, remote)
            sftp.close()
            print('上传 %s -> %s 完成 (%.1fs, %.1f KB)' % (
                local, remote, time.time() - t0,
                os.path.getsize(local) / 1024.0))
        elif mode == 'putdir':
            local, remote = sys.argv[2], sys.argv[3]
            sftp = c.open_sftp()
            n = 0
            total = 0
            t0 = time.time()
            # 先建目录
            for root, dirs, files in os.walk(local):
                rel = os.path.relpath(root, local).replace('\\', '/')
                rd = remote if rel == '.' else posixpath.join(remote, rel)
                try:
                    sftp.stat(rd)
                except IOError:
                    sftp.mkdir(rd)
                for f in files:
                    lp = os.path.join(root, f)
                    rp = posixpath.join(rd, f)
                    sftp.put(lp, rp)
                    n += 1
                    total += os.path.getsize(lp)
            sftp.close()
            print('上传 %d 个文件, %.1f MB, 用时 %.1fs' % (
                n, total / 1048576.0, time.time() - t0))
        else:
            raise SystemExit('未知模式: ' + mode)
    finally:
        c.close()


if __name__ == '__main__':
    main()
