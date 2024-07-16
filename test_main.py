import unittest
from io import StringIO
from unittest.mock import patch
import main  

class TestPredefinedWordsMatcher(unittest.TestCase):

    def setUp(self):
        # Create mock input files content
        self.mock_input = "Detecting first names is tricky to do even with AI.\n" \
                          "how do you say a street name is not a first name?\n"
        self.mock_predefined = "Name\nDetect\nAI\n"

    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.argv', new=['main.py', 'input.txt', 'predefined_words.txt'])
    def test_main_program_output(self, mock_stdout):
        # Mock input files
        with patch('builtins.open', side_effect=[StringIO(self.mock_input), StringIO(self.mock_predefined)]):
            main.main()
            output = mock_stdout.getvalue().strip()
            
            # Adjust expected output to match case insensitivity and formatting
            expected_output = (
                "Predefined word     Match count\n"
                "Name                 2\n"
                "Detect               0\n"
                "AI                   1"
            ).strip()
            
            # Normalize both outputs to lowercase for comparison
            output_lines = [line.lower() for line in output.splitlines()]
            expected_lines = [line.lower() for line in expected_output.splitlines()]
            
            # Compare normalized outputs
            for actual, expected in zip(output_lines, expected_lines):
                self.assertEqual(actual.strip(), expected.strip())

    @patch('sys.stdout', new_callable=StringIO)
    @patch('sys.argv', new=['main.py', 'empty_input.txt', 'predefined_words.txt'])
    def test_empty_input_file(self, mock_stdout):
        # Mock empty input file
        with patch('builtins.open', side_effect=[StringIO(""), StringIO(self.mock_predefined)]):
            main.main()
            output = mock_stdout.getvalue().strip()
            
            # Adjust expected output for an empty input file scenario
            expected_output = (
                "Predefined word     Match count\n"
                "Name                 0\n"
                "Detect               0\n"
                "AI                   0"
            ).strip()
            
            # Normalize both outputs to lowercase for comparison
            output_lines = [line.lower() for line in output.splitlines()]
            expected_lines = [line.lower() for line in expected_output.splitlines()]
            
            # Compare normalized outputs
            for actual, expected in zip(output_lines, expected_lines):
                self.assertEqual(actual.strip(), expected.strip())

if __name__ == '__main__':
    unittest.main()
