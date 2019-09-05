#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving1.ipynb">Øving 1</a>
#     </div>
#     <ul class="nav navbar-nav">
#         <li><a href="Intro%20til%20jupyter.ipynb">Intro til Jupyter</a></li>
#       <li ><a href="Jeg%20elsker%20ITGK!.ipynb">Jeg elsker ITGK!</a></li>
#     <li ><a href="Kalkulasjoner.ipynb">Kalkulasjoner</a></li>
#     <li><a href="Input%20og%20variable.ipynb">Input og variable</a></li>
#     <li><a href="Tallkonvertering.ipynb">Tallkonvertering</a></li>
#     <li ><a href="Peppes%20Pizza.ipynb">Peppes Pizza</a></li>
#     <li ><a href="Geometri.ipynb">Geometri</a></li>
#     <li ><a href="Vitenskapelig%20notasjon.ipynb">Vitenskapelig notasjon</a></li>
#     <li ><a href="Tetraeder.ipynb">Tetraeder</a></li>
#     <li ><a href="Bakekurs.ipynb">Bakekurs</a></li>
#     <li class="active"><a href="James%20Bond%20and%20Operation%20round().ipynb">James Bond and Operation Round</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # James Bond and Operation round()
# 
# **Læringsmål:**
# 
# * Bruk av heltallsdivisjon og modulo, konvertering av data
# 
# * Avrunding
# * (særlig c) Oppdeling / håndtering av strenger
# 
# **Starting Out with Python:**
# 
# * Kap. 2.3
# 
# * Kap. 3.1
# 
# * Kap. 4.2
# 
# * Kap. 8.2

# ## a) Kjøpmannsavrunding

# "Kjøpmannsavrunding" innebærer at man alltid runder opp når et tall er midt mellom to runde tall. F.eks. at 2.5 rundes til 3 og 3.5 til 4 hvis vi skal ha hele tall, og 2.25 likeledes rundes til 2.3 hvis vi skal ha en desimal. Som forklart i tutorial i oppgaven Tallkonvertering (tidligere i denne samme øvingen) bruker Pythons funksjon `round()` **ikke** kjøpmannsavrunding, men runder i stedet i partallsretning i situasjoner hvor tallet er midt mellom to alternativer. Dvs., 2.5 vil da rundes ned til 2 fordi 2 er partall, mens 3.5 rundes opp til 4. Det er fornuftige grunner til dette (unngå systematiske feil som man får hvis man alltid runder opp). I noen situasjoner - f.eks. hvis man er kjøpmann - kan det imidlertid være at man faktisk ønsker kjøpmannsavrunding.
# 
# Oppgaven din her er å lage et program som får til kjøpmannsavrunding. Det skal be bruker om å skrive inn et desimaltall, samt ønsket antall desimaler det skal avrundes til - og så foreta denne avrundingen. Dette må da gjøres på annet vis enn å bruke Pythons `round()`-funksjon, siden du f.eks. skal runde 2.5 til 3 (hvis null desimaler) og 2.25 til 2.3 (hvis en desimal) mens `round()` ville runde nedover her. Et par eksempler på kjøring:
# 
#   
# ```python
# Gi inn et desimaltall: 2.5  
# Antall desimaler i avrunding: 0  
# Avrundet til 0 desimaler: 3
# ```
#   
# ```python
# Gi inn et desimaltall: 2.25  
# Antall desimaler i avrunding: 1  
# Avrundet til 1 desimal: 2.3
#     ```
#   
# ```python
# Gi inn et desimaltall: 2500.0  
# Antall desimaler i avrunding: -3  
# Avrundet til -3 desimaler: 3000  
# ```
# 
# Som eksemplet viser skal det også være mulig å gi inn negativt antall desimaler for å få grovere avrunding enn nærmeste heltall. Også da med kjøpmannsavrunding (dvs. 2500 blir 3000, ikke 2000).
# 
# ***Skriv koden din i blokka under.***

# In[1]:


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


# ## b) Avrunding som unngår unøyaktig tallrepresentasjon

