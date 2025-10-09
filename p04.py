def negyszog(a,b):
    perimeter = 2*(a+b)
    area = a * b
    alakzat = 'teglalap'
    if a == b:
        alakzat = 'negyzet'
    return perimeter, area, alakzat


def szamolas(*args):
    osszeg = sum(args)
    legnagyobb = max(args)
    return osszeg,legnagyobb

sorozat = [1,2,3,4,5]
for elem in sorozat:
    print(elem)

for i in range(1,10,3):
    print(i)

print('Osszeg: ', szamolas(1,2,3))
print('Osszeg: ', szamolas(1,2,3,4))

eredmeny = negyszog(4,4)
print('Perimeter: ', szamolas[0])
print('Area: ', szamolas[1])
print('Alakzat: ', szamolas[2])

