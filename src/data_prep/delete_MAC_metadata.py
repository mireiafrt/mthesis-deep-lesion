import os

def delete_dot_underscore_files(folder_path):
    count = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith("._"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                count += 1
    print(f"\n✅ Done! Deleted {count} ._ files.")

# 🔧 Replace this with your folder path
folder_to_clean = "/Volumes/MIREIA/MTHESIS - DEEPLESION/DATA/Key_slices"
delete_dot_underscore_files(folder_to_clean)
