import os

# os.rename(f"OOPs Concept/ClutteredFolder/Pb.py",f"OOPs Concept/ClutteredFolder/PhoneBook.py")

files = os.listdir("OOPs Concept/ClutteredFolder")

i=1
for file in files:
    if file.endswith(".png"):
        os.rename(f"OOPs Concept/ClutteredFolder/{file}",f"OOPs Concept/ClutteredFolder/{i}.png")
        i=i+1

print(files)
