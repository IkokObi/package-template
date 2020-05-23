#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/03/30 12:53:06 JST.
Last Change: 2019/03/30 13:05:42 JST.

@author: Koki Obinata
"""
from . import stat


def stat_analysis(data):
    """ Calculate statistics """
    analyzer = stat.StatAnalyzer(data=data)
    result = {}
    result["mean"] = analyzer.mean(axis=0)
    result["std"] = analyzer.std(axis=0)
    return result
