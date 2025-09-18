def nums(biggest_num):
    num = input('Please enter a number: ')
    if num.isdigit():
        num = int(num)
        if num == 0:
            print('Dont know the number 0')
        elif num > biggest_num:
            print('The num is too big')

    else:
        print('Invalid input')
    return num

def calculator():
    function = input('Please enter a function (+,-,*,/): ')
    num1 = nums(100)
    num2 = nums(200)
    if function == '+':
        print(f'The result is: {num1 + num2}')
    elif function == '-':
        print(f'The result is: {num1 - num2}')
    elif function == '*':
        print(f'The result is: {num1 * num2}')
    elif function == '/':
        print(f'The result is: {num1 / num2}')
    else:
        print('Invalid input')
        return

def rand(max):
    import random
    num = random.randint(0, max)
    return num

def whole_num():
    while True:
        num = input('Please enter a whole number: ')
        try:
            num = int(num)
            break
        except ValueError:
            print('Invalid input')
    return num

#Novekmenyes ciklus

# A program hivasa
if __name__ == '__main__':
    calculator()
#result = num1 + num2
#print(f'The results: {num1} + {num2} = {result}')