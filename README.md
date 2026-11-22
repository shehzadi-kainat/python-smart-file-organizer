Smart File Organizer 📁

A Python automation tool that organizes files into folders based on their file extensions. It helps keep directories clean and makes file management easier by automatically sorting files into categories.

Features

- Automatically categorizes files by extension.
- Organizes images, documents, videos, audio, archives, and code files.
- Creates destination folders automatically.
- Moves files into their appropriate folders.
- Prevents overwriting files with the same name.
- Skips existing directories.
- Places unrecognized file types into an "Others" folder.

File Categories

Category| File Extensions
Images| ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"
Documents| ".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"
Videos| ".mp4", ".mkv", ".mov", ".avi"
Audio| ".mp3", ".wav", ".aac", ".flac"
Archives| ".zip", ".rar", ".7z", ".tar"
Code| ".py", ".cpp", ".c", ".html", ".css", ".js"
Others| Unrecognized file extensions

Technologies Used

- Python
- "os" module
- "shutil" module

How It Works

1. The user enters the path of the folder they want to organize.
2. The program checks whether the folder exists.
3. It identifies each file by its extension.
4. It creates category folders if they don't already exist.
5. It moves files into their respective folders.
6. It avoids overwriting files with the same name.

How to Run

1. Clone this repository:
   
   git clone https://github.com/YOUR-USERNAME/python-smart-file-organizer.git

2. Navigate to the project directory:
   
   cd python-smart-file-organizer

3. Run the program:
   
   python main.py

4. Enter the folder path you want to organize when prompted.

Example

Before organizing:

MyFiles/
├── photo.jpg
├── notes.pdf
├── song.mp3
└── video.mp4

After organizing:

MyFiles/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── notes.pdf
├── Audio/
│   └── song.mp3
└── Videos/
    └── video.mp4

Learning Objectives

This project helped me practice:

- Python functions
- Loops and conditional statements
- File handling
- Directory management
- Exception handling concepts
- Basic automation
- Working with Python modules

Disclaimer

Test the program on a sample folder before using it on important files. This program moves files from their original locations.
