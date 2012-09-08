#!/usr/bin/env python
import os
import sys
import shutil
import zipfile
import ConfigParser

from make import *

branches = [
    'master'
]

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
    for branch in branches:
        gitCheckout(branch)
        src_folder = pjoin(root_folder, 'src')
        themes_folder = pjoin(root_folder, 'Themes')
        makeNetbeansTheme(src_folder, themes_folder)

if __name__ == '__main__':
    main()