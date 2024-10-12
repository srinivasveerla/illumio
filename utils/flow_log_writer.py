import os
from logger.log_config import logger
def write_port_protocol_pairs_to_file(output_dir, port_protocol_dict):
        """
        Writes the port-protocol pairs to a CSV file.
    
        Args:
            output_dir (str): The directory where the output file will be written.
            port_protocol_dict (dict): A dictionary where each key is a tuple of a dstport and a protocol,
                and each value is the count of the pair.     
        Return:
            None
        """
        logger.info("Writing port-protocol pairs to file")
        with open(os.path.join(output_dir, 'port_protocol_pairs.csv'), 'w') as f:
            f.write("Port,Protocol,Count\n")
            for (dstport, protocol), count in port_protocol_dict.items():
                f.write(f"{dstport},{protocol},{count}\n")
    
    
def write_tags_to_file(output_dir, tags_dict):
    """
    Writes the tags to a CSV file.

    Args:
        output_dir (str): The directory where the output file will be written.
        tags_dict (dict): A dictionary where each key is a tag, and each value is the count of the tag.
    Return:
        None
    """
    logger.info("Writing tags to file")
    with open(os.path.join(output_dir, 'tags_count.csv'), 'w') as f:
        f.write("Tag,Count\n")
        for tag, count in tags_dict.items():
            f.write(f"{tag},{count}\n")
