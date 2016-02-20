#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_stack
----------------------------------

Tests for `python_algorithms.stack` module.
"""

import unittest

from python_algorithms.basic.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self.empty_stack = Stack()
        self.stack = Stack()
        self.seq = [0, 2, 4, 6, 8]
        for x in self.seq:
            self.stack.push(x)

    def test_push_to_empty_stack(self):
        self.empty_stack.push(0)
        self.assertEqual(self.empty_stack.peek(), 0)

    def test_push_to_stack(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)

    def test_pop_from_empty_stack(self):
        self.assertRaises(IndexError, self.empty_stack.pop)

    def test_pop_from_stack(self):
        self.assertEqual(self.stack.pop(), self.seq[-1])

    def test_size_of_empty_stack(self):
        self.assertEqual(self.empty_stack.size, 0)

    def test_size_of_stack(self):
        self.assertEqual(self.stack.size, len(self.seq))

    def test_peek_at_empty_stack(self):
        self.assertRaises(IndexError, self.empty_stack.peek)

    def test_peek_at_stack(self):
        self.assertEqual(self.stack.peek(), self.seq[-1])

    def test_iterate_empty_stack(self):
        for curr in self.empty_stack:
            self.assertEqual(False, True)

    def test_iterate_stack(self):
        iter_seq = []
        for curr in self.stack:
            iter_seq.append(curr)
        iter_seq.reverse()
        self.assertEqual(iter_seq, self.seq)

    def test_str_empty_stack(self):
        self.assertEqual(str(self.empty_stack), "")

    def test_str_stack(self):
        self.assertEqual(str(self.stack), " ".join([str(x) for x in self.seq]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
