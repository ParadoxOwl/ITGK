#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving9.ipynb">Øving 9</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Generelt%20om%20dictionary.ipynb">Generelt om dictionary</a></li>
#     <li ><a href="Innebygde%20funksjoner%20i%20dictionaries.ipynb">Innebygde funksjoner</a></li>
#     <li ><a href="Generelt%20om%20sets.ipynb">Generelt om sets</a></li>
#     <li ><a href="Generelt%20om%20filbehandling.ipynb">Generelt om filbehandling</a></li>
#     <li ><a href="Osteviruset.ipynb">Osteviruset</a></li>
#     <li ><a href="Bursdagsdatabasen.ipynb">Bursdagsdatabasen</a></li>
#     <li ><a href="Tallak%20teller%20antall%20tall.ipynb">Tallak teller antall tall</a></li>
#     <li class="active"><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#         <li ><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li ><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Opptaksgrenser
# 
# **Læringsmål:**
# 
# * Lese fra filer
# * dictionaries
# 
# **Starting Out with Python:**
# 
# * Kap. 6: Files and Exceptions
# * Kap. 9.1 Dictionaries
# 
# I denne oppgaven skal vi lese inn en fil med opptaksgrensene fra Samordna Opptak.
# 
# Filen er på CSV-format (Comma Separated Values), noe som betyr at hver linje er en liste med felter separert med komma. Tekstfelter er omsluttet av fnutter (").
# 
# * Første felt er studiets navn
# * Andre felt er poenggrensen (enten et tall, eller "Alle" dersom alle kom inn)
# 
# F.eks. linjen: **"NTNU 194459 Antikkens kultur","Alle"** sier at alle som søkte kom inn på Dragvoll-studiet “Antikkens kultur” ved NTNU.
# 
# Hver funksjon i de følgende deloppgavene tar data fra filen **poenggrenser_2011.csv** som input. Derfor er det veldig praktisk å lagre innholdet i en variabel, slik at du slipper å lese den på nytt hver gang.

# ### a)

# Les fra fila `poenggrenser_2011.csv` og lagre innholdet i en variabel.
# 
# ***Skriv koden din i boksen under.***

# In[1]:


f = open( 'poenggrenser_2011.csv', 'r' )
poitnts = f.read()


# ### b)

# Skriv en funksjon som finner ut hvor mange studier som tok inn alle søkere. 
# 
# ***Husk at du nå i alle deloppgavene kan bruke variabelen du definerte i a så lenge du har kjørt den kodesnutten først!***
# 
# *Eksempel på kjøring av kode:*
# ```python
# Antall studier hvor alle kom inn: 590
# ```
# ***Skriv koden din i boksen under.***

# In[2]:


def genereate_list( csv ):
    f = open( csv, 'r' )
    lst = f.read().split( '\n' )
    d = {}
    for i in lst:
        tmp = str(i).split(',')
        if len(tmp) != 2:
            continue
        tmp[0] = tmp[0].strip( '"' )
        tmp[1] = tmp[1].strip( '"' )
        d[tmp[0]] = tmp[1]
    return d


def all_in( d ):
    res = 0
    for k, v in d.items():
        if v == 'Alle':
            res += 1
    return res


points = genereate_list( 'poenggrenser_2011.csv' )
print( all_in( points ) )


# ### b)

# Skriv en funksjon som finner gjennomsnittlig opptaksgrense for NTNU. Ikke ta med studier som tok inn alle søkere.
# 
# *Eksempel på kjøring av kode:*
# ```python
# Gjennomsnittlig opptaksgrense for NTNU var: 46.29
# ```
# ***Skriv koden din i boksen under.***

# In[ ]:


def average_ntnu( d ):
    tot = 0
    n = 0
    for k, v in d.items():
        tmp = k.split(' ')
        if tmp[0] == 'NTNU' and v != 'Alle':
            tot += float( v )
            n += 1
    return f'{tot/n:.2f}'


print( f'Gjennomsnittlig opptaksgrense for NTNU var : {average_ntnu( points )}' )


# #### Hint

# For å sjekke om studiet var på NTNU kan du hente ut de fire første bokstavene i hver linje. Hvis du har en string studie kan du gjøre dette ved å skrive: studie[1:5]

# ### c)

# Skriv en funksjon som finner studiet med laveste opptaksgrense (som IKKE tok inn alle søkere).
# 
# *Eksempel på kjøring av kode:*
# ```python
# Studiet som hadde den laveste opptaksgrensen var: AHO 189343 Industridesign
# ```
# ***Skriv koden din i boksen under.***

# In[3]:


def lowest_stud( d ):
    stud = 0
    pnt = 100
    for k, v in d.items():
        tmp = k.split(' ')
        if v != 'Alle' and float( v ) < pnt:
            stud = k
            pnt = float( v )
    return stud


print( f'Studiet som hadde den laveste opptalsgrensen var: {lowest_stud( points )}')


# ### d)

# Lag en dictionary som har studiestedet som nøkkel og en liste med dictionaries som verdi. Denne listen med dictionaries skal ha navnet på linjen som nøkkel og opptakspoengene til den tilsvarende linjen som verdi. Dersom en linje har navnet "Fysikk og Matematikk" trenger du kun å ta hensyn til det første ordet, dvs. "Fysikk". 
# 
# **Eksempel på utskrift:**
# 
# ```python
# ATH [{'Kristendom': ' Alle'}, {'Interkulturell': ' Alle'}, {'Musikk': ' Alle'}, {'Teologi': ' Alle'}, {'Kristendom': ' Alle'}, {'Psykologi': ' Alle'}, {'Musikk': ' Alle'}, {'Interkulturell': ' Alle'}, {'Psykologi': ' Alle'}, {'Praktisk': ' Alle'}]
# AHO [{'Arkitekt': '12.3'}, {'Industridesign': '11.7'}]
# BDH [{'Sykepleierutdanning': '45.5'}]
# MF [{'Kristendom/RLE': ' Alle'}, {'Samfunnsfag': ' Alle'}, {'Interkulturell': ' Alle'}, {'Teologi': ' Alle'}, {'Religion': ' Alle'}, {'Ungdom': ' Alle'}, {'Lektor-': ' Alle'}, {'Teologi': ' Alle'}]
# DHS [{'Sykepleierutdanning': '48.3'}, {'Vernepleierutdanning': '41.8'}, {'Sosialt': '49.1'}, {'Sosialt': '42.4'}, {'Ergoterapeututdanning': '32.6'}]
# DMMH [{'Førskolelærerutdanning': '36.3'}, {'Førskolelærer': '39.1'}, {'Førskolelærer': '44'}, {'Førskolelærer': '46.2'}, {'Førskolelærer': ' Alle'}]
# .
# .
# .
# UIT [{'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Ingeniør': ' Alle'}, {'Sykepleierutdanning': '43.8'}, {'Lærerutdanning': ' Alle'}, {'Lærerutdanning': ' Alle'}, {'Førskolelærerutdanning': ' Alle'}, ....
# ```
# ***Skriv koden din i boksen under.***

# In[7]:


def uni_dict( d ):
    current_uni, studies, res = '', [], {}
    for k, v in d.items():
        tmp = k.split(' ')
        if current_uni == '':
            current_uni = tmp[0]
        if tmp[0] != current_uni:
            res[current_uni] = studies
            studies.clear()
            current_uni = tmp[0]
        foo = {}
        foo[tmp[2]] = v
        studies.append( foo )
    res[current_uni] = studies
    return res



for k, v in uni_dict(points).items():
    print(k,v)
    print()

