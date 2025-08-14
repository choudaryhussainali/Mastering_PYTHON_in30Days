"""
File Organizer Bot
------------------
A Python script that automatically organizes files in a specified folder.
It can sort files by type, creation date, or even rename them in a clean format.
"""

import os
import shutil
from datetime import datetime

def organize_by_type(folder_path):
    """Organizes files into subfolders based on their extension."""
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            ext = file_name.split('.')[-1].lower()
            folder_name = ext.upper() + "_Files"
            dest_folder = os.path.join(folder_path, folder_name)

            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, file_name))
            print(f"Moved {file_name} → {folder_name}")

def organize_by_date(folder_path):
    """Organizes files into subfolders based on creation month & year."""
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            creation_time = os.path.getctime(file_path)
            date_folder = datetime.fromtimestamp(creation_time).strftime("%Y-%m")
            dest_folder = os.path.join(folder_path, date_folder)

            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, file_name))
            print(f"Moved {file_name} → {date_folder}")

def main():
    folder_path = input("Enter folder path to organize: ").strip()

    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        return

    print("\n📂 Choose organization method:")
    print("1. By File Type")
    print("2. By Creation Date")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        organize_by_type(folder_path)
    elif choice == "2":
        organize_by_date(folder_path)
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
