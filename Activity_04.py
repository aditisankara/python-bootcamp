a = int(input("a = "))
b = int(input("b = "))
print("%d + %d = %d" %(a, b, (a+b)))

c = a + b
s = f'{a} + {b} = {c}'
print(s)

t = '{} + {} = {}'.format(a, b, (a+b))
print(t)

u = repr(a) + '+' + repr(b) + '=' + repr(c)
print(u)


