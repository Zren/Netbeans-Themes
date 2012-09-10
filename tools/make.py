#!/usr/bin/env python
import os
import sys
import shutil
import zipfile
import ConfigParser

pjoin = os.path.join
pparent = lambda x: os.path.dirname(os.path.abspath(x))

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

nb_info_filename = '.nbattrs'
nb_info_content_wrapper = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE attributes PUBLIC "-//NetBeans//DTD DefaultAttributes 1.0//EN" "http://www.netbeans.org/dtds/attributes-1_0.dtd">
<attributes version="1.0">
%s
</attributes>"""

def nb_attr_contents(content):
    return nb_info_content_wrapper % content

###

def clean(bin_folder):
    if os.path.exists(bin_folder):
        shutil.rmtree(bin_folder)

def compile_if_found(src_folder, src_filename, bin_folder, relative_dir_path, dest_filename):
    src_path = pjoin(src_folder, src_filename)
    if os.path.exists(src_path):
        dir_path = pjoin(bin_folder, relative_dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        shutil.copy(src_path, pjoin(dir_path, dest_filename))

def compile_src(src_folder, theme_name, bin_folder):
    src_filename = 'base-FontColor.xml'
    relative_dir_path = pjoin('config', 'Editors', 'FontsColors', theme_name)
    dest_filename = 'org-netbeans-modules-editor-settings-CustomFontsColors-tokenColorings.xml'
    compile_if_found(src_folder, src_filename, bin_folder, relative_dir_path, dest_filename)
    #
    src_filename = 'base-Highlights.xml'
    relative_dir_path = pjoin('config', 'Editors', 'FontsColors', theme_name)
    dest_filename = 'org-netbeans-modules-editor-settings-CustomFontsColors-highlights.xml'
    compile_if_found(src_folder, src_filename, bin_folder, relative_dir_path, dest_filename)
    #
    src_filename = 'java-FontColor.xml'
    relative_dir_path = pjoin('config', 'Editors', 'text', 'x-java', 'FontsColors', theme_name)
    dest_filename = 'org-netbeans-modules-editor-settings-CustomFontsColors-tokenColorings.xml'
    compile_if_found(src_folder, src_filename, bin_folder, relative_dir_path, dest_filename)

def compile_attr_file(folder):
    content = ""
    #
    filename = 'org-netbeans-modules-editor-settings-CustomFontsColors-highlights.xml'
    if os.path.exists(pjoin(folder, filename)):
        content += """
    <fileobject name="org-netbeans-modules-editor-settings-CustomFontsColors-highlights.xml">
        <attr name="nbeditor-settings-ColoringType" stringvalue="highlight"/>
    </fileobject>
    """
    #
    filename = 'org-netbeans-modules-editor-settings-CustomFontsColors-tokenColorings.xml'
    if os.path.exists(pjoin(folder, filename)):
        content += """
    <fileobject name="org-netbeans-modules-editor-settings-CustomFontsColors-tokenColorings.xml">
        <attr name="nbeditor-settings-ColoringType" stringvalue="token"/>
    </fileobject>
    """
    #
    content = nb_attr_contents(content)
    f = open(pjoin(folder, nb_info_filename), 'w')
    f.write(content)
    f.close()


def compile_attr_files(theme_name, bin_folder):
    relative_dir_path = pjoin('config', 'Editors', 'FontsColors', theme_name)
    folder = pjoin(bin_folder, relative_dir_path)
    compile_attr_file(folder)
    #
    relative_dir_path = pjoin('config', 'Editors', 'text', 'x-java', 'FontsColors', theme_name)
    folder = pjoin(bin_folder, relative_dir_path)
    compile_attr_file(folder)


def pack(bin_folder, themes_folder, theme_name, selected_theme=None):
    # selected_theme=None (defaults to theme_name)
    # selected_theme="" (don't set a selected_theme)
    if not selected_theme:
        selected_theme = theme_name

    if selected_theme and len(selected_theme) > 0:
        attr_file_content ="""
    <fileobject name="Editors">
        <attr name="currentFontColorProfile" stringvalue="%s"/>
    </fileobject>
    """
        attr_file_content = attr_file_content % selected_theme
        content = nb_attr_contents(attr_file_content)
        filename = pjoin(bin_folder, nb_info_filename)
        f = open(filename, 'w')
        f.write(content)
        f.close()

    create_zip(bin_folder, '', pjoin(themes_folder, theme_name  + '.zip'))

def makeNetbeansTheme(src_folder, themes_folder, theme_name=None, ops=['clean', 'compile_src', 'compile_attr_files', 'pack', 'clean'], selected_theme=None):
    Config = ConfigParser.ConfigParser()
    Config.read(pjoin(src_folder, 'theme.ini'))

    if not theme_name:
        theme_name = Config.get('Theme', 'name')

    bin_folder = pjoin(src_folder, 'target')

    op_funcs = {
        'clean': lambda: clean(bin_folder),
        'compile_src': lambda: compile_src(src_folder, theme_name, bin_folder),
        'compile_attr_files': lambda: compile_attr_files(theme_name, bin_folder),
        'pack': lambda: pack(bin_folder, themes_folder, theme_name, selected_theme=selected_theme)
    }

    for op in ops:
        op_funcs[op]()

def main():
    filename = sys.argv[0]
    tools_folder = pparent(filename)
    root_folder = pparent(tools_folder)
    src_folder = pjoin(root_folder, 'src')
    themes_folder = pjoin(root_folder, 'Themes')
    makeNetbeansTheme(src_folder, themes_folder)

if __name__ == '__main__':
    main()