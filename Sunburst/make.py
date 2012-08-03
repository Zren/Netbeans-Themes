#!/usr/bin/env python
import os
import sys
import shutil
import zipfile

pjoin = os.path.join

###
# http://stackoverflow.com/a/296565
def zipfolder(path, relname, archive):
    paths = os.listdir(path)
    for p in paths:
        p1 = os.path.join(path, p)
        p2 = os.path.join(relname, p)
        if os.path.isdir(p1):
            zipfolder(p1, p2, archive)
        else:
            archive.write(p1, p2)

def create_zip(path, relname, archname):
    archive = zipfile.ZipFile(archname, "w", zipfile.ZIP_DEFLATED)
    if os.path.isdir(path):
        zipfolder(path, relname, archive)
    else:
        archive.write(path, relname)
    archive.close()
###

def makeNetbeansTheme(folder, theme_name):
    base_folder = pjoin(folder, 'config')
    def clean():
        if os.path.exists(pjoin(folder, 'config')):
            shutil.rmtree(pjoin(folder, 'config'))
    def compile():
        def compile_if_found(src_filename, relative_dir_path, dest_filename):
            src_path = pjoin(folder, src_filename)
            if os.path.exists(src_path):
                dir_path = pjoin(folder, relative_dir_path)
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                shutil.copy(src_path, pjoin(dir_path, dest_filename))
        #
        src_filename = 'base-FontColor.xml'
        relative_dir_path = pjoin('config', 'Editors', 'FontsColors', theme_name)
        dest_filename = 'org-netbeans-modules-editor-settings-CustomFontsColors-tokenColorings.xml'
        compile_if_found(src_filename, relative_dir_path, dest_filename)
        #
        src_filename = 'base-Highlights.xml'
        relative_dir_path = pjoin('config', 'Editors', 'FontsColors', theme_name)
        dest_filename = 'org-netbeans-modules-editor-settings-CustomFontsColors-highlights.xml'
        compile_if_found(src_filename, relative_dir_path, dest_filename)
        #
        src_filename = 'java-FontColor.xml'
        relative_dir_path = pjoin('config', 'Editors', 'text', 'x-java', 'FontsColors', theme_name)
        dest_filename = 'org-netbeans-modules-editor-settings-CustomFontsColors-tokenColorings.xml'
        compile_if_found(src_filename, relative_dir_path, dest_filename)
    def pack():
        create_zip(base_folder, 'config', theme_name  + '.zip')

    clean()
    compile()
    pack()




def main():
    filename = sys.argv[0]
    filename = os.path.abspath(filename)
    folder = os.path.dirname(filename)
    theme_name = os.path.basename(folder)
    makeNetbeansTheme(folder, theme_name)

if __name__ == '__main__':
    main()