info={'name':'Karan','age':29,'eligible':True}
print(info)

print(info.keys())
print(info.values())

for key in info.keys():
    print(f"The values corresponding to {key} is {info[key]}")


print(info.items())

for key,value in info.items():
    print(f"The values corresponding to {key} is {info[key]}")


dict1={
    "Harry":"Human Being","Akhilesh":"Brave","Sahil":"Batman"
    }

#print(dict1["Om"]) #Throws Error if not available in Dictionary

print(dict1.get("Om"))
