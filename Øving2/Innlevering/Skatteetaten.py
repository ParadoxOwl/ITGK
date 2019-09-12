#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving2.ipynb">Øving 2</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Ulike%20typer%20if-setninger.ipynb">Ulike typer if-setninger</a></li>
#     <li><a href="Sammenligning%20av%20strenger.ipynb">Sammenligning av strenger</a></li>
#     <li><a href="Logiske%20operatorer%20og%20logiske%20uttrykk.ipynb">Logiske operatorer og logiske uttrykk</a></li>
#     <li><a href="Forbrytelse%20og%20straff.ipynb">Forbrytelse og straff</a></li>
#     <li><a href="Aarstider.ipynb">Årstider</a></li>
#         <li ><a href="Tekstbasert%20spill.ipynb">Tekstbasert spill</a></li>
#     <li><a href="Sjakkbrett.ipynb">Sjakkbrett</a></li>
#     <li><a href="Billettpriser%20og%20rabatter.ipynb">Billettpriser og rabatter</a></li>
#     <li class="active"><a href="Skatteetaten.ipynb">Skatteetaten</a></li>
#     <li><a href="Epletigging.ipynb">Datamaskinen som tigget epler</a></li>
#     <li><a href="Andregradsligning.ipynb">Andregradsligning</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Skatteetaten
# 
# **Læringsmål:**
# 
# * Betingelser
# 
# **Starting Out with Python:**
# 
# * Kap. 3.1- 3.2
# * Kap. 3.4
#  
# 
# I denne oppgaven skal du lage et program som tar inn opplysninger om utleie av eiendom fra en bruker. Programmet vil så beregne hvor stor andel av inntekten som er skattbar.  
# 
# Regler for skatt finnes på Skatteetaten sine hjemmesider, men er ikke nødvendig å sette seg inn i: 
# 
# http://www.skatteetaten.no/no/Person/Selvangivelse/tema-og-fradrag/Jobb-og-utdanning/delingsokonomi/utleie-av-bolig-og-fritidsbolig/
# 
#  
# 
# 

# ### a)

# Lag et program som ber brukeren om opplysninger og svarer om inntekten er skattepliktig eller skattefri. 
# 
# Regler som må implementeres:
# 
# * Hvis du bruker minst halvparten av boligen du eier til eget bruk, beregnet etter utleieverdi, er det skattefritt å leie ut resten.
# *  Leier du ut mer enn halvparten av egen bolig, men for under 20 000 kr i året er det også skattefritt.
# * Leier du ut hele eller mer enn halvparten av egen bolig for over 20 000 kr i året er samtlige leieinntekter for hele året skattepliktige. 
# 
# **Eksempel på kjøring av kode:**
#  
# ```python
# INFO  
# Dette programmet besvarer om din utleie av egen bolig er skattepliktig. 
# Først trenger vi å vite hvor stor del av boligen du har leid ut.
# Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,
# 20 en mindre del av boligen som f.eks. en hybel.
# ----------------------------------------------------------------------  
# DATAINNHENTING:  
# Oppgi hvor mye av boligen som ble utleid: 65  
# Skriv inn hva du har hatt i leieinntekt: 45000   
# ----------------------------------------------------------------------  
# SKATTEBEREGNING:  
# Inntekten er skattepliktig  
# Skattepliktig beløp er 45000
# ```
# 
# ***Skriv koden din her:***

# In[ ]:


def private_home():
    print ('''INFO
Dette programmet besvarer om din utleie av egen bolig er skattepliktig.
Først trenger vi å vite hvor stor del av boligen du har leid ut.
Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,
20 en mindre del av boligen som f.eks. en hybel.
----------------------------------------------------------------------
DATAINNHENTING:  ''')
    ppc = int(input('Oppgi hvor mye av boligen som ble utleid: '))
    rent = int(input('Skriv inn hva du har hatt i leieinntekt: '))
    if ppc <= 50 or rent < 20000:
        print('''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er ikke skattepliktig''')
    else:
        print(f'''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er skattepliktig
Skattepliktig beløp er {rent}''')

