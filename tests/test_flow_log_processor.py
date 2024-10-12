import unittest
from unittest import mock
from utils.flow_log_processor import read_flow_logs

class TestFlowLogProcessor(unittest.TestCase):

    @mock.patch('builtins.open', new_callable=mock.mock_open, read_data='2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 0 25 20000 1620140761 1620140821 ACCEPT OK')
    @mock.patch('utils.flow_log_processor.write_port_protocol_pairs_to_file')
    @mock.patch('utils.flow_log_processor.write_tags_to_file')
    def test_read_flow_logs_calls_writer_functions(self, mock_write_tags_to_file, mock_write_port_protocol_pairs_to_file, mock_open):
        mock_write_port_protocol_pairs_to_file.return_value = None
        mock_write_tags_to_file.return_value = None
        
        # Create a mock flow log data
        mock_filename = 'dummy_flow_log_file'
        mock_look_up_table = {(80, 'tcp'): 'HTTP'}
        mock_protocols = ['tcp']
        
        # Call the function under test
        read_flow_logs(mock_filename, mock_look_up_table, mock_protocols)
        
        # Assert that the writing functions were called
        # Adjust these checks based on the expected behavior of your function
        mock_write_port_protocol_pairs_to_file.assert_called_once()
        mock_write_tags_to_file.assert_called_once()

    @mock.patch('builtins.open', new_callable=mock.mock_open,
                read_data='2 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 0 25 20000 1620140761 1620140821 ACCEPT OK\ninvalid data')
    @mock.patch('utils.flow_log_processor.write_port_protocol_pairs_to_file')
    @mock.patch('utils.flow_log_processor.write_tags_to_file')
    def test_read_flow_logs_calls_writer_with_correct_data(self, mock_write_tags_to_file,
                                                           mock_write_port_protocol_pairs_to_file, mock_open):
        # Create mock data and arguments
        mock_filename = 'dummy_flow_log_file'
        mock_look_up_table = {(49153, 'tcp'): 'HTTPS'}
        mock_protocols = ['tcp']

        # Call the function under test
        read_flow_logs(mock_filename, mock_look_up_table, mock_protocols)

        # Expected data for port-protocol pairs and tags
        expected_port_protocol_dict = {(49153, 'tcp'): 1}
        expected_tags_dict = {'HTTPS': 1}

        # Assert that the write_port_protocol_pairs_to_file was called with the correct data
        mock_write_port_protocol_pairs_to_file.assert_called_once_with('out/', expected_port_protocol_dict)

        # Assert that the write_tags_to_file was called with the correct data
        mock_write_tags_to_file.assert_called_once_with('out/', expected_tags_dict)

    @mock.patch('builtins.open', new_callable=mock.mock_open,
                read_data='invalid data')
    @mock.patch('utils.flow_log_processor.write_port_protocol_pairs_to_file')
    @mock.patch('utils.flow_log_processor.write_tags_to_file')
    @mock.patch('utils.flow_log_processor.logger')
    def test_read_flow_logs_logs_warning_for_invalid_data(self, mock_logger, mock_write_tags_to_file,
                                                          mock_write_port_protocol_pairs_to_file, mock_open):
        mock_write_port_protocol_pairs_to_file.return_value = None
        mock_write_tags_to_file.return_value = None

        # Create mock data and arguments
        mock_filename = 'dummy_flow_log_file'
        mock_look_up_table = {(443, 'tcp'): 'HTTPS'}
        mock_protocols = ['tcp']

        # Call the function under test
        read_flow_logs(mock_filename, mock_look_up_table, mock_protocols)

        # Assert that the logger.warning was called for invalid data
        mock_logger.warning.assert_called_with('Unsupported flow log line: %s', 'invalid data')

        # Assert that the writer functions were called for valid data
        mock_write_port_protocol_pairs_to_file.assert_called_once()
        mock_write_tags_to_file.assert_called_once()

    @mock.patch('builtins.open', new_callable=mock.mock_open,
                read_data='3 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 0 25 20000 1620140761 1620140821 ACCEPT OK')
    @mock.patch('utils.flow_log_processor.write_port_protocol_pairs_to_file')
    @mock.patch('utils.flow_log_processor.write_tags_to_file')
    @mock.patch('utils.flow_log_processor.logger')
    def test_read_flow_logs_logs_warning_for_unsupported_version(self, mock_logger, mock_write_tags_to_file,
                                                          mock_write_port_protocol_pairs_to_file, mock_open):
        mock_write_port_protocol_pairs_to_file.return_value = None
        mock_write_tags_to_file.return_value = None

        # Create mock data and arguments
        mock_filename = 'dummy_flow_log_file'
        mock_look_up_table = {(443, 'tcp'): 'HTTPS'}
        mock_protocols = ['tcp']

        # Call the function under test
        read_flow_logs(mock_filename, mock_look_up_table, mock_protocols)

        # Assert that the logger.warning was called for invalid data
        mock_logger.warning.assert_called_with('Unsupported flow log line: %s', '3 123456789012 eni-0a1b2c3d 10.0.1.201 198.51.100.2 443 49153 0 25 20000 1620140761 1620140821 ACCEPT OK')

        # Assert that the writer functions were called for valid data
        mock_write_port_protocol_pairs_to_file.assert_called_once()
        mock_write_tags_to_file.assert_called_once()


if __name__ == '__main__':
    unittest.main()
