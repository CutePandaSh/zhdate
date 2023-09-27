# -*- coding=utf-8 -*-

import unittest
from datetime import datetime
from zhdate import ZhDate


class TestZhdate(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_zhdate_validate(self):
        test_cases = [
            ((1900, 11, 1, False), True),
            ((1900, 11, 29, False), True),
            ((1900, 12, 30, False), True),
            ((2001, 12, 29, False), True),
            ((1909, 2, 29, True), True),
            ((1933, 5, 30, False), True),
            ((1909, 1, 29, True), False),
            ((1909, 2, 30, True), False),
            ((2100, 12, 29, True), False),
            ((2100, 12, 29, False), True),
            ((2100, 12, 30, True), False),
        ]

        for case in test_cases:
            self.assertEqual(ZhDate.validate(*case[0]), case[1])

    def test_yearcode_decode(self):
        test_cases = [
            (19416, [29, 30, 29, 29, 30, 29, 30, 30, 29, 30, 30, 29, 30]),
            (19168, [29, 30, 29, 29, 30, 29, 30, 29, 30, 30, 30, 29]),
            (21717, [29, 30, 29, 30, 29, 29, 30, 29, 29, 30, 30, 29, 30]),
            (91476, [29, 30, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30]),
            (119381, [30, 30, 29, 30, 29, 30, 29, 30, 29, 29, 30, 29, 30])
        ]

        for case in test_cases:
            self.assertEqual(ZhDate.decode(case[0]), case[1])

    def test_to_datetime(self):
        test_cases = [
            ((2100, 11, 27), datetime(2100, 12, 27)),
            ((1903, 5, 17), datetime(1903, 6, 12)),
            ((1903, 5, 17, True), datetime(1903, 7, 11)),
            ((1900, 1, 20), datetime(1900, 2, 19)),
            ((2050, 1, 28), datetime(2050, 2, 19)),
            ((2050, 3, 30, True), datetime(2050, 5, 20)),
            ((1900, 1, 1), datetime(1900, 1, 31))
        ]

        for case in test_cases:
            self.assertEqual(ZhDate(*case[0]).to_datetime(), case[1])

    def test_from_datetime(self):
        test_cases = [
            ((2100, 11, 27), datetime(2100, 12, 27)),
            ((1903, 5, 17), datetime(1903, 6, 12)),
            ((1903, 5, 17, True), datetime(1903, 7, 11)),
            ((1900, 1, 20), datetime(1900, 2, 19)),
            ((1900, 12, 30), datetime(1901, 2, 18)),
            ((2050, 1, 28), datetime(2050, 2, 19)),
            ((2050, 3, 30, True), datetime(2050, 5, 20)),
            ((1900, 1, 1), datetime(1900, 1, 31)),
        ]

        for case in test_cases:
            self.assertEqual(ZhDate.from_datetime(case[1]), ZhDate(*case[0]))

    def test_sub(self):
        test_cases = [
            (ZhDate(2019, 1, 1), ZhDate(2018, 1, 1), 354),
            (ZhDate(2019, 1, 1), 354, ZhDate(2018, 1, 1)),
            (ZhDate(2019, 1, 1), datetime(2018, 2, 16), 354)
        ]

        for case in test_cases:
            self.assertEqual(case[0] - case[1], case[2])

    def test_validate(self):
        test_cases = [
            ((1900, 11, 1, False), True),
            ((1900, 11, 29, False), True),
            ((1900, 12, 30, False), True),
            ((2001, 12, 29, False), True),
            ((1909, 2, 29, True), True),
            ((1933, 5, 30, False), True),
            ((2100, 12, 29, False), True),
            ((1900, 1, 1, False), True),
            ((2020, 4, 29, True), True),
            ((2020, 4, 30, False), True),
            ((2020, 4, 30, True), False),
            ((2020, 3, 30, True), False),
        ]

        for case in test_cases:
            self.assertEqual(ZhDate.validate(*case[0]), case[1])
