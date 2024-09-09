# Flow Log Parser

This Python program parses flow log data and a lookup table, maps each flow log entry to a tag, and generates an output file with:

1.	The count of matches for each tag.
2.	The count of matches for each port/protocol combination.

## Assumptions

- Supported Log Version: Only version 2.
- Protocols: Supports TCP (6), UDP (17), and ICMP (1).
- Unknown Entries: Entries with no match are tagged as Untagged.
- Lookup Table: CSV format with dstport, protocol, and tag.

## Run the Program

1.	Place flow_logs.csv and lookup_table.csv in the same directory as the program.
2.	Run the program:

```bash
python main.py
```

3.	Output file flow_log_analysis_output.txt will be generated.