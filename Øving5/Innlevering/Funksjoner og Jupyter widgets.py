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
#     <li ><a href="Euklids%20algoritme.ipynb">Euklids algoritme</a></li>
#     <li><a href="Primtall.ipynb">Primtall</a></li>
#     <li><a href="Multiplikasjon.ipynb">Multiplikasjon</a></li>
#         <li><a href="Den%20store%20sporreundersokelsen.ipynb">Den store spørreundersøkelsen</a></li>
#     <li><a href="Arbeidsdager.ipynb">Arbeidsdager</a></li>
#     <li><a href="Sekantmetoden.ipynb">Sekantmetoden</a></li>
#     <li><a href="Not%20quite%20Blackjack.ipynb">Not quite Blackjack</a></li>
#     <li class="active"><a href="Funksjoner%20og%20Jupyter%20widgets.ipynb">Funksjoner og Jupyter widgets</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Funksjoner og Jupyter widgets
# 
# **Læringsmål:**
# - Funksjoner
# 
# Det er mye vi kan bruke funksjoner til i python. I jupyter finnes det et eget bibliotek med knapper og andre interaktive verktøy kalt widgets. Med widgets kan vi interagere med brukeren på et litt annet nivå enn det å ta tekstlig input fra konsollen tillater. Det anbefales å ta en liten kikk på dokumentajsonen til widgets før du setter i gang, [her](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html).  

# ### Interact

# Under ser vi hvordan vi kan definere en simpel funksjon, før vi kobler sammen funksjonen med grensesnittkontroller i form av en slider. Funksjonen vil så kalles med hva enn slideren er satt til. Når vi beveger slideren kalles funksjonen med sliderens verdi og verdien printes. **Kjør koden under**

# In[1]:


from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
import ipywidgets as widgets

def f(x):
    return x

interact(f, x=10)


# **Oppgave a): Lag en slider hvor kvadratet av tallet slideren er satt til pluss 10 printes ut. Sett sliderens standardverdi til 3, minimumsverdien til -15, og maksverdien til 20. Steglengden skal være 0.2**

# In[5]:


def g( x ):
    return x**2 + 10

interact(g, x=widgets.FloatSlider(min = -15, max = 20, step = 0.2, value =3))


# #### Hint

# Se [her](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html#Widget-abbreviations) og [her](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html). Husk at det er forskjell på int og float.

# ### Interact med andre datatyper

# På helt lik linje kan vi kalle funksjonen vår med helt andre datatyper, så lenge vi ikke gjør noe ulovlig med dem inne i funksjonen. Setter vi x til en boolean vil vi heller få opp en avkrysningsboks, som enten vil være True eller False. Setter vi x til en streng vil få opp en tekstboks.

# In[4]:


interact(f, x=True)
interact(f, x = "Hei, hva heter du?")


# **Oppgave b):** Lag en funksjon `equation(a,b,c,x,reverse,statement)` som tar inn fem argumenter ved hjelp av widgets, a,b,c og x skal være heltall, reverse en boolean, og statement en streng. Funksjonen skal returnere statement, men dersom reverse er True, skal det være stor bokstav der det tidligere var liten, og motsatt. Deretter skal den regne ut
# 
# $ax^{2}+bx+c$ 
# 
# og dersom reverse er True skal fortegnet til a ganges med -1. 
# 
# Eksmpel på kjøring:
# ```python
# >>> print(equation(2,2,2,1,True, "Hei")
# ("hEI", 2)
# >>> print(equation(2,2,2,1,False, "Hei")
# ("Hei", 6)
# >>> print(equation(5,1,-10,20,False, "Heiho")
# ("Heiho", 2010)
# ```

# In[17]:


from string import ascii_uppercase, ascii_lowercase


def reverse_caps( statement ):
    tmp = ''
    if statement is '':
        return tmp
    for c in statement:
        if c in ascii_lowercase:
            tmp += c.upper()
        elif c in ascii_uppercase:
            tmp += c.lower()
        else:
            tmp += c
    return tmp


@interact( a=10, b=10, c=10, x=10, reverse=False, statement='' )
def equation( a, b, c, x, reverse, statement ):
    if reverse:
        a = -a
        statement = reverse_caps( statement )
    ans = a*(x**2) + b*x + c
    return statement, ans


# #### Hint

# En funksjon i python kan enkelt returnere to verdier separert med komma.
# ```python
# def funksjon()
#     return "hei",6
# ```
# Her må vi i tillegg iterere over en streng, noe vi teknisk sett ikke har lært enda. Du kan lese litt mer om dette [her](https://thispointer.com/python-how-to-iterate-over-the-characters-in-string/).

# ### Buttons

# Jupyter lar oss også benytte oss av buttons, som vi kan koble sammen med funksjoner. I tillegg la oss ta en kikk på Textarea, som vi kan bruke til å ta input fra bruker på en litt annen måte. 

# In[18]:


tekst = widgets.Textarea(
    value='Hello World',
    placeholder='Type something',
    description='tekst:',
    disabled=False
)
display(tekst)
print(tekst.value)


# Over ser vi et eksempel på et tekstfelt, hvor vi etterpå prøver å printe verdien som gis inn i tekstfeltet. Dette ser vi ikke fungerer om vi prøver å endre verdien i tekstfeltet og kjøre koden på nytt. La oss heller se på hvordan en knapp fungerer. Under ser vi hvordan vi definerer en knapp og så en funksjon som kalles når knappen trykkes. Merk at funksjonen hello tar inn en parameter b, denne parameteren vil da være knappen selv, altså button. Dette trenger du ikke tenke så mye på, bare vit at når definerer en funksjon som kalles når knappen trykkes, må denne parameteren alltid være med. 

# In[20]:


button = widgets.Button(
    description='Click me',
    disabled=False,
    tooltip='Click me',
)
tekst = widgets.Textarea(
    value='Hello World',
    placeholder='Type something',
    description='tekst:',
    disabled=False
)

def hello(b):
    print(tekst.value)
    
button.on_click(hello)
display(tekst)
display(button)


# **Oppgave c):** Endre funksjonen hello så den printer ut det som er skrevet inn i tekstfeltet "tekst".

# **Oppgave d)**: Lag en funksjon som stiller brukeren et flervalgsspørsmål. Ta derimot inn i svaret ved hjelp av RadioButtons-widgeten. Sjekk svaret ved bruk av en knapp og fortell brukeren om den svarte riktig eller galt. 

# In[48]:


def is_correct(b):
    question.disabled = True
    if question.value is 'True':
        print('Correct answer')
    else:
        print('Wrong Answer')
    return


question = widgets.RadioButtons(
    options = [ 'True', 'False' ],
#    description = 'test',
    disabled = False
)

button = widgets.Button(
    description='Submit',
    disabled=False,
)

print('test')
display( question )
display( button )
button.on_click(is_correct)


# #### Hint

# Det kan værte lurt å se [her](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Selection-widgets). Python har også støtte for å definere funksjoner inni funksjoner, les mer om disse [her](https://realpython.com/inner-functions-what-are-they-good-for/).