private_home()


# ### b)

# For å leie ut *sekundærbolig* eller *fritidsbolig* gjelder det særskilte regler. Lag et tilsvarende program som dekker disse behovene. (Se samme nettside for mer informasjon om ønskelig.)
# 
# Regler som må implementeres:
# 
# * Sekundærbolig:
#  * Utleie av sekundærbolig beskattes fra første krone.
# * Fritidsbolig:
#  * Der du helt eller delvis bruker fritidsboligen til fritidsformål, og selv bruker eiendommen i rimelig omfang over tid, så vil utleieinntekter inntil kr 10 000 være skattefrie.
#  * Av det overskytende beløp regnes 85 prosent som skattepliktig inntekt.
#  * Dersom fritidsboligen anses som utleiehytte blir det beskatning fra første krone.
#  * Om du leier ut flere enn en fritidsbolig vil grensen på 10 000 gjelde per fritidsbolig.
#  
# **Eksempel på kjøring av kode:**
#  
# ```python
# INFO
# Dette programmet besvarer om din utleie en annen type bolig,
# her sekundær- eller fritidsbolig, er skattepliktig.
# Først trenger vi å vite om du leier ut en sekundær- eller en fritidsbolig.
# ---------------------------------------------------------------------
# DATAINNHENTING:
# Skriv inn type annen bolig (sekundærbolig/fritidsbolig) du har leid ut: Fritidsbolig
#     
# INFO
# Du har valgt fritidsbolig.
# Nå trenger vi først å vite om fritidsboligen(e) primært brukes til utleie eller fritid.
# Deretter trenger vi å vite hvor mange fritidsbolig(er) du leier ut.
# Til slutt trenger vi å vite hvor store utleieinntekter du har pr. fritidsbolig.
# 
# ---------------------------------------------------------------------
# DATAINNHENTING:
# Skriv inn formålet med fritidsboligen(e): Fritid
# Skriv inn antallet fritidsboliger du leier ut: 3
# Skriv inn utleieinntekten pr. fritidsbolig: 15000
#     
# ---------------------------------------------------------------------
# SKATTEBEREGNING:
# Inntekten er skattepliktig
# Overskytende beløp pr. fritidsbolig er 5000
# Skattepliktig inntekt pr. fritidsbolig er 4250
# Totalt skattepliktig beløp er 12750
# ```
# 
# ***Skriv koden din her:***

# In[2]:


def secondary_home():
    rent = int(input('Skriv inn hva du har hatt i leieinntekt: '))
    print(f'''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er skattepliktig
Skattepliktig beløp er {rent}''')


def leisure_home():
    print('''
INFO
Du har valgt fritidsbolig.
Nå trenger vi først å vite om fritidsboligen(e) primært brukes til utleie eller fritid.
Deretter trenger vi å vite hvor mange fritidsbolig(er) du leier ut.
Til slutt trenger vi å vite hvor store utleieinntekter du har pr. fritidsbolig.

---------------------------------------------------------------------
DATAINNHENTING:''')
    use = input( 'Skriv inn formålet med fritidsboligen(e): ' )
    num = int( input( 'Skriv inn antallet fritidsboliger du leier ut: ' ) )
    rent = int( input( 'Skriv inn utleieinntekten pr. fritidsbolig: ' ) )
    if use.lower() == 'fritid' and rent <= 10000:
        print('''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er ikke skattepliktig''')
    elif use.lower() == 'fritid':
        print(f'''----------------------------------------------------------------------
SKATTEBEREGNING
Inntekten er skattepliktig
Overskytende beløp pr. fritidsbolig er {rent-10000}
Skattepliktig inntekt pr. fritidsbolig er {(rent-10000)*num*0.85:.2f}
Totalt skattepliktig beløp er {(rent-10000)*num*0.85:.2f}''')
    else:
        print(f'''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er skattepliktig
Skattepliktig beløp er {rent * num}''')


