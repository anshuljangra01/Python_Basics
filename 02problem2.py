import os

# Specify the directory yoy want to list
# or
# Select the directory whose content you want to list
directory_path = '/'

# use the OS module to list the directory content
# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)