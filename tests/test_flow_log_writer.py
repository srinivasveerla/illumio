import unittest
from unittest.mock import patch, mock_open
from utils.flow_log_writer import write_port_protocol_pairs_to_file, write_tags_to_file

class TestFlowLogWriter(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    def test_write_port_protocol_pairs_to_file(self, mock_file):
        output_dir = "dummy_dir"
        port_protocol_dict = {
            (80, "tcp"): 5,
            (443, "tcp"): 3,
        }
        write_port_protocol_pairs_to_file(output_dir, port_protocol_dict)
        mock_file().write.assert_any_call("Port,Protocol,Count\n")
        mock_file().write.assert_any_call("80,tcp,5\n")
        mock_file().write.assert_any_call("443,tcp,3\n")

    @patch("builtins.open", new_callable=mock_open)
    def test_write_tags_to_file(self, mock_file):
        output_dir = "dummy_dir"
        tags_dict = {
            "HTTP": 5,
            "HTTPS": 3,
        }
        write_tags_to_file(output_dir, tags_dict)
        mock_file().write.assert_any_call("Tag,Count\n")
        mock_file().write.assert_any_call("HTTP,5\n")
        mock_file().write.assert_any_call("HTTPS,3\n")

if __name__ == "__main__":
    unittest.main()
