import os
import shutil

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
    "Code": [".py", ".cpp", ".c", ".html", ".css", ".js"]
}


def get_category(file_name):
    extension = os.path.splitext(file_name)[1].lower()

    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category

    return "Others"


def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist!")
        return

    files = os.listdir(folder_path)
    moved_count = 0

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        category = get_category(file_name)
        destination_folder = os.path.join(folder_path, category)

        # Create category folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, file_name)

        # Avoid overwriting files
        if os.path.exists(destination_path):
            name, extension = os.path.splitext(file_name)
            counter = 1

            while os.path.exists(destination_path):
                new_name = f"{name}_{counter}{extension}"
                destination_path = os.path.join(destination_folder, new_name)
                counter += 1

        shutil.move(file_path, destination_path)
        moved_count += 1

        print(f"Moved: {file_name} -> {category}")

    print("\nOrganization completed!")
    print(f"Total files organized: {moved_count}")


# Main program
print("===== SMART FILE ORGANIZER =====")

folder_path = input("Enter the folder path you want to organize: ").strip()

organize_files(folder_path)