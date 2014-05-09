# -*- mode: Python; tab-width: 2; indent-tabs-mode:nil; -*-          #
######################################################################
# Author: Anton Strilchuk <anton@isoty.pe>                           #
# URL: http://isoty.pe                                               #
# Created: 09-05-2014                                                #
# Last-Updated: 09-05-2014                                           #
#   By: Anton Strilchuk <anton@isoty.pe>                             #
#                                                                    #
# Filename: jorgen                                                   #
# Version: 0.0.1                                                     #
# Original By: github:drbunsen/custom-notebooks                      #
#                                                                    #
# Description:                                                       #
# This is a modified version of a custom notebook generator          #
# originally made by Seth Brown. The generator is design to          #
# aid in the creation of a physical notebook, and with associated    #
# markup document that can be quickly opened using an embedded       #
# qrcode on each page of the printed journal.                        #
#                                                                    #
# Two files are include, the journal generator itself, jorgen        #
# and the associated print formatter.                                #
#                                                                    #
# QR Codes created by the generator are set to open in               #
# Textastic on the iPhone. To change this, edit the                  #
# x-callback-url found in the section titled APP LINK                #
#                                                                    #
######################################################################
######################################################################

import os
import sys
import qrcode
import datetime
from random import randint

# Generate associated markup files for the notebook.
#
# Things you may want to edit:
# (working on menu for this)
#
# The section titled fill defines the YAML frontmatter
# for the connected markup files. If you are using markdown
# you may want to switch some of the options in the fill.
# Also, change the following option to make the generator
# compile to markdown files instead of org-mode.
notebook_markup_format = 'org'

def ref_file(page_stamp, img_dir):

    date = datetime.datetime.today().strftime('%Y-%m-%d-').rstrip('-')
    img = ''.join((page_stamp, '.png'))
    img_fn = os.path.join(img_dir, img)
    fill = ('---', 'title: "{0}"'.format(page_stamp),
            'created_at: {0}'.format(date),
            'status: incomplete',
            'format: org',
            'isonum: {0}'.format(randint(1,606)), # random image per post hack
            'layout: post',
            'topic: ',
            'kind: article',
            'comments: true',
            'tags: []',
            '---', '\n\n',
    '<a href="{0}"><img class=centered src="{0}" width="600" /></a>'.\
        format(img_fn))

    fill = '\n'.join(line for line in fill)

    return fill

def support_files(date, page_stamp, notebook_markup_files, img_dir):
    fn = date + page_stamp + notebook_markup_format
    mkd_file = os.path.join(notebook_markup_files, fn)
    if not os.path.isfile(mkd_file):
        with open(mkd_file, mode='w') as outfile:
            fill = ref_file(page_stamp, img_dir)
            outfile.write(fill)

##,-=========================================================-
##| This is the part that handles the setup of
##| the LaTeX header for the journal
##|
##| Options:
##| (currently working on simple menu to allow quick changes)
##|
##| LaTeX Required Packages:
##| wallpaper
##| fontspec
##| Geometry
##| background
##| ebgaramond
##|
##| Options you might wanna change:
##| user_name
##| user_email
##`-=========================================================-

def preface(vol_no):
    # the date the notebook was created
    user_name = 'Anton Strilchuk'
    user_email = 'anton@isotyp.pe'
    est_date = datetime.date.today().strftime('%B %Y')
    preamble = (r'\documentclass{article}',
                r'\usepackage[paperheight=9.5in,paperwidth=7.31in]{geometry}',
                r'\pagestyle{empty}',
                r'\usepackage{wallpaper}',
                r'\usepackage{fontspec}',
                r'\usepackage{background}',
                r'\usepackage{ebgaramond}',
                r'\SetBgScale{1}',
                r'\SetBgAngle{0}',
                r'\SetBgColor{black}',
                r'\SetBgOpacity{0}',
                r'\SetBgPosition{current page.south}',
                r'\begin{document}',
                r'\vspace*{3cm}',
                r'\NoBgThispage',
                r'\centering',
                r'\begin{Huge}',
                r'\textbf{\emph{Vol. ' + str(vol_no) + r'}}',
                r'\end{Huge}\\',
                r'\vspace{0.1cm}',
                r'\textbf{\emph{' + est_date + r'}}\\',
                r'\vspace{1cm}',
                r'\begin{large}',
                r'' + user_name + '',
                r'\end{large}\\',
                r'\vspace{0.1cm}',
                r''+ user_email + '\\',
                r'\vspace{10cm}',
                r'\newpage',
                r'\section*{Table of Contents}',
                r'\vspace{3cm}',
                r'\centering',
                '\n')

    return '\n'.join(i for i in preamble)


def page_stamps(bookno, page_end=500):
    pages = xrange(0, page_end)
    stamps = (''.join((str(bookno), '-', str(page))) for page in pages)

    return [stamp for stamp in stamps]


def toc_lines(stamps):
    dots = '.' * 100
    eol = ''.join(('\n', r'\newline', '\n', r'\newline'))

    return ''.join('{0:<10}{1}{2}\n'.format(stamp, dots, eol)
            for stamp in stamps)


##,-========-
##| APP LINK
##`-========-
def qr(date, page_stamp, notebook_markup_files):
    qr_handle = ''.join(('qr_', page_stamp, '.png'))
    fn = date + page_stamp + notebook_markup_format
    qr_path = os.path.join(notebook_markup_files, fn)
    img_link = ''.join(('textastic://x-callback-url/open?path=notebook&name=', qr_path))
    img = qrcode.make(img_link)
    img.save(qr_handle)

    return qr_handle

##,-================-
##| Adds QR to pages
##`-================-
def notepage(page_stamp, qr_handle):
    page = (r'\newpage',
            r'\SetBgScale{1}',
            r'\SetBgAngle{0}',
            r'\SetBgColor{black}',
            r'\SetBgOpacity{1}',
            r'\SetBgPosition{current page.south}',
            r'\mbox{}',
            r'\LLCornerWallPaper{1.02}{notebook.eps}',
            r'\SetBgVshift{0.5cm}',
            r'\SetBgContents{' + page_stamp + r'}',
            r'\LRCornerWallPaper{0.09}{' + qr_handle + '}')

    return '\n'.join(i for i in page)

def end():
    return  '\n'.join((r'\newpage',
                       '\n',
                       r'\SetBgOpacity{0}',
                       r'\newpage',
                       r'\ClearWallPaper',
                       r'\thispagestyle{empty}',
                       r'\mbox{}',
                       r'\newpage',
                       '\n',
                       r'\end{document}'))


##,-====-
##| MAIN
##`-====-
def main(notebook_markup_files, img_dir, vol, pages):
    volume_number = int(vol)
    pages = int(pages)
    date = datetime.datetime.today().strftime('%Y-%m-%d-')

    stamps = page_stamps(volume_number, pages)
    [support_files(date, stamp, notebook_markup_files, img_dir) for stamp in stamps]

    with open('notebook.tex', mode='w') as outfile:
        add_preface = preface(vol)
        add_tableofcontents = toc_lines(stamps)
        aggregate = add_preface + add_tableofcontents
        outfile.write(aggregate)
        for stamp in stamps:
            add_qr = qr(date, stamp, notebook_markup_files)
            add_qr_to_pages = notepage(stamp, q)
            outfile.write(add_qr_to_pages)
        put_everything_together = end()
        outfile.write(put_everything_together)

if __name__ == '__main__':
    (notebook_markup_files, img_dir, vol, pages) = sys.argv[1:5]
    main(notebook_markup_files, img_dir, vol, pages)

##,-=====================-
##| notebook.py ends here
##`-=====================-
