import os
import shutil
import sys

# Define folder categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".java", ".cpp", ".html", ".css", ".js"]
}

def organize_folder(path):
    if not os.path.exists(path):
        print("❌ Folder not found!")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file)
        moved = False

        for folder, extensions in FILE_TYPES.items():
            if ext.lower() in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
                moved = True
                break

        if not moved:
            others_path = os.path.join(path, "Others")
            os.makedirs(others_path, exist_ok=True)
            shutil.move(file_path, os.path.join(others_path, file))

    print("✅ Files organized successfully!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_organizer.py <folder_path>")
    else:
        organize_folder(sys.argv[1])