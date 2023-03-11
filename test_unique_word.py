import unittest
from unique_word import unique_word

class TestUniqueWord(unittest.TestCase):

    def test_unique_word_count_words(self):
        document_count = "In the , project\nThe project has to\tcount the frequency of each unique word"
        expected_output = {'In': 1, 'the': 2, ',': 1, 'project': 2, 'The': 1, 'has': 1, 'to': 1, 'count': 1, 'frequency': 1, 'of': 1, 'each': 1, 'unique': 1, 'word': 1}
        self.assertEqual(unique_word(document_count), expected_output)


    def test_punctuation(self):
        document_count = "In the , project\nThe project has to\tcount the frequency of each unique word"
        expected_output = {'In': 1, 'the': 2, ',': 1, 'project': 2, 'The': 1, 'has': 1, 'to': 1, 'count': 1, 'frequency': 1, 'of': 1, 'each': 1, 'unique': 1, 'word': 1}
        self.assertEqual(unique_word(document_count), expected_output)

    def test_empty_input(self):
        document_count = ""
        expected_output = {}
        self.assertEqual(unique_word(document_count), expected_output)

    def test_with_space(self):
        document_count = "how you are      you"
        expected_output = {'how': 1, 'you':2, 'are': 1}
        self.assertEqual(unique_word(document_count), expected_output)

    def test_with_tab(self):
        document_count = "to\tcount"
        expected_output = {'to': 1, 'count': 1}
        self.assertEqual(unique_word(document_count), expected_output)

    def test_with_newline(self):
        document_count = "project\nThe"
        expected_output = {'project': 1, 'The': 1}
        self.assertEqual(unique_word(document_count), expected_output)

    def test_with_combination(self):
        document_count = "has\nto\tcount"
        expected_output = {'has': 1, 'to': 1, 'count': 1}
        self.assertEqual(unique_word(document_count), expected_output)
    

if __name__ == '__main__':
    unittest.main()
