#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import shutil

def organize_files(source_dir, destination_dir):
    # Create destination directories if they don't exist
    for folder_name in ["Images", "Documents", "Videos", "Audios", "Others"]:
        folder_path = os.path.join(destination_dir, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Define file extensions for each category
    file_extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".doc", ".docx", ".pdf", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
        "Audios": [".mp3", ".wav", ".flac", ".aac"],
    }

    # Organize files by moving them to appropriate folders
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        if os.path.isfile(source_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for category, extensions in file_extensions.items():
                if file_extension in extensions:
                    destination_path = os.path.join(destination_dir, category, filename)
                    shutil.move(source_path, destination_path)
                    print(f"Moved {filename} to {category} folder.")
                    moved = True
                    break
            if not moved:
                destination_path = os.path.join(destination_dir, "Others", filename)
                shutil.move(source_path, destination_path)
                print(f"Moved {filename} to Others folder.")

# Example usage
if __name__ == "__main__":
    source_directory = r"C:\Users\Kemins\Pictures"
    destination_directory = r"C:\Users\Kemins\Pictures\Screenshots"
    organize_files(source_directory, destination_directory)


# In[ ]:




