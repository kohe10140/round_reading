def exchange(n):
    print(bin(n))
    return ((0xAAAAAAAAAAAAAAAA&n) >> 1) | ((0x5555555555555555&n) << 1)

print(bin(exchange(33)))
print(bin(exchange(23414)))
