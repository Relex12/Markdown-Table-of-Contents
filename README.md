# Markdown-Table-of-Contents
Python tool to compile hyperlinked Table of Contents into Markdown (GFM) files

![](https://img.shields.io/badge/status-In_Progress-green) ![](https://img.shields.io/github/license/Relex12/Markdown-Table-of-Contents) ![](https://img.shields.io/github/repo-size/Relex12/Markdown-Table-of-Contents) ![](https://img.shields.io/github/languages/top/Relex12/Markdown-Table-of-Contents) ![](https://img.shields.io/github/last-commit/Relex12/Markdown-Table-of-Contents) ![](https://img.shields.io/github/stars/Relex12/Markdown-Table-of-Contents)



Check out on GitHub:

[![Markdown-Table-of-Contents](https://github-readme-stats.vercel.app/api/pin/?username=Relex12&repo=Markdown-Table-of-Contents)](https://github.com/Relex12/Markdown-Table-of-Contents)

[Read in French.](https://relex12.github.io/fr/Markdown-Table-of-Contents)

---

## Summary

* [Markdown-Table-of-Contents](#markdown-table-of-contents)
    * [Summary](#summary)
    * [What is it?](#what-is-it)
    * [How does it work?](#how-does-it-work)
    * [How to use it?](#how-to-use-it)
    * [CLI arguments](#cli-arguments)
    * [Specifications](#specifications)
    * [Missing features](#missing-features)
    * [License](#license)

<!-- table of contents created by Adrian Bonnet, see https://github.com/Relex12/Markdown-Table-of-Contents for more -->

## What is it?

**Haven't you ever been frustrated by not being able to create a dynamic table of contents in Markdown?**

That's what this tool is about. Running **only one command** , your can create an **hyperlinked table of contents** directly in your Markdown file.

## How does it work?

In your Markdown file, write a **table of contents tag** where you want to add the table of contents (TOC), then run Markdown-Table-of-Contents on your file. This will delete the line containing the TOC tag, and insert the generated hyperlinked TOC instead.

A **TOC tag** is a `toc` string, uppercase or lowercase, surrounded by a simple or a double pair of brackets. That means only `[TOC]`, `[[TOC]]`, `[toc]` and `[[toc]]` are valid TOC tags.

This behavior is already used by many Markdown editors (Typora, Markdown Monster) and tools (doctoc), but this one is the first Python small easy-to-use CLI tool adding this feature to Github-Flavored-Markdown.

## How to use it?

**It's a 2 step procedure:**

1. install Markdown-Table-of-Contents by cloning the repo : `git clone https://github.com/Relex12/Markdown-Table-of-Contents.git`
2. run the script on your Markdown file : `python3 toc.py FileName.md` (locations of `toc.py` and your file can be relative to the working directory or absolute)

## CLI arguments

Here is the result of  the `python toc.py -h` command:

```
usage: toc.py [-h] [-o OUTPUT] [--depth {1,2,3,4,5,6}] [--ignore-begin]
              FileName

positional arguments:
  FileName              input Markdown file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output file to write in, default overwrites FileName
  --depth {1,2,3,4,5,6}
                        maximum heading depth, default is 6
  --ignore-begin        ignore headings before the TOC tag
```

## Specifications

The TOC tag line **MUST** start with `[TOC]`, `[[TOC]]`, `[toc]` or `[[toc]]`, that means there **MUST NOT** be any white space between the previous end of line and the first bracket `[`.

The entire TOC tag line will be removed, that means every character between the final bracket `]` and the next end of line will be deleted along with the TOC tag.

The TOC tag **MUST** be one of these : `[TOC]`, `[[TOC]]`, `[toc]` or `[[toc]]`. Even if `[TOC]]` and `[toc]]` **MAY** work, they **SHOULD NOT** be used.

If there is more the one TOC tag line in the whole file, only the first one will be replaced by the generated TOC. Every other TOC tag will be ignored, that means it will still be in the output file. If you want to replace each TOC tag, you **SHOULD** run the script several times.

To be interpreted as a heading, a heading line **MUST** contain a white space (at least one white space character) between the sharp(s) and the heading label. However, you **SHOULD NOT** use more than one white space character, every character between the first white space and end of line excluded are used in the link title and the link value (excluding modifications).

The heading value is modified to be correctly interpreted by GitHub as a link-to-paragraph URL: space characters are replaced by dashes `-`, question marks `?` and exclamation marks `!` are removed and not replaced. You **SHOULD NOT** use white space characters different from space characters (such as tabulations) in a heading line. Some special characters such as sharps `#`, ampersands `&` and others **MAY** cause unexpected behaviors once uploaded on GitHub. White space characters (including space characters) right before end of line **MAY** also cause unexpected behaviors. If you find any of these behaviors, please open an issue.

The indentation for the different list levels uses four space characters for each greater indent, starting from 0 space for headings level 1, 4 spaces for headings level 2, up to 24 spaces for headings level 6. After those spaces, there is a single asterisk `*` followed by a single space character and a bracket `[`. Up to the next bracket `]` is the heading line (every character from the heading line between the first white space and end of line excluded). After the bracket, a parenthesis `(` and a sharp `#`, then the modified heading line up to the final parenthesis `)`. As the end of line is removed from heading line, another end of line is added after the final parenthesis.

End of line are expected to be one character long, considered as LF (`\n`). That means only one character is removed at the end of heading lines before it is used as link title and modified as link value. However, it **MAY** work if you use CRLF end of lines. In the same way, only one LF character is inserted at the end of link lines in the generated TOC.

## Missing features

Only "sharps shaped" heading are included in the generated TOC, excluding equals `=`  and dashes `-` underline style and HTML style tag such as `<h1>...</h1>`. The implementation should also consider sharps right before end of line as part of syntax and remove then. Many other specifications are supposed to be respected and are not. See Github-Flavored-Markdown specifications [here](https://github.github.com/gfm).

Also, the exhaustive list of unexpected behaviors due to special characters doesn't exist: if something strange happens, think about special characters in the first place.

## License

The project is a small one. The code is given to the GitHub Community  for free, only under the MIT License, that is not too restrictive.
