#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:21:59 2024

@author: ceccas
"""

import unittest

class TestSmall(unittest.TestCase):
    def test_is_true(self):
        self.assertIsTrue(1 + 1 == 2)