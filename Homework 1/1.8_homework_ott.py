def reverse(x):
    if x < 2147483647 and x > -2147483647:
        arv = str(x)
        vastus = ""
        esimene = arv[0]
        i = len(arv) - 1
        if esimene == '-':
            vastus += '-'
            while i >= 1:
                vastus += arv[i]
                i -= 1
        else:
            while i >= 0:
                vastus += arv[i]
                i -= 1
        vastus = int(vastus)
        return vastus
    else:
        return 0

test = 123
print(reverse(test))
#comm
