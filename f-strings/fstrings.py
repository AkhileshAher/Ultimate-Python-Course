letter="Hey My name is {1} and I am from {0}"
country="India"
name="Akhilesh"

print(letter.format(country,name))

print(f"Hey my name is {name} and i am from {country}")

print(f"We use f-strings like this: Hey my name is {{name}} and I am From {{country}}")

price=49.099999
txt=f"For only {price:.2f} Dollars !!!"
print(txt)

# print(txt.format())
print(type(f"{2*30}"))
