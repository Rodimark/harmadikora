import harmadikora
num = 10
while num > 2:
    num -= 1
    if num == 4:
        continue
    if num == 3:
        break
    print(num)
else:
    print('End of cycle')

#Hatultesztelo
while True:
    num += 1
    print(num)
