import unittest
from unittest import mock
import sys

from main import main

class TestMain(unittest.TestCase):

    @mock.patch('os.path.isfile', return_value=True)
    @mock.patch('main.parse_lookup_table')
    @mock.patch('main.parse_protocol_numbers')
    @mock.patch('main.read_flow_logs')
    def test_main_file_exist(self, mock_read_flow_logs, mock_parse_protocol_numbers, mock_parse_lookup_table,isfile):
        # Mocking the return values
        mock_parse_protocol_numbers.return_value = ['tcp'] * 146
        mock_parse_lookup_table.return_value = {(80, 'tcp'): 'HTTP'}
        
        # Simulate command line arguments
        sys.argv = ['main.py', 'dummy_flow_log_file', 'dummy_lookup_table']
        
        # Call main
        main()
        
        # Assert that read_flow_logs was called
        mock_read_flow_logs.assert_called_once_with('dummy_flow_log_file', mock_parse_lookup_table.return_value, mock_parse_protocol_numbers.return_value)

    @mock.patch('utils.parse_csv.parse_lookup_table')
    def test_main_file_not_exist(self, mock_parse_lookup_table):
        # Simulate command line arguments
        sys.argv = ['main.py', 'dummy_flow_log_file', 'invalid_lookup']
        
        # Call main and check for error
        with self.assertRaises(SystemExit):
            main()

    @mock.patch('utils.parse_csv.parse_lookup_table')
    def test_main_usage_with_no_arguments(self, mock_parse_lookup_table):
        # Simulate command line arguments
        sys.argv = ['main.py']
        
        # Call main and check for error
        with self.assertRaises(SystemExit):
            main()


if __name__ == '__main__':
    unittest.main()
