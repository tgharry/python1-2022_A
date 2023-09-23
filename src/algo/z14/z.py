f = b'011012'
print(f)
print(type(f))

ba = bytearray(10)
print(type(ba))
print(ba)
ba[0] = 5
print(ba)
ba[1] = 2
print(ba)

print(type(ba[0]))  # int
x = 10
print(bin(x))  # 0b1010
print((x >> 3) & 1)  # 1
print(x | (1 << 2))  # 14
