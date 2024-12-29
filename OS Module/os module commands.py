import os 
folders = os.listdir("Data")

for folder in folders:
    print(folder)
    print(os.listdir(f"Data/{folder}"))


print(os.getcwd()) # returns Current Working Directory


os.chdir("/Users") # Changes Directory to given Argument

print(os.getcwd()) #  returns Current Working Directory