def other():
    print('''INFO
Dette programmet besvarer om din utleie en annen type bolig,
her sekundær- eller fritidsbolig, er skattepliktig.
Først trenger vi å vite om du leier ut en sekundær- eller en fritidsbolig.
---------------------------------------------------------------------
DATAINNHENTING:''')
    type = input('Skriv inn type annen bolig (sekundærbolig/fritidsbolig) du har leid ut:')
    if type.lower() == 'fritidsbolig':
        leisure_home()
    elif type.lower() == 'sekundærbolig':
        secondary_home()
    else:
        return


other()


# ### c)

# Sett sammen del (a) og (b) til et større program som først spør brukeren hva som er blitt leid ut (egen bolig / sekundærbolig / fritidsbolig), og deretter regner ut passende skattesats. Du kan delvis kopiere koden fra de tidligere deloppgavene.
# 
# ***Skriv koden din her:***

# In[ ]:


def private_home():
    print ('''INFO
Du har valgt primærbolig.
Først trenger vi å vite hvor stor del av boligen du har leid ut.
Angi dette i prosent, 100 betyr hele boligen, 50 betyr halve,
20 en mindre del av boligen som f.eks. en hybel.
----------------------------------------------------------------------
DATAINNHENTING:  ''')
    ppc = int(input('Oppgi hvor mye av boligen som ble utleid: '))
    rent = int(input('Skriv inn hva du har hatt i leieinntekt: '))
    if ppc <= 50 or rent < 20000:
        print('''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er ikke skattepliktig''')
    else:
        print(f'''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er skattepliktig
Skattepliktig beløp er {rent}''')


def secondary_home():
    rent = int(input('Skriv inn hva du har hatt i leieinntekt: '))
    print(f'''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er skattepliktig
Skattepliktig beløp er {rent}''')


def leisure_home():
    print('''
INFO
Du har valgt fritidsbolig.
Nå trenger vi først å vite om fritidsboligen(e) primært brukes til utleie eller fritid.
Deretter trenger vi å vite hvor mange fritidsbolig(er) du leier ut.
Til slutt trenger vi å vite hvor store utleieinntekter du har pr. fritidsbolig.

---------------------------------------------------------------------
DATAINNHENTING:''')
    use = input( 'Skriv inn formålet med fritidsboligen(e): ' )
    num = int( input( 'Skriv inn antallet fritidsboliger du leier ut: ' ) )
    rent = int( input( 'Skriv inn utleieinntekten pr. fritidsbolig: ' ) )
    if use.lower() == 'fritid' and rent <= 10000:
        print('''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er ikke skattepliktig''')
    elif use.lower() == 'fritid':
        print(f'''----------------------------------------------------------------------
SKATTEBEREGNING
Inntekten er skattepliktig
Overskytende beløp pr. fritidsbolig er {rent-10000}
Skattepliktig inntekt pr. fritidsbolig er {(rent-10000)*num*0.85:.2f}
Totalt skattepliktig beløp er {(rent-10000)*num*0.85:.2f}''')
    else:
        print(f'''----------------------------------------------------------------------
SKATTEBEREGNING:
Inntekten er skattepliktig
Skattepliktig beløp er {rent * num}''')


def other():
    print('''INFO
Dette programmet besvarer om din utleie av bolig,
her sekundær-, primær- eller fritidsbolig, er skattepliktig.
Først trenger vi å vite om du leier ut en primær-, sekundær- eller en fritidsbolig.
---------------------------------------------------------------------
DATAINNHENTING:''')
    type = input('Skriv inn type annen bolig (primærbolig/sekundærbolig/fritidsbolig) du har leid ut:')
    if type.lower() == 'fritidsbolig':
        leisure_home()
    elif type.lower() == 'sekundærbolig':
        secondary_home()
    elif type.lower() == 'primærbolig':
        private_home()
    else:
        print('ikke gyldig input')
        return


other()

