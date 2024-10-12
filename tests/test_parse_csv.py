import unittest
from unittest.mock import patch, mock_open
from utils.parse_csv import parse_protocol_numbers, parse_lookup_table

class TestParseCSV(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="Decimal,Keyword\n1,tcp\n2,udp\n145,ipv6")
    def test_parse_protocol_numbers(self, mock_file):
        protocols = parse_protocol_numbers("dummy_path")
        self.assertEqual(protocols[1], "tcp")
        self.assertEqual(protocols[2], "udp")
        self.assertEqual(protocols[145], "ipv6")
        self.assertIsNone(protocols[0])

    @patch("builtins.open", new_callable=mock_open, read_data="dstport,protocol,tag\n80,tcp,HTTP\n443,tcp,HTTPS")
    def test_parse_lookup_table(self, mock_file):
        lookup_table = parse_lookup_table("dummy_path")
        self.assertEqual(lookup_table[(80, "tcp")], "HTTP")
        self.assertEqual(lookup_table[(443, "tcp")], "HTTPS")

if __name__ == "__main__":
    unittest.main()
