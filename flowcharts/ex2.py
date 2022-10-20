def Greatest(a,b,c):
    if a>b:
        if a>c:
            return a
        return c
    if b>c:
        return b
    return c

a = int(input('number a please:'))
b = int(input('number b please:'))
c = int(input('number c please:'))
print(Greatest(a,b,c))
