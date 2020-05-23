#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/03/30 12:44:06 JST.
Last Change: 2019/03/30 12:52:21 JST.

@author: Koki Obinata
"""
import numpy as np


class StatAnalyzer(object):
    """
    Class for statistic analysis.

    Parameters
    ----------
    data : array-like
        n-dimensional list or array-like object are available.
        This data will be passed to numpy.array()
    """

    def __init__(self, data):
        self.data = np.array(data)

    def mean(self, axis=None):
        """ Return mean value of data """
        return self.data.mean(axis=axis)

    def std(self, axis=None):
        """ Return standard deviation of data """
        return self.data.std(axis=axis)
