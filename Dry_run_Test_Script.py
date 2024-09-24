import os
from datetime import datetime

# This is a dry run version of the backup script.
# It will show you what would happen without actually creating a backup.

# Step 1: Set up the folders we'll be working with
downloads_folder = os.path.expanduser('~/Downloads')
backup_directory = "D:\\Backups"

# Step 2: Create a name for our backup file
today_date = datetime.now().strftime('%Y%m%d')
zip_filename = os.path.join(backup_directory, f"downloads_backup_{today_date}.zip")

# Step 3: Simulate the backup process
print("=== Dry Run: Backup Simulation ===")
print(f"Source folder: {downloads_folder}")
print(f"Backup file (not actually created): {zip_filename}")
print("\nFiles that would be included in the backup:")

total_files = 0
total_size = 0

for foldername, subfolders, filenames in os.walk(downloads_folder):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        relative_path = os.path.relpath(file_path, downloads_folder)
        file_size = os.path.getsize(file_path)
        
        print(f"  - {relative_path} ({file_size} bytes)")
        
        total_files += 1
        total_size += file_size

# Step 4: Display summary
print("\n=== Backup Simulation Summary ===")
print(f"Total files that would be backed up: {total_files}")
print(f"Total size of backup: {total_size} bytes ({total_size / 1024 / 1024:.2f} MB)")
print(f"\nIf this looks correct, you can run the actual backup script.")

input("\nPress Enter to exit.")
