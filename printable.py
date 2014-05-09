# printable.py --- 
# 
# Filename: printable.py
# Description: Extension for Seth Brown's Custom Notebook
# Author: y_pe
# Created: Wed Mar 12 18:42:35 2014 (+0000)
# Version: 0.0.1
# Package-Requires: (notebook.py, XeLaTeX)
# Last-Updated: Sun Mar 16 22:23:25 2014 (+0000)
#           By: anton
#     Update #: 55
# URL: http://isoty.pe
# Original URL: github:drbunsen/custom-notebooks
# Keywords: Python, Notebook
#
# Commentary: 
# Extension for Seth Brown's Custom Notebook to
# allow for the easy printing of booklets from
# created notebooks.
# 
# Change Log:
# - Added printable.py to custom-notebooks generator
#
#
# License:
# Copyright (c) 2014 [y_pe]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# Code:

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys

def support_files(notebook):
    mkd_file = os.path.join(notebook)
    if not os.path.isfile(mkd_file):
        with open(mkd_file, mode='w') as outfile:
            fill = ref_file(notebook)
            outfile.write(fill)

def printable(notebook):
    notebook_file = os.path.join(notebook)
    booklet = (r'\documentclass{scrartcl}',
               r'\usepackage{pdfpages}',
               r'\begin{document}',
               r'\includepdf[pages=-,booklet=true, turn=false, landscape]{' + notebook_file + '}',
               r'\end{document}')
    return '\n'.join(line for line in booklet)

def main(notebook):
    [support_files(notebook)]

    with open('printable.tex', mode='w') as outfile:
        p = printable(notebook)
        outfile.write(p)

if __name__ == '__main__':
        (notebook) = sys.argv[1]
        main(notebook)
# 
# printable.py ends here
