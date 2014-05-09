# Jorgen

Jorgen is a custom journal tool that creates a printable PDF journal
that can be easily folded and bound at home.

Jorgen is required by [Offprint](https://github.com/offprint/offprint), a frontend web app for Jorgen.

To start using Jorgen, check out <https://offprint.github.io/>

- [Using Jorgen](#using-jorgen)
- [Examples](#examples)
- [Templates for Jorgen](#templates-for-jorgen)
- [Hacking Jorgen](#hacking-jorgen)
- [TODO](#todo)

## Why not just buy a journal?

Jorgen was not created to make buying journals, notebooks, diaries and
the like obsolete - but rather to create an alternative option for
those who want to be able to have full control over the page content
of their journals. There are a few options available which all ready
provide some of this functionality, unfortunately they fall short by
either offering a limited amount of templates to choose from, or only
allowing for the customization of cover and back, and not the actual
page content.

There are customized journals from a variety of companies covering a
range of different themes and topics, however these are few and far
between and can be ridgley stuck to one specific field, or another.

Jorgen is designed to tackle the themes that haven't been created, and
offer a way to create a journals more that is defined by you and
specific to your needs - which is accomplished through a massive
selection of templates that can be arrange, and added whenever and
where ever you want them.

## Using Jorgen

The Makefile associated with Jorgen has a few different options to
allow you to quickly generate your notebook. The easiest way to get
started is with this command.

Change the volume number and pages. Also you may want to open up
Jorgen.py and edit the user_name

```sh
make VOL=1 PAGES=10 USER_NAME="Your Name" USER_EMAIL="Your Email"
```

## TODO

### Command Line Menu for setting options

Jorgen needs some sort of menu to set various LaTeX, and markup
options, as well as preferences associated with printing.

### Tutorial on Creating your own Templates

A tutorial on how to create your own templates would be useful - this
can be accomplished by moving template settings out of the main
generator into a seperate file.

With a seperate template file, templates could be quickly parsed by
the generator to output the resulting notebook.

### Handwritten Text Recognition

A major goal of the Jorgen project is to be able to one day scan the
pages of a Jorgen Journal and have it automatically converted to text
using [Handwriting Recognition](http://en.wikipedia.org/wiki/Handwriting_recognition).

This tool is a work in progress, and is available to
developers in the [offhand](https://github.com/offprint/offhand) repo.
