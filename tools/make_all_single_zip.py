#!/usr/bin/env python
import os
import sys
import datetime

from make import *
from make_all import branches

def gitCheckout(branch):
    import subprocess
    cmd = "git checkout %s" % branch
    cmd = cmd.split(" ")
    p = subprocess.Popen(cmd)
    p.wait()

def main():
    filename = sys.argv[0]
    tools_folder = pparent(filename)
    root_folder = pparent(tools_folder)
    src_folder = pjoin(root_folder, 'src')
    themes_folder = pjoin(root_folder, 'Themes')
    makeNetbeansTheme(src_folder, themes_folder, ops=['clean'])
    for branch in branches:
        gitCheckout(branch)
        makeNetbeansTheme(src_folder, themes_folder, ops=['compile_src', 'compile_attr_files'], selected_theme="")
    theme_pack_name = 'Netbean Themes (%s)' % datetime.date.today().isoformat()
    makeNetbeansTheme(src_folder, themes_folder, theme_name=theme_pack_name, ops=['pack', 'clean'])

if __name__ == '__main__':
    main()