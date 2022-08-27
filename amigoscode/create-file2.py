import os.path

file_name = "data.csv"

if os.path.isfile(file_name):
    with open(file_name, "r") as file:
        print(file.read())
else:
    print(f"file {file_name} does not exist")