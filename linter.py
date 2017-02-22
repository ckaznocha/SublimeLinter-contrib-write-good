#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Clifton Kaznocha
# Copyright (c) 2014 Clifton Kaznocha
#
# License: MIT
#

"""This module exports the WriteGood plugin class."""

from SublimeLinter.lint import Linter, highlight


class WriteGood(Linter):

    """Provides an interface to write-good."""

    syntax = ('markdown', 'plain text')
    cmd = ('write-good')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    regex = r'''(?xi)
        ^(?P<message>(?P<near>"[^"]*").*)\son\sline\s(?P<line>\d+)\sat\scolumn\s\d+$
    '''
    multiline = True
    default_type = highlight.WARNING
    selectors = {
        'source': 'comment',
        'text.html.markdown': '*',
        'text.plain': '*',
        'text.tex.latex': '*'
    }
    tempfile_suffix = '.tmp'
