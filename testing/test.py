import unittest

from src.clean import clean_text


class TestClean(unittest.TestCase):
    def test_clean(self):
        """[Testing if the function cleans the sentence.]
        """
        data = ['This is a 9']
        result = clean_text(data)
        actual_result = 'This is a number'
        self.assertEqual(result, actual_result)