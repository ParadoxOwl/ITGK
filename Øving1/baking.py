cookies_per_oppskrift=48
ingredienser = ["sukker(g)", "smør(g)", 'sjokolade(g)', "egg", "hvetemel(g)"]
mengde = [400.0, 320.0, 500.0, 2.0, 460.0]

def skaler_oppskrift(n_org, ingred, mengd, skalert_til):
    forhold= skalert_til / n_org
    ans = ''
    for i in range(len(ingred)):
        ans += ingred[i] + ": " + str(mengd[i]*forhold) + '\n'
    return ans

onske = int(input("hvor mange cookies ønsker du å bake?: "))
print(skaler_oppskrift(cookies_per_oppskrift, ingredienser, mengde, onske))
