def clearBitsMSBthroughI(num, i):
    mask = (1<<i) -1
    return num & mask

def clearBitsIthrough0(num, i):
    mask = -1 << (i+1)
    return num & mask

def insert(N, M, i, j):
    mid = M << i
    right = clearBitsMSBthroughI(N, i)
    left = clearBitsIthrough0(N, j)
    return right | mid | left

N = 0b10000000000
M = 0b10011
i = 2
j = 6
print(bin(insert(N, M, i, j)))

N = 0b10000
M = 0b11
i = 1
j = 2
print(bin(insert(N, M, i, j)))