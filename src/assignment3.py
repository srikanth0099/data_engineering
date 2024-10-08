# create list with 8 numbers of your choice
# Find the largest and smallest
# Sort those numbers in descending order
# Find sum of all elements
# craete a list of strings 
# convert all into upper case
# FInd largest string and shortest string
# Join list by using '-'

list = [5.43, 2, 22.7, 1.32, 32, 9, 4, 18]
list.sort(reverse= True)
print(list)
largest=list[0]
print(largest)
smallest=list[-1]
print(smallest)
print(sum(list))

list = ['Windows', 'Linux', 'Mac', 'Java', 'python', 'Angular', 'JavaScript']
upper = [words.upper() for words in list]
print(upper)
maximum = max(list)
print(maximum)
minimum = min(list)
print(minimum)
join_with = '-'
combined = join_with.join(upper)
print(combined)

dict = {'srikanth' : 87, 'suresh' : 92, 'ramesh' : 75, 'pavan' : 67, 'mahesh' : 98, 'vijay' : 55, 'nikhil' : 77}
highest = max(dict.values())
lowest = min(dict.values())
for key, val in dict.items():
    if val == highest:
        print(f'{key} has highest score of {val}')
    elif val == lowest:
        print(f'{key} has lowest score of {val}')

dict['vamsi'] = 99
print(dict)
dict.pop('suresh')
print(dict)
        
    