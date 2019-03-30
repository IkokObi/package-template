#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/03/30 12:56:39 JST.
Last Change: 2019/03/30 13:01:42 JST.

@author: Koki Obinata
"""
import textwrap


def greet(name='NoName'):
    description = """\
    Hello {}!
    I'm Koki Obinata.
    This repository is template for Python package.
    Have a great project!\
    """.format(name)
    print(textwrap.dedent(description))
