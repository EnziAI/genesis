import os
import time
import subprocess

# Specify the folder path to monitor for file changes
folder_path = "./C1_MIT"

# Specify the bash script to run when changes are detected
bash_script = "./p"

# Dictionary to store file timestamps
file_timestamps = {}

# Function to check if a file has been modified
def is_file_modified(file_path):
    current_timestamp = os.path.getmtime(file_path)
    previous_timestamp = file_timestamps.get(file_path, None)
    file_timestamps[file_path] = current_timestamp
    return current_timestamp != previous_timestamp

# Main loop to monitor the folder for changes
while True:
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if is_file_modified(file_path):
                print(f"Detected change in file: {file_path}")
                subprocess.run(["bash", bash_script])
    # Sleep for a specified interval before checking again
    time.sleep(5)  # Adjust this interval as needed
