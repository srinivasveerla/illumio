import csv

from logger.log_config import logger

def parse_protocol_numbers(filename):
    """
    Returns a list for 146 defined protocols, where index i is the decimal associated
    with the protocol and protocol[i] is the keyword. The list is populated by reading the csv file 
    found here - https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml

    Args:
        filename (str): The name of the file containing the protocol numbers.
    Returns:
        list: A list of 146 defined protocols, where index i is the decimal associated
            with the protocol and protocol[i] is the keyword.
    """
    logger.info(f"Reading protocol numbers from {filename}")
    protocols = [None]*146
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            protocol_number = int(row['Decimal'])
            kw = row['Keyword'].lower()
            protocols[protocol_number] = kw
            if protocol_number == 145:
                break
    logger.info("Finished reading protocol numbers")
    return protocols

def parse_lookup_table(file_path):
    """
    Returns a dictionary where each key is a tuple of a dstport and a protocol
    and each value is a tag. The dictionary is populated by reading the csv file 
    of the look up table

    Args:
        file_path (str): The path to the csv file of the look up table
    Returns:
        dict: A dictionary where each key is a tuple of a dstport and a protocol
            and each value is a tag.
    """
    logger.info(f"Loading lookup table from {file_path}")
    lookup_table = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            port = int(row['dstport'])
            protocol = row['protocol'].lower()
            tag = row['tag']
            lookup_table[(port, protocol)] = tag
    logger.info("Finished loading lookup table")
    return lookup_table
if __name__ == "__main__":
    parse_protocol_numbers('../data/protocol-numbers-1.csv')
    parse_lookup_table('../data/lookup_table.csv')

