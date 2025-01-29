import os
from datetime import datetime

# Folder to store files
folder_path = "generated_files"
os.makedirs(folder_path, exist_ok=True)

# Get current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = os.path.join(folder_path, f"{timestamp}.txt")

# Create file and write "Hello World"
with open(file_path, "w") as f:
    f.write("Hello World")

print(f"File created: {file_path}")
