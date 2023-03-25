def reverse(x):
    if x < 2147483647 and x > -2147483647: #ei näe selle vajadust aga ig if-i jaoks
        arv = str(x)
        vastus = ""
        esimene = arv[0]
        i = len(arv) - 1
        if esimene == '-':
            vastus += '-' #mul jääks oma versioniga sama süsteem algusesse
            while i >= 1:
                vastus += arv[i]
                i -= 1
        else:
            while i >= 0:
                vastus += arv[i]
                i -= 1
        vastus = int(vastus) #ngl ma ei oskaks ka seda paremaks teha kuna
        return vastus	     #while tsükkel on effective ja sõne tükeldus+ list join võtaks kauem aega
    else:
        return 0

test = 123
print(reverse(test))
"""
def reverse(x):
    arv=str(x)
    i = len(arv)-1
    a=lst()
    b=""
    if arv[0] == "-":
            b+= "-"
            arv.remove(arv[0])
    for taht in arv:
        a.append(taht)
    c = reversed(a)
    vastus.append(c.join())
    return vastus
"""
ma teeks u nii seda
        