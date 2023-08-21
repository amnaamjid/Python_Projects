#Python 1st project
#category: Basic
#Project Name: My personal diary App

import os
from datetime import datetime

# Create a folder to store diary entries
if not os.path.exists('entries'):
    os.mkdir('entries')

def write_entry():
    date = datetime.now().strftime('%Y-%m-%d')
    entry = input("Write your diary entry: ")
    
    with open(f'entries/{date}.txt', 'w') as file:
        file.write(entry)
    
    print("Entry saved successfully!")

def view_entries():
    entry_files = os.listdir('entries')
    
    if not entry_files:
        print("No entries found.")
        return
    
    print("Available entries:")
    for i, entry_file in enumerate(entry_files, start=1):
        print(f"{i}. {entry_file[:-4]}")  # Remove '.txt' extension
    
    choice = input("Enter the number of the entry you want to view: ")
    
    try:
        choice = int(choice)
        selected_entry = entry_files[choice - 1]
        
        with open(f'entries/{selected_entry}', 'r') as file:
            entry = file.read()
            print(f"\n{entry}\n")
    except (ValueError, IndexError):
        print("Invalid choice.")

def main():
    while True:
        print("\n=== Personal Diary App ===")
        print("1. Write an entry")
        print("2. View entries")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            write_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()

