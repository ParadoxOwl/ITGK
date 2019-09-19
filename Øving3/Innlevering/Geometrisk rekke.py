#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving3.ipynb">Øving 3</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Intro%20til%20lokker.ipynb">Intro til løkker</a></li>
#     <li ><a href="Mer%20om%20lokker.ipynb">Mer om løkker</a></li>
#     <li><a href="Nostede%20lokker.ipynb">Intro til nøstede løkker</a></li>
#     <li ><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li ><a href="Gjett%20tallet.ipynb">Gjett tallet</a></li>
#         <li ><a href="Tekstbasert%20spill%202.ipynb">Tekstbasert spill 2</a></li>
#     <li class="active"><a href="Geometrisk%20rekke.ipynb">Geometrisk rekke</a></li>
#     <li ><a href="Fibonacci.ipynb">Fibonacci</a></li>
#     <li><a href="Alternerende%20sum.ipynb">Alternerende sum</a></li>
#     <li ><a href="Hangman.ipynb">Hangman</a></li>
#     <li ><a href="Doble%20lokker.ipynb">Doble løkker</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Geometrisk rekke
# 
# **Læringsmål:**
# 
# * Løkker
# 
# **Starting Out with Python:**
# 
# * Kap. 4.2-4.3
# 
# En geometrisk rekke er en sum som kan skrives på formen under: 
# 
# $\sum_{i=0}^{n}r^{i}=r^{0}+r^{1}+r^{2}+r^{3}+\cdot \cdot \cdot +r^{n}$  
# $r \in (-1,1)$

# ### a)

# Lag et program som summerer en geometrisk rekke fra 0 til n ved hjelp av en while løkke.
# 
# Sjekk: r = 0.5 og n = 4 skal gi sum = 1.9375
# 
# ***Skriv koden din her:***

# In[3]:


def geo_n( r, n ):
    result = 0
    for i in range( n + 1 ):
        result += r**i
    return result


def geo_t( r, t ):
    result = 0
    itr = 0
    limit = 1/(1-r)
    while abs( limit - result ) > t:
        result += r**itr
        itr += 1
    return result


def geo_t_itr_dif( r, t ):
    result = 0
    itr = 0
    limit = 1/(1-r)
    while abs( limit - result ) > t:
        result += r**itr
        itr += 1
    return itr - 1, abs( limit - result )


foo = geo_t_itr_dif(0.5, 0.001)
print(f'Påkrevde iterasjoner: {foo[0]}\nDifferanse: {foo[1]}')


# ### b) 

# Skriv om programmet ditt slik at løkken avsluttes når din sum er innenfor en toleranse tol til grenseverdien av summen (verdien til summen når n går mot uendelig; se hint).
# 
# Test dette med tol = 0.001, r = 1/2, som vist i eksempelet under.

# #### Hint

# Summen til en geometrisk rekke er $\frac{1-r^{n+1}}{1-r}$
# . For rekken i b) blir grenseverdien $\frac{1}{1-r}$ = 2.

# ### c)

# La programmet gi ut antall iterasjoner som trengs for å være innenfor toleransen. Gi også ut den virkelige differansen mellom summen du fant og grenseverdien.

# ### Eksempel

# Eksempel på kjøring av kode a, b, og c:
# ```
# #a)  
# Summen av rekken er 1.9375  
# #b&c)  
# For å være innenfor toleransegrensen: 0.001 , kjørte løkken  11 ganger.  
# Differansen mellom virkelig og estimert verdi var da 0.0009765625
# ```
