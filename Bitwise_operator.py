'''
There are six bitwise operator
=> & (bitwise AND)
=> | (bitwise OR)
=> ~ (bitwise NOT)
=> ^ (bitwise XOR)
=> << (bitwise LEFT SHIFT)
=> >> (bitwise RIGHT SHIFT)
'''

a=0b1010 #0b means binary number
b=0b1100

#=> & (bitwise AND)
c= (a&b)
print(bin(c))


#=> | (bitwise OR)
d=(a|b)
print(bin(d))

#=> ~ (bitwise NOT)
e=(~a)
print(bin(e))

f=(~b)
print(bin(f))

#=> ^ (bitwise XOR)

g=(a^b)
print(bin(g))

#=> << (bitwise LEFT SHIFT)
h=(a<<2) #the digits of a will shift by two step in the left
print(bin(h))

#=> >> (bitwise RIGHT SHIFT)
i=(a>>1) #the digits of a will shift by one step in the right
print(bin(i))

print(bin(a>>2))