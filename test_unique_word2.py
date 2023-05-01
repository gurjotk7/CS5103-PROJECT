import unittest
from unique_word2 import unique_word

class TestUniqueWord(unittest.TestCase):
    
# Case1- Unit testing to Count the frequency of the word

    def test_count_words(self):
        document_count = "In the project the project"
        expected_word = {'In': 1, 'the':2 , 'project': 2}
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(word_count, expected_word)
    
    def test_punctuation(self):
        document_count = "In ! word"
        expected_word = {'In':1, '!': 1,'word': 1}
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(word_count, expected_word)

    def test_empty_input(self):
        document_count = ""
        expected_word = {}
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(word_count, expected_word)

    def test_with_space(self):
        document_count = "how you are      you"
        expected_word = {'how': 1, 'you':2, 'are': 1}
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(word_count, expected_word)

    def test_with_tab(self):
        document_count = "to\tcount"
        expected_word = {'to': 1, 'count': 1}
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(word_count, expected_word)
        
    def test_with_newline(self):
        document_count = "\n"
        expected_word = {}
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(word_count, expected_word)

    def test_with_combination(self):
        document_count = "has\nto\tcount"
        expected_word = {'has': 1, 'to': 1, 'count': 1}
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(word_count, expected_word)

# Case2- Unit testing to Count the lines

    def test_empty_line(self):
        document_count = ""
        expected_lines = 1
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_lines, expected_lines)

    def test_empty_string(self):
        document_count = "\n\n"
        expected_lines = 3
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_lines, expected_lines)

    def test_one_line_one_string(self):
        document_count = "Hello World"
        expected_lines = 1
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_lines, expected_lines)

    def test_multi_line_one_string(self):
        document_count = "\nHello\n"
        expected_lines = 3
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_lines, expected_lines)
 
    def test_multi_line_multi_string(self):
        document_count = "Hello World!\nGood Morning."
        expected_lines = 2
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_lines, expected_lines)

# Case: 3 Unit testing to count the characters

    def test_empty_input(self):
        document_count = ""
        expected_char = 0
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_char, expected_char)

    def test_count_characters(self):
        document_count = "Hello World"
        expected_char = 10
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_char, expected_char)

    def test_punctuation(self):
        document_count = "ABC ! "
        expected_char = 4
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_char, expected_char)   
       
    def test_with_space(self):
        document_count = "      A B C"
        expected_char = 3
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_char, expected_char)   

    def test_with_specialCharacter(self):
        document_count = "\n\t"
        expected_char = 2
        word_count, num_of_lines, num_of_char = unique_word(document_count)
        self.assertEqual(num_of_char, expected_char)   

        
if __name__ == '__main__':
    unittest.main()
        
