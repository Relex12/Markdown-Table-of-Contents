#!/usr/bin/env python3
import os
import argparse


# list of possible table of contents tags
toc_tag_list = ["[TOC]", "[[TOC]]", "[toc]", "[[toc]]"]

escape_char_list = ['?', '!', '$', '`', ':']

if __name__ == '__main__':

    # Arguments processing
    parser = argparse.ArgumentParser()
    parser.add_argument("FileName", help="input Markdown file")
    parser.add_argument("-o", "--output", help="output file to write in, default overwrites FileName")
    parser.add_argument("--depth", help="maximum heading depth, default is 6", type=int, choices=range(1, 7), default=6)
    parser.add_argument("--ignore-begin", help="ignore headings before the TOC tag", action="store_true", default=False)
    args = parser.parse_args()
    if not args.output:
        args.output = args.FileName


    input_file = open(args.FileName, 'r')

    # True when an element from toc_tag_list has been encountered
    toc_tag_encountered = False
    # generated table of contents as a string
    table_of_contents = ""
    # lines from the input file, respectively before and after the toc tag
    output_text = ["", ""]

    for line in input_file:
        # if the line could be a heading and it must be converted
        if line.startswith('#') and (not args.ignore_begin or toc_tag_encountered):
            for i in range (1, args.depth+1):
                if line.startswith(i*'#' + ' '):
                    # add as much white spaces as necessary, the line between
                    # brackets as link title, and the line between
                    # parenthesis after a # char, lowercased, without unwanted
                    # characters, as link value
                    raw_new_toc_line = (i-1)*4*' '+'* ['+line[(i+1):-1]+']'
                    sed_new_toc_line = '(#'+line[(i+1):-1].lower().replace(' ','-')+')\n'
                    for char in escape_char_list:
                        sed_new_toc_line = sed_new_toc_line.replace(char, '')
                    table_of_contents += raw_new_toc_line+sed_new_toc_line

        # if a table of content tag is encountered
        if any([line.startswith(x) for x in toc_tag_list]):
                toc_tag_encountered = True

        # else we add the line to the right (i.e. not wrong) part
        elif not toc_tag_encountered:
            output_text[0] += line
        else:
            output_text[1] += line


    input_file.close()

    # please keep the line below as a reference to the author's work
    author_renference = "\n<!-- table of contents created by Adrian Bonnet, see https://Relex12.github.io/Markdown-Table-of-Contents for more -->\n"

    if toc_tag_encountered:
        output_file = open(args.output, 'w')
        output_file.write(output_text[0]+table_of_contents+author_renference+output_text[1])
        output_file.close()
