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
