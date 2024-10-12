from collections import defaultdict

from utils.flow_log_writer import write_port_protocol_pairs_to_file, write_tags_to_file
from logger.log_config import logger


    
def read_flow_logs(filename, look_up_table, protocols):
    """
    Reads a flow log file and counts the number of times each port-protocol
    pair and tag appear.
    writes the port-protocol pairs to a out/port_protocol_pairs.csv file and 
    the tags to a out/tags_count.csv file

    Args:
        filename (str): The name of the flow log file to read.
        look_up_table (dict): A dictionary mapping port-protocol pairs to tags.
        protocols (list): A list of 146 protocol keywords, where index i is the
            keyword associated with protocol number i.
    Returns:
        None
    """
    
    tags_dict = defaultdict(int)
    for (dstport, protocol), tag in look_up_table.items():
        tags_dict[tag] = 0
    port_protocol_dict = defaultdict(int)
    logger.info("Reading flow log from %s", filename)
    with open(filename,'r') as f:
        for line in f:
            log_parts = line.strip().split(" ")
            if log_parts[0] != "2" or len(log_parts)!= 14:
                logger.warning("Unsupported flow log line: %s", line)
                continue
            dstport = int(log_parts[6])
            protocol_decimal = int(log_parts[7])
            protocol_kw  = protocols[protocol_decimal]
            # Count the number of times a port-protocol pair appears
            port_protocol_dict[(dstport,protocol_kw )] += 1
            # Count the number of times a tag appears
            if (dstport, protocol_kw) in look_up_table:
                tags_dict[look_up_table[(dstport, protocol_kw)]] += 1
            else:
                tags_dict["Untagged"] += 1

    output_dir = 'out/'
    write_port_protocol_pairs_to_file(output_dir, port_protocol_dict)
    write_tags_to_file(output_dir, tags_dict)    
