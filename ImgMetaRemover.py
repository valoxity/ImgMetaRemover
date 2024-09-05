from PIL import Image
import os
import glob
import time

print("""
A product of ValoXity
      
Our website (https://valoxity.com/)
""")
time.sleep(15)


# Specify the folder name you want to create
folder = 'withoutmeta'

# Get the current directory
current_directory = os.getcwd()

# Combine the current directory with the folder name
folder_path = os.path.join(current_directory, folder)

# Check if the folder already exists
if not os.path.exists(folder_path):
    # If the folder doesn't exist, create it
    os.makedirs(folder_path)
    print(f"Folder '{folder}' created successfully.")
else:
    print(f"Folder '{folder}' already exists.")
# Get the current directory
current_directory = os.getcwd()
outpuy = os.path.join(current_directory, folder)
# Define the file extensions to search for
file_extensions = ['png', 'jpeg', 'jpg']

# Create a list to store file names with the specified extensions
image_files = []

# Iterate through the files in the directory
for extension in file_extensions: 
    image_files.extend(glob.glob(os.path.join(current_directory, f'*.{extension}')))

# Extract and print the file names without paths
for file_path in image_files:
    file_name = os.path.basename(file_path) 
    image = Image.open(file_name)
    image = image.copy()
    image.save(outpuy+"/"+file_name, quality=95)
    print("("+file_name+") Successfully removed image metadata :)")
print("\n")
print("\n")
print("-------------------------------------------------------------------")
print("Please don't forget to visit our website (https://valoxity.com/) :)")
print("-------------------------------------------------------------------")
print("\n")
print("\n")
time.sleep(15)



