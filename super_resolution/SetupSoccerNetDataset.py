import os
import sys
import zipfile
import glob
from tqdm import tqdm

# Debug prints to verify current working directory and its contents
print("Current working directory:", os.getcwd())
print("Contents of current working directory:", os.listdir(os.getcwd()))

# Adjust the path below to the folder that contains the SoccerNet module.
# For example, if the SoccerNet folder is inside "super_resolution", use:
# sys.path.append(os.path.join(os.getcwd(), "super_resolution", "SoccerNet"))
# If it's in the project root, use:
sys.path.append(os.path.join(os.getcwd(), "SoccerNet"))
print("Updated sys.path:", sys.path)

try:
    from SoccerNet.Downloader import SoccerNetDownloader as SNdl
    print("Successfully imported SoccerNet.Downloader")
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)
    # If this error occurs, you need to adjust the sys.path.append() above
    # to point to the correct location of the SoccerNet module.
    raise

def unzip_with_progress(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
        total_files = len(file_list)

        if total_files == 0:
            print(f"⚠️ {zip_path} is empty, skip it...")
            return
        for file in tqdm(file_list, desc=f"Extracting {os.path.basename(zip_path)}", unit="file"):
            zip_ref.extract(file, extract_to)

def batch_unzip(directory):
    zip_files = glob.glob(os.path.join(directory, "*.zip"))  # Get all ZIP files in the directory
    if not zip_files:
        print("❌ No zip files found")
        return

    print(f"📂 In {directory}, found {len(zip_files)} zip files, unzipping now...\n")
    for zip_file in zip_files:
        extract_folder = directory
        os.makedirs(extract_folder, exist_ok=True)
        unzip_with_progress(zip_file, extract_folder)
    print("\n✅ All files unzipped!")

root_dir = os.getcwd()
mySNdl = SNdl(LocalDirectory="data")
mySNdl.downloadDataTask(task="jersey-2023", split=["train", "test", "challenge"])

dataset_path = os.path.join(root_dir, 'data/jersey-2023')
if os.path.exists(dataset_path):
    dataset_path_old = dataset_path
    dataset_path = os.path.join(root_dir, 'data/SoccerNet')
    os.rename(dataset_path_old, dataset_path)
    print(f'Renamed {dataset_path_old} to {dataset_path}')

    # Unzip dataset
    batch_unzip(dataset_path)
