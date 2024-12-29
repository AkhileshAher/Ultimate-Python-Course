import os

if(not os.path.exists("Data")):
    os.mkdir("Data")

for i in range(0,15):
    os.mkdir(f"Data/Day{i+1}")
