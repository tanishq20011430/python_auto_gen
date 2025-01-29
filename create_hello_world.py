import os
from datetime import datetime

# Define folder path inside the repo
folder_path = "generated_files"
os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist

# Generate file name based on timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = os.path.join(folder_path, f"{timestamp}.txt")

# Write "Hello World" to the file
with open(file_path, "w") as f:
    f.write("Hello World")

print(f"File created: {file_path}")
