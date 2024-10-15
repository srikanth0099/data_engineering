import random
a=random.randint(1,20)
guess=int(input('Enter a number:'))
if(a==guess):
    print('Your guess is correct')
else:
    print('Your guess is wrong')
    print(f'The number is {a}')
