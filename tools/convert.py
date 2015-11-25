#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright © 2014 fishcried(tianqing.w@gmail.com)
#

"""

"""

import json
import os
import argparse

def json2file(context, outfile):

    dname = os.path.dirname(outfile)
    if not os.path.exists(dname):
        os.mkdir(dname)

    context_string = json.dumps(context, sort_keys=True, indent=4)
    with open(outfile, 'w') as fp:
        fp.write(context_string)

def join_file(dname, fname):
    context_list = []
    for parent, dirname, fnames in os.walk(dname):
        for f in fnames:
            to_load_file = os.path.join(parent,f)
            context_list.append(json.load(file(to_load_file)))

    json2file(context_list, os.path.abspath(fname))

def split_file(fname, dname):
    for entry in json.load(file(fname)):
        split_name = os.path.join(dname, entry['_source']['title'] + '.json')
        json2file(entry,split_name)


def main():

    parser = argparse.ArgumentParser(
            description = "Split or join the json files")

    parser.add_argument("-d", "--dir", required=True,
            help="specify the directory where json files outputed")
    parser.add_argument("-f", "--file", required=True,
            help="specify file to split/join")
    parser.add_argument("--func", default="split", 
            choices=['split','join'],help="split/join")
    args = parser.parse_args()

    if args.func == "split":
        split_file(args.file, args.dir)
    else:
        join_file(args.dir, args.file)

if __name__ == '__main__':
    main()
