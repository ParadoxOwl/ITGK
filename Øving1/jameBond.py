def bondify(name):
    subNames = name.split(" ")
    bond= "The name is " + subNames[-1] + ", " + name
    return bond

nome=input("Navn: ")
print(bondify(nome))
