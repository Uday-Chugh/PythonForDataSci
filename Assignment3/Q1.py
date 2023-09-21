import os
import random
import string

# Directory where you want to create the files
directory = "text_files"
os.makedirs(directory, exist_ok=True)

# Number of files to create
num_files = 500

# Number of lines in each file
num_lines = 20000

# Length of each random string
string_length = 20

# Function to generate a random string of given length
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Create 500 text files
for i in range(1, num_files + 1):
    file_name = f"{directory}/file_{i}.txt"
    with open(file_name, "w") as file:
        for _ in range(num_lines):
            random_string = generate_random_string(string_length)
            file.write(f"{random_string}\n")

print(f"{num_files} files created in '{directory}' directory.")
