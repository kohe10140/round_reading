def xor(a, b):
    print('a', bin(a))
    print('b', bin(b))
    c = a ^ b
    res = 0
    while c != 0:
        if c & 1 == 1:
            res += 1
        c = c >> 1
    return res

print(xor(17, 23))
print(xor(100, 23))
print(xor(64, 15))
print(xor(63, 15))
print(xor(10, 10))
