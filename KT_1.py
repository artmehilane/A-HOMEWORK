def countDigits(, num: int) -> int:
        
        numbrid = [int(d) for d in str(num) if d != '0']
        lugeja = sum(1 for d in numbrid if num % d == 0)
        return lugeja


##
Testtitud leetcode poolt kasutades automaattesti

Loeb kokku arvu jagavad arvud:
        eraldame numbrid täisarvudena
        loendame numbrite arvu, mis jagavad numbrit
        funktsioon loendab tõeste väärtuste summa
        

Kasutatud keel:
        Pyhthon 3
        

