import unittest

from title_func import title


# title from title_func should behave the same way as title from builtins
class TestTitleFunc(unittest.TestCase):

    def test_capitalize_first_letter(self):
        input_str = "hello world"
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_not_modify_capitalized_words(self):
        input_str = "Hello World"
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_handle_single_word_sentence(self):
        input_str = "hello"
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_handle_consecutive_spaces(self):
        input_str = "hello     world"
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_handle_non_ascii_characters(self):
        input_str = "héllö wörld"
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_handle_leading_trailing_spaces(self):
        input_str = "  hello world  "
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_empty_string(self):
        input_str = ""
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_sentence_with_numbers_and_special_characters(self):
        input_str = "  hello    wor123ld! "
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_sentence_with_non_alphabetic_characters(self):
        input_str = "!@#$%^&*()"
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_russian_lowercase(self):
        input_str = "  привет    ми123р!ф "
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)

    def test_russian_not_modify(self):
        input_str = "  Привет    Ми123Р!Ф "
        expected_output = input_str.title()
        self.assertEqual(title(input_str), expected_output)


if __name__ == '__main__':
    unittest.main()
