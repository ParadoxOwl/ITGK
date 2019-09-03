def rounding(num, des):
    n = str(num)
    zero = "0"
    for j in range(len(n)):
        zero += "0"
    for i in range(len(n)):
        if n[i] == ".":
            if int(des) >= 0:
                d = i + 1 + int(des)
                if int(n[d])< 5:
                    if int(des) == 0:
                        return n[:d-1]
                    else:
                        return n[:d]
                if int(n[d])>= 5:
                    if int(des) == 0:
                        foo = ""
                        if int(n[d-2])==9:
                            foo = rounding(num, int(des) -1)
                        else:
                            foo = n[:d-2]+ str(int(n[d-2])+1)
                        return foo
                        return n[:d-2] + str(int(n[d-2])+1)
                    if int(des) > 0:
                        foo = ""
                        if int(n[d-1])==9:
                            for k in range(1+d):
                                if d-k == i:
                                    continue
                                if int(n[d-k])==9:
                                    foo = rounding(num, int(des) -1)
                        else:
                            foo = n[:d-1]+ str(int(n[d-1])+1)
                        return foo
            if int(des) < 0:
                d = i + int(des)
                if int(n[d])<5:
                    return n[:d]+zero[:abs(int(des))]
                if int(n[d])>=5:
                    foo = ""
                    if int(n[d-1])==9 and d != 1:
                        foo = rounding(num, int(des)-1)
                    else:
                        foo = n[:d-1]+ str(int(n[d-1])+1) + zero[:abs(int(des))]
                    return foo
        else:
            continue
    if int(des) < 0:
        d = len(n) + int(des)
        zero = "0"
        for j in range(len(n)):
            zero += "0"
        if int(n[d])<5:
            return n[:d]+zero[:len(n)+int(des)+1]
        if int(n[d])>=5:
            foo = ""
            if int(n[d-1])==9 and d != 1:
                foo = rounding(num, int(des)-1)
            else:
                foo = n[:d-1]+ str(int(n[d-1])+1) + zero[:abs(int(des))]
            return foo


numb = input("Gi inn et desimaltall: ")
deci = input("Antall desimaler i avrunding: ")
print("Avrundet til " + str(deci) + " desimaler: " + str(rounding(numb, deci)))
