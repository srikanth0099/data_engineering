count=0
num=17

if num<=1:
    print(f'{num} is not a prime number')
if num==2 or num==3:
    print(f'{num} is a prime number')
for i in range(4,num+1):
    if num%i==0:
        count+=1
    else:
        pass
if count==2:
    print("It's a prime")
else:
    print("It's not a prime")



l=[]
for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        l.append(i)
num=20
print(f'Prime numbers until {num} are {l}')




def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

if is_prime(num):
    print(f'{num} is a prime')
else:
    print(f'{num} is not a prime')



