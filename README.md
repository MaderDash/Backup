# Weekly Backup Script for Downloads Folder

This project contains a Python script that creates a weekly backup of your Downloads folder. Follow the instructions below to set up the automated backup using Windows Task Scheduler.

## Prerequisites

- Windows 10 or later
- Python 3.x installed
- The backup script (`Backup.py`) located in a known directory

## Setting Up the Scheduled Task

1. **Open Task Scheduler**
   - Press `Windows key + R` to open the Run dialog
   - Type `taskschd.msc` and press Enter

2. **Create a New Task**
   - In the Task Scheduler, click on "Create Basic Task" in the right-hand Actions panel
   - Name: "Weekly Backup of Downloads Folder"
   - Description: "Runs a Python script to backup the Downloads folder every week"

3. **Set the Trigger**
   - Click "Next" and select "Weekly"
   - Choose your preferred start date and time
   - Set "Recur every 1 week" and select the day of the week
   - Click "Next"

4. **Configure the Action**
   - Select "Start a program" and click "Next"
   - Program/script: Enter the path to your Python executable (e.g., `C:\Python39\python.exe`)
   - Add arguments: Enter the full path to your backup script (e.g., `C:\Scripts\Backup.py`)
   - Click "Next"

5. **Review and Finish**
   - Review your settings and click "Finish"

## Testing the Task

1. Locate your newly created task in the Task Scheduler library
2. Right-click on the task and select "Run"
3. Check that the backup file is created in your specified backup directory

## Dry Run

Before setting up the scheduled task, you can use the `Dry_run_Test_Script.py` to simulate the backup process:

1. Open a command prompt
2. Navigate to the directory containing `Dry_run_Test_Script.py`
3. Run the script: `python Dry_run_Test_Script.py`
4. Review the output to ensure it covers the expected files and directories

## Troubleshooting

- Ensure that Python is in your system's PATH
- Check that the paths to Python and the script are correct in the task settings
- Verify that the user account running the task has necessary permissions

For any issues, please check the Windows Event Viewer for task-related errors.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.