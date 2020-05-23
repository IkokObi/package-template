#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/03/30 13:29:42 JST.
Last Change: 2019/03/30 13:52:48 JST.

@author: Koki Obinata
"""
from unittest import TestCase

from package_template.stat import stat


class TestStat(TestCase):
    def test_mean(self):
        case1 = stat.StatAnalyzer([1, 2, 3])
        case2 = stat.StatAnalyzer([1.5, 2.1, 3])
        case3 = stat.StatAnalyzer([[1.5, 0.5], [2.0, 1.5], [3, 4.0]])

        self.assertAlmostEqual(case1.mean(), 2, places=7)
        self.assertAlmostEqual(case2.mean(), 2.2, places=7)
        self.assertAlmostEqual(case3.mean(axis=0).tolist()[1], 2, places=7)

    def test_std(self):
        case1 = stat.StatAnalyzer([1, 2, 3])
        case2 = stat.StatAnalyzer([1.5, 2.1, 3])
        case3 = stat.StatAnalyzer([[1.5, 0.5], [2.0, 1.5], [3, 4.0]])

        self.assertAlmostEqual(case1.std(), (2 / 3) ** 0.5, places=7)
        self.assertAlmostEqual(case2.std(), (1.14 / 3) ** 0.5, places=7)
        self.assertAlmostEqual(
            case3.std(axis=0).tolist()[1], (6.5 / 3) ** 0.5, places=7
        )
