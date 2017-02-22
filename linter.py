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

from SublimeLinter.lint import NodeLinter, highlight


class WriteGood(NodeLinter):
    """Provides an interface to write-good."""

    syntax = ('*')
    cmd = ('write-good')
    npm_name = 'write-good'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = ">=0.9.0"
    regex = r'''(?xi)
        ^(?P<message>(?P<near>"[^"]*").*)\son\sline\s(?P<line>\d+)\sat\scolumn\s\d+$
    '''
    multiline = True
    default_type = highlight.WARNING
    selectors = {
        '*': 'text.html.markdown, text.plain, text.tex.latex, comment'
    }
    tempfile_suffix = '.tmp'
