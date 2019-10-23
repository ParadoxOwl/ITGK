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
#     <li ><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#     <li class="active"><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li ><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>  
#     </ul>
#   </div>
# </nav>
# 
# ## Søke i tekst
# 
# **Læringsmål:**
# 
# * Lese fra fil
# * Tekstbehandling
# * Dictionary
# 
# **Starting Out with Python:**
# 
# * Kap. 6: Files and Exceptions
# * Kap. 9: Dictionaries and Sets
#  
# 
# I denne oppgaven skal du bli bedre kjent med dictionaries og lesing fra fil. Bruk gjerne innebygde funksjoner, alt er lov!

# ### a)

# Lag en funksjon **`read_from_file(filename)`** som tar inn en string (**filename**) og returnerer innholdet i filen. Dersom funksjonen tar inn 'Alice_in_wonderland.txt' bør utskriften bli følgende:
# 
# **Kjøring av kode:**
# 
# ```
# Alice's Adventures in Wonderland
# 
#                 ALICE'S ADVENTURES IN WONDERLAND
# 
#                           Lewis Carroll
# 
#                THE MILLENNIUM FULCRUM EDITION 3.0
# 
# 
# 
# 
#                             CHAPTER I
# 
#                       Down the Rabbit-Hole
# 
# .
# .
# .
# 
# ```
# ***Skriv koden din i boksen under.***

# In[1]:


def read_from_file( filename ):
    f = open( filename, 'r' )
    txt = f.read()
    f.close()
    return txt


print( read_from_file( 'alice_in_wonderland.txt' ) )


# ### b)

# Lag en funksjon **`remove_symbols(text)`** som fjerner alle spesialtegn fra teksten **text**, og gjør alle bokstaver små (lowercase).   
# Ting som skal fjernes er slik som tall, komma, punktum og fnutter. La mellomrom stå slik at du kan skille ord fra hverandre.
# 
# Dersom funksjonen tar inn 'Alice_in_wonderland.txt' bør utskriften bli følgende:
# 
# **Kjøring av kode:**
# ```alices adventures in wonderland                alices adventures in wonderland                          lewis carroll ...```
# 
# ***Skriv koden din i boksen under.***

# In[3]:


import string

def remove_symbols( text ):
    for symb in string.printable:
        if symb not in string.ascii_letters and not symb.isspace() :
            text = text.replace( symb, '' )
    return text.lower()


story = read_from_file( 'alice_in_wonderland.txt' )
print(remove_symbols( story ))


# #### Hint

# Dette kan gjøres ved hjelp av funksjonene *.join()*, *.isalpha()* og *.lower()*. 
# 
# lower() gjør alle bokstavene i en streng små.

# In[ ]:


streng = 'Hei pÅ deg'
streng = ord.lower()
print(streng)


# isalpha() sjekker om en streng kun består av bokstaver

# In[ ]:


streng = 'Hei'
print(streng.isalpha())     
streng = 'Hei på deg'
print(streng.isalpha()) 
streng = "Hei!!!!"
print(streng.isalpha())


# join() returnerer en streng hvor strengelementene i en liste blir knyttet sammen av str operatoren.

# In[ ]:


s = '-'
seq = ('a', 'b', 'c')
print(s.join(seq))


# ### c)

# Lag en funksjon **`count_words(filename)`** som tar inn en streng (**filename**), teller antall forekomster av alle ord i filen og returnerer en dictionary med resultatet.
# 
# ***Skriv koden din i boksen under.***

# In[10]:


def count_words( filename ):
    text = remove_symbols( read_from_file( filename ) )
    words = text.split()
    d = {}
    for word in words:
        if word.isalpha():
            try:
                d[word] += 1
            except KeyError:
                d[word] = 1
    return d


# #### Hint

# Bruk en dictionary med **ord** som nøkkel og **antall forekomster** som value.

# ### d)

# Sjekk om oppgave c) fungerer ved å kjøre funksjonen med 'Alice_in_wonderland.txt' som argument.
# 
# *Du kan skrive ut hver linje i dictionarien for seg ved å bruke:*

# In[11]:


alice_dict = count_words('alice_in_wonderland.txt')
for word, value in alice_dict.items():
    print(word, value)

