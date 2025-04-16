import os
import zipfile

# Path to the folder containing the 56 zip files and output directory
zips_dir = '/Volumes/MIREIA/MTHESIS - DEEPLESION/DATA/Images_zip'
output_dir = '/Volumes/MIREIA/MTHESIS - DEEPLESION/DATA/Images_png'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# List all zip files in the directory (ignore ._ files, metadata from MAC)
zip_files = [f for f in os.listdir(zips_dir) if f.endswith('.zip') and not f.startswith('._')]
print(f"Found {len(zip_files)} zip files.")

for zip_file in zip_files:
    zip_path = os.path.join(zips_dir, zip_file)
    print(f"Extracting: {zip_file}")
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            # skip MAC metadata files and folders (will be created when saving files)
            if member.startswith('._') or member.endswith('/'):
                continue

            member_path = member.replace('\\', '/')  # normalize for safety
            full_output_path = os.path.join(output_dir, member_path)
            os.makedirs(os.path.dirname(full_output_path), exist_ok=True)

            with zip_ref.open(member) as source, open(full_output_path, "wb") as target:
                target.write(source.read())

print("Extraction complete!")
