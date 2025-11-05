import os
import shutil
from zipfile import ZipFile

# create destination folder -> move -> unpack

if __name__ == "__main__":
# --------------------------------------- DEFINE DIRECTORIES --------------------------------------- #

    source_directory = os.environ.get("TAKEOUT_FOLDER")
    destination_directory = os.environ.get("PHOTOS_FOLDER")

# -------------------------------------------- GET FILES -------------------------------------------- #

    files = os.listdir(source_directory)

    # filter so code only gets zip files
    zip_files = [file for file in files if os.path.splitext(file)[1] == ".zip"]

# ----------------------------------- DESTINATION FOLDER CREATION ----------------------------------- #
    # make destination folder for each zip files
    for file in zip_files:
        filename = os.path.splitext(file)[0]
        file_num = filename.split("-")[-1]

        destination_path = os.path.join(destination_directory, f"Takeout_{file_num}")

        if os.path.exists(destination_path):
            print(f"{destination_path} already exists, skipping.")
        else:
            folder_name = os.path.basename(destination_path)
            print(f"{folder_name} folder created.")

# -------------------------------------------- MOVE FILES -------------------------------------------- #
    # create paths for file source and destination
    source_files = [*map(lambda x: os.path.join(source_directory, x), zip_files)]
    destination_files = [*map(lambda x: os.path.join(destination_directory,
                                                     f"Takeout_{os.path.splitext(x)[0].split("-")[-1]}",
                                                     x),
                                        zip_files)]

    for source_file, destination_file in zip(source_files, destination_files):
        if os.path.exists(source_file):
            print(f"Success: {source_file} exists and will be moved to {destination_file}.")
            shutil.move(source_file, destination_file)
        else:
            print("Skipped: Source file does not exist.")

# ----------------------------------------- UNPACK ZIP FILES ----------------------------------------- #

# os.walk returns root, dirs, files
destination_root_dir_files = list(os.walk(destination_directory))
for root, dirs, files in destination_root_dir_files:
    for file in files:
        if file.endswith(".zip"):
            zip_file_path = os.path.join(root, file)
            print(f"Zip file path: {zip_file_path}")

            # only run once so comment out once done unpacking
            # with ZipFile(zip_file_path, 'r') as zip_file:
            #     # extract to the same root/dir
            #     zip_file.extractall(root)

# ----------------------------------------- DELETE ZIP FILES ----------------------------------------- #

            os.remove(zip_file_path)
            print(f'Done unpacking, now removing: {zip_file_path}')
            print('-------')

