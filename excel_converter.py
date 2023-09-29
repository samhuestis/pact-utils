import csv
import json

# Function to convert CSV to JSON with custom naming
def csv_to_json(csv_file, json_file):
    data = []

    # Custom mapping for object name conversions
    name_mapping = {
        "ext": "extension",
        "bf": "benchmarkingFootprint",
        "ms": "mineToSmelter",
        "va": "valueAddedProduct",
        "fb": "fullBoundary"
    }

    # Read the CSV file and convert it to a list of dictionaries
    with open(csv_file, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            new_row = {}
            for key, value in row.items():
                parts = key.split('.')
                current_dict = new_row
                
                for part in parts[:-1]:
                    current_key = name_mapping.get(part, part)
                    if current_key not in current_dict:
                        current_dict[current_key] = {}
                    current_dict = current_dict[current_key]
                
                # Special handling for the first object
                if parts[0] == "bf":
                    current_dict[name_mapping.get(parts[0])] = {parts[1]: value}
                else:
                    last_part = name_mapping.get(parts[-1], parts[-1])
                    current_dict[last_part] = value
            
            data.append(new_row)

    # Write the list of dictionaries to a JSON file
    with open(json_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Input and output file names
csv_filename = 'data.csv'
json_filename = 'data.json'

# Convert the CSV file to JSON
csv_to_json(csv_filename, json_filename)

print(f"CSV file '{csv_filename}' has been converted to JSON file '{json_filename}'.")
