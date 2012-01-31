#!/usr/bin/env python
# -*- coding: utf-8 -*-

__VERSION__ = '1.0.1'
__author__ = 'rx.wen218@gmail.com'

import sys
import os
from bcscope_utils import androidmk_parser
from optparse import OptionParser

modules = {}
def add_module_to_source(mod_name):
# do nothing if the module is already in modules collection
    if mod_name in modules:
        pass
    else:
        mod = all_modules.find_module(mod_name)
        if mod:
            modules[mod_name] = mod
            for dep in mod.depends:
                add_module_to_source(dep)

def transfer_to_dot_valid(name):
    return name.replace("-", "_").replace(".", "_").replace("+", "")

def generate_dependency_graph(dot_file_path):
    dot_file = open(dot_file_path, "w")
    dot_file.write("digraph {\n")
    for (mod_name, mod) in modules.items():
            dot_file.write("%s[label=\"%s\l%s\"]\n"%(transfer_to_dot_valid(mod.name), mod.name, mod.directory))
    for (mod_name, mod) in modules.items():
        for dep in mod.depends:
            dot_file.write("%s->%s\n"%(transfer_to_dot_valid(mod.name), transfer_to_dot_valid(dep)))
    dot_file.write("}\n")
    dot_file.close()

def parse_directory(dir_to_parse):
    mk_files = androidmk_parser.find_android_mk(dir_to_parse)
    all_modules = None
    for mk_file in mk_files:
        all_modules = androidmk_parser.parse_makefile(mk_file, all_modules)
    return all_modules

if __name__ == "__main__":
# parse command line options
    opt_parser = OptionParser(version = "%prog " + __VERSION__, 
                description = "command line tool for generating android dependency diagram",
                usage = "%prog [OPTION] [dir_to_parse]")
    opt_parser.add_option("-o", "--output", dest="output_file", 
            help="dot diagram file")
    opt_parser.add_option("-m", "--module", dest="module",
            help="only generate dependency diagram for specified module")
    opt_parser.add_option("-l", "--listmodule", action="store_true", default=False, 
            help="only list modules defined in specified directory [default: %default]")
    (cmdline_options, args) = opt_parser.parse_args()

    dir_to_parse = os.path.curdir
    if len(args) > 0:
        dir_to_parse = args[0]

    if not cmdline_options.listmodule:
        if not cmdline_options.output_file:
            print "must specify -o/--output option"
            sys.exit(-1)
        else:
            android_root = androidmk_parser.find_root()
            if android_root:
                dir_to_parse = android_root
            all_modules = parse_directory(dir_to_parse)
            if not cmdline_options.module:
                modules = all_modules.pool
            else:
                add_module_to_source(cmdline_options.module)
            generate_dependency_graph(cmdline_options.output_file)
    else:
        all_modules = parse_directory(dir_to_parse)
        for mod_name in all_modules.pool:
            print mod_name


