nCookies = 48
nSjoko = 500.0
nSukk = 400.0

antall = []
for i in range(3):
    antall.append(int(input(f'Hvor mange cookies vil du lage {i+1}. gang: ')))

print(f'Antall cookies: \t sukker(g)\tsjokolade(g)')
for i in range(len(antall)):
    rel=antall[i]/nCookies
    print(f'{antall[i]}\t\t\t {nSukk*rel:.1f}\t\t{nSjoko*rel:.1f}')
