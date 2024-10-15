# for loop
total=0
for i in range(1,101):
    total+=i
print(f'total: {total}')

# List Comprehension
total=sum([num for num in range(1,101)])
print(f'total: {total}')


numbers=[i for i in range(1,21)]

for num in numbers:
    if num%3==0:
        continue
    else:
        print(num)