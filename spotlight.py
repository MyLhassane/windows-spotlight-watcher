import os
from pathlib import Path
import shutil
from datetime import datetime

# Get the list of files in the updated folder
updated_folder = Path.home().joinpath('AppData', 'Local', 'Packages',
                                      'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy', 'LocalState', 'Assets')
updated_files = os.listdir(updated_folder)

counter = 1
# Create a new folder for each updated file named by the date of modification
for file_name in updated_files:
    file_path = os.path.join(updated_folder, file_name)
    mod_time = os.path.getmtime(file_path)
    mod_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
    # Create a new folder name using the date of modification
    new_folder_name = f'{mod_date}'
    new_folder_path = Path.home().joinpath('Pictures', 'spotlight', new_folder_name)
    # Create a new folder for the updated file if it does not exist already
    os.makedirs(new_folder_path, exist_ok=True)
    # Add .jpg extension to the file name
    new_file_name = f'{mod_date}_{str(counter).zfill(2)}.jpg'
    counter += 1
    new_file_path = os.path.join(new_folder_path, new_file_name)
    # Copy the updated file to the new folder with the new file name
    shutil.copy(file_path, new_file_path)
