import csv

def load_lookup_table(file_path):
    lookup = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            dstport = row[0].strip()
            protocol = row[1].strip().lower()  # Make protocol case-insensitive
            tag = row[2].strip()
            lookup[(dstport, protocol)] = tag
    return lookup

def parse_flow_logs(file_path):
    flow_logs = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row
        for row in reader:
            dstport = row[6]  # Destination port is the 7th field
            protocol_number = row[7]  # Protocol number is the 8th field
            # Convert protocol number to name (TCP/UDP/ICMP)
            protocol = map_protocol_number(protocol_number)
            flow_logs.append((dstport, protocol))
    return flow_logs

def map_protocol_number(protocol_number):
    protocol_map = {
        '6': 'tcp',
        '17': 'udp',
        '1': 'icmp'
    } # Map protocol numbers to names
    return protocol_map.get(protocol_number, 'unknown')

def tag_flow_logs(flow_logs, lookup_table):
    tagged_logs = []
    for dstport, protocol in flow_logs:
        tag = lookup_table.get((dstport, protocol), 'Untagged')
        tagged_logs.append((dstport, protocol, tag))
    return tagged_logs

def main():
    # Step 1: Load the lookup table
    lookup_table_path = 'lookup_table.csv'
    lookup_table = load_lookup_table(lookup_table_path)

    print("Lookup Table Loaded:")
    for key, value in lookup_table.items():
        print(f"Port: {key[0]}, Protocol: {key[1]} -> Tag: {value}")

    # Step 2: Parse the flow logs
    flow_log_path = 'flow_logs.csv'
    flow_logs = parse_flow_logs(flow_log_path)

    print("\nFlow Logs Parsed:")
    for dstport, protocol in flow_logs:
        print(f"Destination Port: {dstport}, Protocol: {protocol}")

    # Step 3: Tag the flow logs
    tagged_logs = tag_flow_logs(flow_logs, lookup_table)

    # Step 4: Print tagged flow logs to verify
    print("\nTagged Flow Logs:")
    for dstport, protocol, tag in tagged_logs:
        print(f"Destination Port: {dstport}, Protocol: {protocol}, Tag: {tag}")

if __name__ == "__main__":
    main()