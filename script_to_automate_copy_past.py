import os
import shutil

def copy_latest_file(source_folder, destination_folder):
    # Ensure source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return
    
    # Get all files in the source directory
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    if not files:
        print("No files found in source folder.")
        return
    
    # Get the latest file based on modification time
    latest_file = max(files, key=lambda f: os.path.getmtime(os.path.join(source_folder, f)))
    source_file_path = os.path.join(source_folder, latest_file)
    destination_file_path = os.path.join(destination_folder, latest_file)

    # Ensure destination folder exists, create if not
    os.makedirs(destination_folder, exist_ok=True)

    # Copy the latest file
    shutil.copy2(source_file_path, destination_file_path)
    
    print(f"Copied latest file: {latest_file} to {destination_folder}")

# Define source and destination (Dynamic values)
source_path = r"\\server\Planning\PBI_PLM_RAW_DATA_EXPORT"
destination_path = r"C:\Users\tswarnkar\PBI_PLM_RAW_DATA_EXPORT"

# Run the function
copy_latest_file(source_path, destination_path)
