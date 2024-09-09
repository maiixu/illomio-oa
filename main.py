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

def main():
    # Step 1: Load the lookup table
    lookup_table_path = 'lookup_table.csv'
    lookup_table = load_lookup_table(lookup_table_path)

    # Step 2: Print the loaded lookup table to verify it loaded correctly
    print("Lookup Table Loaded:")
    for key, value in lookup_table.items():
        print(f"Port: {key[0]}, Protocol: {key[1]} -> Tag: {value}")

if __name__ == "__main__":
    main()