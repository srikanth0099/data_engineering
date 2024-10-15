a=int(input('Enter a number:'))
if a>0:
    print(f'The number {a} is +ve')
elif a<0:
    print(f'The number {a} is -ve')
else:
    print(0)


score=int(input('Enter score:'))
if score>90:
    print('Grade A')
elif score<=89 and score>=80:
    print('Grade B')
elif score<=79 and score>=70:
    print('Grade C')
else:
    print('Grade D')