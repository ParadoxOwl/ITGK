Pizza = 750
Studentrabatt = 0.20
Tipps = 0.08

print(f'Pizza: {Pizza}kr\nStudentrabatt: {Studentrabatt*100}%\nTipps: {Tipps*100}%\nTotal: {Pizza*(1-Studentrabatt)*(1+Tipps)}kr')
