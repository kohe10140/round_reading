import decimal
decimal.getcontext().prec = 64

def digit2bin(num):
    res = '0.'
    cnt = 1
    while cnt <= 32:
        num = decimal.Decimal(num)
        num *= 2
        if num >= 1:
            res += '1'
            num -= 1
        else:
            res += '0'
        cnt += 1
        if num == 0:
            return res
        num = decimal.Decimal(num)
    else:
        return "ERROR"

print(digit2bin(0.375))
print(digit2bin(0.4444))
print(digit2bin(0.25))
print(digit2bin(0.125))
