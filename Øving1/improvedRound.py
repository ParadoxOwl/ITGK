def roundim(numb, deci, val):
    numb=round(numb,val)
    deciNew = round(deci, val -len(str(deci)))
    test = 5
    while True:
        if test*10>deci:
            break
        test = test*10
    if len(str(deciNew)) > len(str(deci)):
        if numb % 2 != 0 or deci>test:
            numb += 1
        if val > 0:
            deci = int(str(deciNew)[0:val+1])
            return str(numb) + "." + str(deci)
        else:
            deci = 0
            return str(numb) + "." + str(deci)
    if val > 0:
        deci = int(str(deciNew)[:val])
        return str(numb) + "." + str(deci)
    else:
        deci = 0
        return str(numb) + "." + str(deci)

num=int(input("Oppgi heltallsdelen av tallet: "))
dec=int(input("Oppgi desimaldelen av tallet: "))
valu=int(input("Oppgi ønsket antall desimaler i avrunding: "))
print(roundim(num,dec,valu))
