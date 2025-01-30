import os
from datetime import datetime

folder_path = "generated_files"
os.makedirs(folder_path, exist_ok=True) 

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_path = os.path.join(folder_path, f"{timestamp}.txt")

with open(file_path, "w") as f:
    f.write("Hello World")

print(f"File created: {file_path}")
