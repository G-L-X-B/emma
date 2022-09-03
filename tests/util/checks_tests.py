import unittest

from emma.util.checks import *


class CheckWordTest(unittest.TestCase):
    def test_correct_input(self):
        self.assertIsNone(check_word('a'), 'One character is a word.')
        self.assertIsNone(check_word('word'), 'Lowercase letters are considered a word.')
        self.assertIsNone(check_word('WORD'), 'Uppercase letters are considered a word.')
        self.assertIsNone(check_word('14'), 'Digits are considered a word.')
        self.assertIsNone(check_word('abc123'), 'Letters and digits together are a one word.')
        self.assertIsNone(check_word('123abc'), 'Letters and digits together are a one word.')
        self.assertIsNone(check_word('.,:;!?<>/\\|@#$%^&*()_-+=\'\"'), 'A word can contain one or more special characters.')

    def test_not_str_input(self):
        with self.assertRaises(TypeError, msg='Given wrong type must raise TypeError.'):
            check_word(object)

    def test_empty_string(self):
        with self.assertRaises(ValueError, msg='Given empty string must raise ValueError.'):
            check_word('')

    def test_containing_whitespace(self):
        with self.assertRaises(ValueError, msg='String containing whitespaces is not a word.'):
            check_word(' ')
            check_word(' a')
            check_word('a ')
            check_word('a b')


class CheckIsIdentifierTest(unittest.TestCase):
    def test_correct_input(self):
        self.assertIsNone(check_isidentifier('af12_'), 'Should be a valid identifier.')
        self.assertIsNone(check_isidentifier('_'), 'Should be a valid identifier.')
        self.assertIsNone(check_isidentifier('__'), 'Should be a valid identifier.')

    def test_not_str_input(self):
        with self.assertRaises(TypeError, msg='Given wrong type must raise TypeError.'):
            check_isidentifier(object)

    def test_special_characters(self):
        with self.assertRaises(ValueError, msg='Given string containing special characters must raise ValueError.'):
            check_isidentifier(' ')
            check_isidentifier('.,')
            check_isidentifier('%')
