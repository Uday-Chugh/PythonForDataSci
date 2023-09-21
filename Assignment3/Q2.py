import os
import random
import string
import time
import csv

# Directory where you want to create the text files
output_directory = "python 4"

# Number of text files to create
num_files = [100, 200, 300, 400, 500]

# Number of lines per file
num_lines = 20000

# Length of each line (number of characters)
line_length = 20

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Create a CSV file to save the results
results_file = "conversion_results.csv"

# Initialize the results data
results_data = []

# Generate and write the text files
for num in num_files:
    filename = os.path.join(output_directory, f"file_{num}.txt")
    
    # Generate random data and write to the file
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            random_line = ''.join(random.choice(string.ascii_letters) for _ in range(line_length))
            file.write(random_line + '\n')
    
    # Measure the time taken to convert the file to uppercase
    start_time = time.time()
    with open(filename, 'r') as file:
        data = file.read()
        data_upper = data.upper()
    with open(filename, 'w') as file:
        file.write(data_upper)
    end_time = time.time()
    
    # Calculate the time taken in seconds
    elapsed_time = end_time - start_time
    
    # Append the results to the data list
    results_data.append((num, elapsed_time))

# Write the results to the CSV file
with open(results_file, 'w', newline='') as csvfile:
    fieldnames = ["No. of Files", "Time Taken (sec)"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for num, elapsed_time in results_data:
        writer.writerow({"No. of Files": num, "Time Taken (sec)": elapsed_time})

print(f'Results have been saved in {results_file}.')
