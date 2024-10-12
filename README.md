# Flow Log Processing Project

## Overview

This solution processes flow logs and generates two output files: 
- **Port-Protocol-Count File**: Contains the count of port-protocol pairs observed in the logs (at out/port_protocol_pairs.csv).
- **Tags File**: Contains the count of flow logs associated with a specific tag from the lookup table (at out/tags_count.csv).

The solution is written in Python and does not rely on any non-default libraries.
## Assumptions 
   - The program assumes the log lines adhere to the **version 2** format described in the [AWS documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-log-records.html).
   - Custom formats are not supported.
   - The lookup table file is assumed to be a **CSV file** (with columns - dstport,protocol,tag).
   - The lookup table uses **protocol names** (e.g., 'tcp') instead of protocol decimal values. A mapping is created between protocol decimal codes and keywords based on the [Assigned Internet Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml).
   - The **destination port** (`dstport`) field is assumed to be the port when generating the port-protocol combinations count.
   - Support flow log files with standard encoding.
  **Outputs**
   - Both output files are written in **CSV format**.
   - The program generates:
     - `port_protocol_count.csv`: Contains port, protocol, and count of occurrences.
     - `tags_count.csv`: Contains tags and their counts.

## Running the Program

### Prerequisites
- **Python 3.x** installed on your local machine.
- Ensure the flow log and lookup table files are available in the correct format.

### Steps to Compile/Run

1. Clone the repository:
   ```bash
   git clone https://github.com/srinivasveerla/illumio.git
   cd illumio
   ```

2. Run the program:
   replace python3 with python for windows machines.
   ```bash
   python3 main.py <path to flow-log> <path to lookup-table>
   ```

   Example:
   ```bash
   python3 main.py logs/flow_log lookup_table.csv
   ```

   This will process the provided flow log and lookup table, generating the following output files in the `out/` folder:
   - `port_protocol_count.csv`
   - `tags_count.csv`

## Testing

Unit tests have been written for the solution for various components involved.

### Running Tests
Run the following command to execute the test cases:
```bash
python3 -m unittest discover tests/
```

### Test Cases
1. **test_main**: Tests the main flow of the program with valid and invalid inputs.
2. **test_flow_log_processor**: Verifies that the correct data is passed to the output files, and checks if functions handle incorrect input formats correctly.
3. **Edge Cases**: Includes scenarios where:
   - The log line format is incorrect (e.g., wrong version or missing fields).
   - The log line format doesn't have 14 fields, as expected from version 2 logs.

## Analysis
- The flow log file size can be up to 10MB, containing approximately 60,000 logs. The complexity of processing depends on the size of the input file.
- The code avoids the use of non-default Python libraries to ensure ease of setup and portability.
- Supports all types of standard protocols.
  
