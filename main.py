#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file: main.py
# author: JinTian
# time: 04/02/2018 11:59 AM
# Copyright 2018 JinTian. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
"""
main entrance of Alfred
"""
import os
import sys
import argparse
import colorama


def arg_parse():
    """
    parse arguments
    :return:
    """
    parser = argparse.ArgumentParser(prog="alfred")

    # vision, text, scrap
    sub_parser = parser.add_subparsers()
    vision_parser = sub_parser.add_parser('vision', help='vision related commands.')
    vision_parser.add_argument('extract', help='extract image from video')
    vision_parser.add_argument('2video', help='combine an image sequence into a video')
    vision_parser.add_argument('gray', help='covert a colorful image into gray image')
    vision_parser.add_argument('clean', help='clean all un-supported or broken image from a directory')
    vision_parser.add_argument('faces', help='extract all faces from a single image or from a images dir')

    text_parser = sub_parser.add_parser('text', help='text related commands.')
    text_parser.add_argument('clean', help='clean a text file, which will clean all un-use words for nlp')
    text_parser.add_argument('translate', help='translate a words to target language')

    scrap_parser = sub_parser.add_parser('scrap', help='scrap related commands.')
    scrap_parser.add_argument('image', help='scrap images with a query words and save into local')

    return parser.parse_args()


if __name__ == '__main__':
    args = arg_parse()
    print(args)