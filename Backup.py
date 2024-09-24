import os
import zipfile
from datetime import datetime

# Hello! This script will create a backup of your Downloads folder.
# It will zip all the files and save them with today's date.

# Step 1: Set up the folders we'll be working with

# This is where we'll look for files to backup (your Downloads folder)
downloads_folder = os.path.expanduser('~/Downloads')

# This is where we'll save the backup zip file
# You can change this to any folder you like
backup_directory = "D:\\Backups"

# Step 2: Create a name for our backup file
# It will look like "downloads_backup_20240101.zip" (for January 1, 2024)
today_date = datetime.now().strftime('%Y%m%d')
zip_filename = os.path.join(backup_directory, f"downloads_backup_{today_date}.zip")

# Step 3: Start the backup process
print(f"Starting backup of {downloads_folder}")
print(f"Backup will be saved to {zip_filename}")

# Create a zip file and add all the files from the Downloads folder
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    # Walk through all folders and files in the Downloads folder
    for foldername, subfolders, filenames in os.walk(downloads_folder):
        for filename in filenames:
            # Get the full path of each file
            file_path = os.path.join(foldername, filename)
            # Add the file to the zip, preserving the folder structure
            zipf.write(file_path, os.path.relpath(file_path, downloads_folder))
            print(f"Added {filename} to the backup")

# Step 4: Finish up
print(f"\nBackup complete!")
print(f"All files from {downloads_folder} have been zipped into {zip_filename}")

# Wait for user input before closing
input("Press Enter to exit.")
