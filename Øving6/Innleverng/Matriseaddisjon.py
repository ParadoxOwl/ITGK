#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving6.ipynb">Øving 6</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Generelt%20om%20lister.ipynb">Generelt om lister</a></li>
#     <li ><a href="Lett%20og%20blandet.ipynb">Lett og blandet</a></li>
#     <li ><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li ><a href="Vektorer.ipynb">Vektorer</a></li>
#     <li ><a href="Lister%20og%20lokker.ipynb">Lister og løkker</a></li>
#     <li ><a href="Teoridelen%20paa%20eksamen.ipynb">Teoridelen på eksamen</a></li>
#     <li ><a href="Gangetabell%20og%20lister.ipynb">Gangetabell og lister</a></li>
#     <li ><a href="Lotto.ipynb">Lotto</a></li>
#     <li ><a href="Tannfeen.ipynb">Tannfeen</a></li>
#         <li ><a href="Chattebot.ipynb">Chattebot</a></li>
#     <li class="active"><a href="Matriseaddisjon.ipynb">Matriseaddisjon</a></li>
#     <li ><a href="Intro%20til%20numpy-arrays.ipynb">Intro til numpy-arrays</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Matriseaddisjon
# 
# **Læringsmål:**
# 
# * Lister av flere dimensjoner
# 
# **Starting Out with Python:**
# 
# * Kap. 7.8
# 
# I denne oppgaven skal du implementere noen funksjoner slik at to matriser blir skrevet ut på et fint format og addert med hverandre. 
# 
# En matrise er et godt eksempel på en todimensjonal liste av tall som har et bestemt antall rader x og et bestemt antall kolonner y. Du kan tenke på en matrise som en liste med x antall elementer, hvor hvert element er en liste av størrelse y. I denne oppgaven skal vi se på matriseaddisjon. I denne oppgaven definerer vi addisjon av to matriser på samme måte som med vektoraddisjon: dersom vi skal summere matrise a med b og kaller den nye matrisen for c, vil *c[x][y]* være *a[x][y]* + *b[x][y]*, hvor *c[x][y]* er elementet i matrisen c som befinner seg på rad *x* og kolonne *y*.
# 
# Du får gitt en main-funksjon med følgende kode:

# In[3]:


def main():
    A = random_matrise(4,3)
    print_matrise(A, 'A')
    B = random_matrise(3,4)
    print_matrise(B, 'B')
    C = random_matrise(3,4)
    print_matrise(C, 'C')
    D = matrise_addisjon(A,B)
    E = matrise_addisjon(B,C)
    print_matrise(E, 'B+C' )


# som, etter at du har gjort oppgaven, skal gi følgende utskrift:
# 
# ```python
# A=[
#    [1, 8, 4, 3]
#    [5, 1, 5, 8]
#    [9, 5, 8, 0]
#   ]
# B=[
#    [7, 3, 3]
#    [2, 1, 7]
#    [2, 2, 3]
#    [3, 5, 9]
#   ]
# C=[
#    [4, 4, 6]
#    [1, 9, 0]
#    [9, 8, 5]
#    [2, 9, 5]
#   ]
# Matrisene er ikke av samme dimensjon # A og B har ulike dimensjoner (ulikt antall rader og kolonner)
# B+C=[
#      [11, 7, 9]
#      [3, 10, 7]
#      [11, 10, 8]
#      [5, 14, 14]
#     ]
#     ```
#     
#     
# **Din oppgave**
# 
# Implementer funksjonene `random_matrise(bredde, høyde)`, `print_matrise(matrise, navn)` og `matrise_addisjon(a, b)` slik at utskriften av `main()` gir utskriften over.
# 
# 1. Funksjonen `random_matrise(bredde, høyde)` skal returnere en matrise med *høyde* antall rader og *bredde* antall kolonner. Matrisen skal være fylt med tilfeldige tall fra og med 0 til 10. Bruk random-biblioteket.
# 2. `print_matrise(matrise, navn)` skal printe ut matrisene på samme format som vist i utskriften over. 
# 3. `matrise_addisjon(a, b)` skal ta inn to matriser og returnere en matrise som er summen av a og b. Dersom to matriser er av ulik størrelse er det umulig å addere matrisene og "Matrisene er ikke av samme dimensjon" skal skrives ut. 
# 
# ***Skriv koden din i boksen under.***

# In[8]:


import random


def random_matrise( w, h ):
    matrix= []
    for i in range( h ):
        row = []
        for j in range( w ):
            row.append(random.randint(0,9))
        matrix.append(row)
    return matrix


def print_matrise( matrix, name ):
    print(f'{name}=[')
    ws = ' ' * (len( name ) + 1)
    for r in matrix:
        print( ws + ' ' + str( r ) )
    print( ws + ']' )


def matrise_addisjon( m1, m2 ):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        print("Matrisene er ikke av samme dimensjon")
    else:
        matirx =[]
        for i in range(len(m1)):
            row = []
            for j in range(len(m1[i])):
                row.append( m1[i][j] + m2[i][j] )
            matirx.append(row)
        return matirx

main()


# #### Hint

# For å sjekke om to matriser er av samme dimensjon må du sjekke om de både har samme antall rader og samme antall kolonner. len(matrise) returnerer antall rader en matrise har, og len(matrise[0]) returnerer antall kolonner i matrisen.
