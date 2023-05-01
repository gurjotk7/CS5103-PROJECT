import unittest
from unique_word3 import unique_word

class TestUniqueWord(unittest.TestCase):
    
#1 Unit testing to Count the frequency of the word

    def test_punctuation(self):
        document_count = "In ! word"
        expected_output = {'In':1, '!': 1,'word': 1}
        word= "task"
        new_word = "assignment"   
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)

    def test_empty_input(self):
        document_count = ""
        expected_output = {}
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)

    def test_with_space(self):
        document_count = "how you are      you"
        expected_output = {'how': 1, 'you':2, 'are': 1}
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)

    def test_with_tab(self):
        document_count = "to\tcount"
        expected_output = {'to': 1, 'count': 1}
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)
        
    def test_with_newline(self):
        document_count = "\n"
        expected_output = {}
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)

    def test_with_combination(self):
        document_count = "has\nto\tcount"
        expected_output = {'has': 1, 'to': 1, 'count': 1}
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)

#2 Unit testing to Count the lines

    def test_empty_line(self):
        document_count = ""
        expected_lines = 1
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_lines, expected_lines)

    def test_empty_string(self):
        document_count = "\n\n"
        expected_lines = 3
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_lines, expected_lines)

    def test_one_line_one_string(self):
        document_count = "Hello World"
        expected_lines = 1
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_lines, expected_lines)

    def test_multi_line_one_string(self):
        document_count = "\nHello\n"
        expected_lines = 3
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_lines, expected_lines)
 
    def test_multi_line_multi_string(self):
        document_count = "Hello World!\nGood Morning."
        word= "task"
        new_word = "assignment"
        expected_lines = 2
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_lines, expected_lines)

#3 Unit testing to count the characters

    def test_empty_input1(self):
        document_count = ""
        expected_char = 0
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_char, expected_char)

    def test_count_characters(self):
        document_count = "Hello World"
        expected_char = 10
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_char, expected_char)

    def test_punctuation1(self):
        document_count = "ABC ! "
        expected_char = 4
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_char, expected_char)   
       
    def test_with_space1(self):
        document_count = "      A B C"
        expected_char = 3
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_char, expected_char)   

    def test_with_specialCharacter(self):
        document_count = "\n\t"
        expected_char = 2
        word= "task"
        new_word = "assignment"
        word_count, num_of_lines, num_of_char = unique_word(document_count, word, new_word)
        self.assertEqual(num_of_char, expected_char) 

#4 Unit testing to display the replacement of the word
        
    def test_replace(self):
        document_count = "In the project the proj"
        word= "project"
        new_word = "task"        
        expected_output = {'In': 1, 'the':2 , 'task': 1, 'proj': 1}
        word_count, num_of_lines, num_of_chars = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)
    
    def test_word_not_found(self):
        document_count = "In the project the project"
        word= "task"
        new_word = "assignment"        
        expected_output = {'In': 1, 'the':2 , 'project': 2}
        word_count, num_of_lines, num_of_chars = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)

    def test_empty_file3(self):
        document_count = ""
        word= "task"
        new_word = "assignment"        
        expected_output = {}
        word_count, num_of_lines, num_of_chars = unique_word(document_count, word, new_word)
        self.assertEqual(word_count, expected_output)

      
if __name__ == '__main__':
    unittest.main()
        
