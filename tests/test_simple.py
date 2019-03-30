#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on : 2019/03/30 13:17:17 JST.
Last Change: 2019/03/30 13:20:41 JST.

@author: Koki Obinata
"""
from unittest import TestCase
from package_template import simple


class TestSimple(TestCase):
    def test_cast_int(self):
        self.assertEqual(simple.cast_int(1.4), 1)
        self.assertEqual(simple.cast_int(4.8), 4)

    def test_cast_str(self):
        self.assertEqual(simple.cast_str(4.2), '4.2')
        self.assertEqual(simple.cast_str(1421), '1421')
