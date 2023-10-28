import glob
import datetime

# Get the current date in the format "dd-Mon-YYYY"
current_date_str = datetime.datetime.now().date().strftime("%d-%b-%Y")

# Construct the file name with the current date
search_pattern = f"MA-Equities-CM-volume-{current_date_str}.csv"

# Use glob.glob to search for the file with the specific name pattern in the current directory
matching_files = glob.glob(search_pattern)

# Print the list of matching files
for file in matching_files:
    print(file)

# Read and print the contents of matching files
for file in matching_files:
    with open(file, 'r') as f:
        file_contents = f.read()
        print(f"Contents of {file}:")
        print(file_contents)