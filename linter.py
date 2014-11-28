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

    syntax = '*'
    cmd = ('write-good')
    regex = r'''(?xi)
        ^(?P<message>(?P<near>"[^"]*").*)\son\sline\s(?P<line>\d+)\sat\scolumn\s\d+$
    '''
    multiline = True
    default_type = highlight.WARNING
    tempfile_suffix = '.tmp'
