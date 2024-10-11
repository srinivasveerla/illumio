from utils.parse_csv import parse_protocol_numbers,parse_lookup_table
from utils.flow_log_processor import read_flow_logs

import sys
import os

from logger.log_config import logger

if len(sys.argv) != 3:
    logger.error("Usage: python main.py <flow_log_file> <lookup_dir>")
    sys.exit(1)
elif not os.path.isfile(sys.argv[1]) or not os.path.isfile(sys.argv[2]):
    logger.error("Required files do not exist. Usage: python main.py <flow_log_file> <lookup_dir>")
    sys.exit(1)
else:
    protocols = parse_protocol_numbers("data/protocol-numbers-1.csv")
    look_up_table = parse_lookup_table(sys.argv[2])
    
    read_flow_logs(sys.argv[1], look_up_table, protocols)