# ## Selv hvis vi er fornøyde med IEEE-standarden for avrunding (heller enn kjøpmannsavrunding), kan `round()` av og til gi overraskende resultater. F.eks.
# 
# * `round(2.50000000000000000001)` gir 2, selv om tallet er litt nærmere 3
# * `round(2.15, 1)` gir 2.1, selv om regelen om å gå mot partall skulle tilsi 2.2
# 
# Begge disse og andre lignende tilfeller skyldes egentlig ikke noen feil ved `round()`-funksjonen, men problemer med selve representasjonen av tall i det binære systemet.
# 
# 2.50000000000000000001 lar seg ikke representere eksakt i maskinen, så den tar det nærmeste den får til, som her blir 2.5 - og dermed vipper `round()` ned.
# 
# 2.15 lar seg heller ikke representere eksakt (i det binære tallsystemet, selv om det kun trengs tre siffer i titallssystemet), det nærmeste maskinen får til er 2.14999999999999999999. Dermed ligger tallet ikke lenger midt imellom men litt nærmere 2.1, så avrunding vipper ned.
# 
# Oppgaven her er å lage et program som klarer å avrunde korrekt selv med slike tall som dette. For å klare oss mest mulig med det som er undervist av pensum hittil, kan heltallsdelen og desimaldelen til tallet vi skal behandle, leses inn hver for seg. Eksempel på kjøring blir da:
# 
#   
# ```
# Oppgi heltallsdelen av tallet (det foran punktum): 2
# Oppgi desimaldelen av tallet (det bak punktum): 5
# Oppgi ønsket antall desimaler i avrunding: 0
# 2.5 avrundet til 0 desimaler blir 2
# 
# Oppgi heltallsdelen av tallet (det foran punktum): 2
# Oppgi desimaldelen av tallet (det bak punktum): 15
# Oppgi ønsket antall desimaler i avrunding: 1
# 2.15 avrundet til 1 desimal blir 2.2
# 
# Oppgi heltallsdelen av tallet (det foran punktum): 2
# Oppgi desimaldelen av tallet (det bak punktum): 500000000000000000001
# Oppgi ønsket antall desimaler i avrunding: 0
# 2.500000000000000000001 avrundet til 0 desimaler blir 3
# ```
# 
# Denne oppgaven går delvis utenfor det som undervist hittil i emnet.
# 
# ***Skriv koden din i blokka under.***

# In[1]:


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


# ## c) Strenghåndtering

# Lag et program hvor brukeren skriver inn navnet sitt fra tastaturet etter ledeteksten "Jeg heter:", og la maskinen svare med setningen The name is... som vist i boksen under.
# 
#   
# ```
# Jeg heter: James Bond
# The name is Bond, James Bond
# ```
# 
# Her vil du mest sannsynlig måtte benytte deg av programmeringsmekanismer som ikke er forelest ennå, enten if-setninger, løkker og strengindeksering, eller strengmetoder som `split()` med tilhørende listebehandling. Hvis du vil gjøre det ekstra vanskelig for deg selv (**VALGFRITT**, ikke nødvendig for å få godkjent), prøv å lage et program som også funker for personer med flere enn to navn (f.eks. The name is Hopper, Grace Murray Hopper), men som tar hensyn til at preposisjoner som Von, Van, De, Di er del av etternavnet (f.eks. The name is Von Neumann, John Von Neumann; The name is De Morgan, Augustus De Morgan... dog likevel bare hvis dette kommer i midten, det må fortsatt bli The name is Morrison, Van Morrison). Dessuten, hvis et navn slutter med Jr, Sr eller romertall, er det ikke det siste ordet som er etternavnet men det nest siste: The name is Northug, Petter Northug Jr; The name is Huxtable, Henry Huxtable III.
# 
# ***Skriv koden din i blokka under.***

# In[ ]:


def bondify(name):
    subNames = name.split(" ")
    bond= "The name is " + subNames[-1] + ", " + name
    return bond

nome=input("Jeg heter: ")
print(bondify(nome))

