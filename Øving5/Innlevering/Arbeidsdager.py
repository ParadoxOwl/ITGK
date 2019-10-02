#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving5.ipynb">Øving 5</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Grunnleggende%20om%20funksjoner.ipynb">Grunnleggende om funksjoner</a></li>
#     <li><a href="Varierte%20funksjoner.ipynb">Varierte funksjoner</a></li>
#     <li><a href="Lokale%20variabler.ipynb">Lokale variabler</a></li>
#     <li><a href="Globale%20variabler.ipynb">Globale variabler</a></li>
#     <li><a href="Euklids%20algoritme.ipynb">Euklids algoritme</a></li>
#     <li><a href="Primtall.ipynb">Primtall</a></li>
#     <li><a href="Multiplikasjon.ipynb">Multiplikasjon</a></li>
#         <li><a href="Den%20store%20sporreundersokelsen.ipynb">Den store spørreundersøkelsen</a></li>
#     <li class="active"><a href="Arbeidsdager.ipynb">Arbeidsdager</a></li>
#     <li><a href="Sekantmetoden.ipynb">Sekantmetoden</a></li>
#     <li><a href="Not%20quite%20Blackjack.ipynb">Not quite Blackjack</a></li>
#         <li><a href="Funksjoner%20og%20Jupyter%20widgets.ipynb">Funksjoner og Jupyter widgets</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Arbeidsdager
# 
# **Læringsmål:**
# - Funksjoner 
# - Betingelser
# - Løkker
# 
# **Starting Out with Python:**
# - Kap. 3.1-3.2
# - Kap. 4.3
# - Kap. 5.3
# - Kap. 5.5
# - Kap. 5.8
# 

# Et vanlig år består av 52 hele uker og én dag, til sammen 365 dager. Det vil si at hvis ett år starter på en mandag, starter neste år på en tirsdag. Skuddår har en dag ekstra. Dvs. hvis et skuddår starter på en mandag, starter neste år på en onsdag. 1. januar 1900 var en mandag. Skuddår er litt finurlig definert. Bruk følgende funksjon til å bestemme om et år er et skuddår:

# In[ ]:


# Trykk ctrl + enter her så har du denne funksjonen til senere oppgaver
def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


# ## a)

# Lag først en funksjon `weekday_newyear(year)` som tar inn et årstall, og returnerer hvilken ukedag året starter på. Ukedager representeres med heltall, dvs. mandag = 0, tirsdag = 1, ..., søndag = 6. 
# 
# *Merk: Deloppgaven skal løses uten å bruke Pythons innebygde datofunksjoner.*
# 
# Skriv deretter ut årstall med tilhørende første ukedag i tekstlig format for år 1900 til og med 1919 ved å benytte funksjonen `weekday_newyear(year)`.
# 
# ***Skriv koden i kodeblokken under***

# In[2]:


def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def weekday_newyear( year ):
    base = 1900
    day = 0
    for y in range( base, year ):
        if is_leap_year( y ):
            day += 2
        else:
            day += 1
        day = day % 7
    return day


days = [ 'man', 'tir', 'ons', 'tor', 'fre', 'lor', 'son' ]
for y in range(1900, 1920):
    print( f'{y} {days[weekday_newyear( y )]}' )
    #print(f'{y} har {workdays_in_year( y )}arbeidsdager')


# Hvis du har gjort alt riktig skal koden din gi følgende output:
# ```python
# 1900 man
# 1901 tir
# 1902 ons
# 1903 tor
# 1904 fre
# 1905 son
# 1906 man
# 1907 tir
# 1908 ons
# 1909 fre
# 1910 lor
# 1911 son
# 1912 man
# 1913 ons
# 1914 tor
# 1915 fre
# 1916 lor
# 1917 man
# 1918 tir
# 1919 ons
# ```

# ## b)

# Lag funksjonen `is_workday(day)` som tar inn en ukedag, og returnerer `True` om ukedagen er arbeidsdag, og `False` ellers. (Alle hverdager er arbeidsdager. Lørdag og søndag er ikke arbeidsdager. For eksempel skal `is_workday(2)` returnere `True`, mens `is_workday(5)` skal returnere `False`.
# 
# ***Skriv koden din i kodeblokken under og test at den fungerer***

# In[3]:


def is_workday( day ):
    if day < 5:
        return True
    else:
        return False


print(is_workday(2))
print(is_workday(5))


# ## c)

# Lag først funksjonen `workdays_in_year(year)` som tar inn et årstall og skriver ut antall arbeidsdager i det gitte året. (Vi ser bort ifra helligdager som faller på arbeidsdager, dvs. at bl.a. langfredag vil telles som en arbeidsdag.) 
# 
# Husk at skuddår har en ekstra dag i februar. 
# 
# Skriv deretter ut antall arbeidsdager for årene 1900 til og med 1919.
# 
# ***Skriv koden din i kodeblokken under***

# In[4]:


def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def weekday_newyear( year ):
    base = 1900
    day = 0
    for y in range( base, year ):
        if is_leap_year( y ):
            day += 2
        else:
            day += 1
        day = day % 7
    return day


def is_workday( day ):
    if day < 5:
        return True
    else:
        return False


def workdays_in_year( year ):
    base = 52*5
    if is_leap_year( year ):
        if weekday_newyear( year ) is 4:
            return base + 1
        elif weekday_newyear( year ) is 5:
            return base
        else:
            return base + 2
    else:
        if is_workday( weekday_newyear( year ) ) is False:
            return base
        else:
            return base + 1


days = [ 'man', 'tir', 'ons', 'tor', 'fre', 'lor', 'son' ]
for y in range(1900, 1920):
    #print( f'{y} {days[weekday_newyear( y )]}' )
    print(f'{y} har {workdays_in_year( y )}arbeidsdager')


# **Hint:** Benytt deg av tidligere lagde funksjoner for å slippe å skrive mye kode på nytt.

# Har du gjort alt riktig skal koden din gi følgende output:
# 
# ```python
# 1900 har 261 arbeidsdager
# 1901 har 261 arbeidsdager
# 1902 har 261 arbeidsdager
# 1903 har 261 arbeidsdager
# 1904 har 261 arbeidsdager
# 1905 har 260 arbeidsdager
# 1906 har 261 arbeidsdager
# 1907 har 261 arbeidsdager
# 1908 har 262 arbeidsdager
# 1909 har 261 arbeidsdager
# 1910 har 260 arbeidsdager
# 1911 har 260 arbeidsdager
# 1912 har 262 arbeidsdager
# 1913 har 261 arbeidsdager
# 1914 har 261 arbeidsdager
# 1915 har 261 arbeidsdager
# 1916 har 260 arbeidsdager
# 1917 har 261 arbeidsdager
# 1918 har 261 arbeidsdager
# 1919 har 261 arbeidsdager
# ```
