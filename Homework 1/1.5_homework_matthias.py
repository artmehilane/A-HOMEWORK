def countDigits(, num: int) -> int:
        
        numbrid = [int(d) for d in str(num) if d != '0']
        lugeja = sum(1 for d in numbrid if num % d == 0)
        return lugeja
