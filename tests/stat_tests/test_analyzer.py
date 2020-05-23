#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/03/30 13:48:33 JST.
Last Change: 2019/03/30 13:54:39 JST.

@author: Koki Obinata
"""
from unittest import TestCase

from package_template import stat


class TestAnalyzer(TestCase):
    def test_stat_analysis(self):
        case1 = stat.stat_analysis([1, 2, 3])
        case2 = stat.stat_analysis([[1.5, 0.5], [2.2, 1.5], [3.5, 4.0]])
        self.assertAlmostEqual(case1["mean"], 2, places=7)
        self.assertAlmostEqual(case1["std"], (2 / 3) ** 0.5, places=7)
        self.assertAlmostEqual(case2["mean"][0], 2.4, places=7)
        self.assertAlmostEqual(case2["std"][1], (6.5 / 3) ** 0.5, places=7)
