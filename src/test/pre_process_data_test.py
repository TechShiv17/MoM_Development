import unittest
from src.utils.pre_process_data import DataPreProcessing


class DataPreProcessingTest(unittest.TestCase):

    def test_clean_no_special_characters(self):
        # Test input text without any special characters
        input_text = "This is a simple test text without any special characters."
        cleaned_text = DataPreProcessing.clean(input_text)
        self.assertEqual(cleaned_text, input_text.lower())

    def test_clean_with_special_characters(self):
        # Test input text with special characters
        input_text = "This is a test, text with 'quotes' [and] new line."
        cleaned_text = DataPreProcessing.clean(input_text)
        expected_output = "this is a test text with quotes and new line."
        self.assertEqual(cleaned_text, expected_output.lower())

    def test_clean_empty_input(self):
        # Test empty input text
        input_text = ""
        cleaned_text = DataPreProcessing.clean(input_text)
        self.assertEqual(cleaned_text, input_text.lower())

    def test_clean_only_special_characters(self):
        # Test input with only special characters
        input_text = ",[]"
        cleaned_text = DataPreProcessing.clean(input_text)
        self.assertEqual(cleaned_text, "")

    def test_clean_all_uppercase(self):
        # Test input with all uppercase characters
        input_text = "THIS IS AN ALL UPPERCASE TEXT."
        cleaned_text = DataPreProcessing.clean(input_text)
        expected_output = "this is an all uppercase text."
        self.assertEqual(cleaned_text, expected_output)

    def test_clean_with_mixed_characters(self):
        # Test input with mixed characters
        input_text = "This is a test with mixed characters ,[]."
        cleaned_text = DataPreProcessing.clean(input_text)
        expected_output = "this is a test with mixed characters ."
        self.assertEqual(cleaned_text, expected_output)
