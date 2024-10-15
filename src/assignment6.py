numbers=[3,1,4,1,5,9,2,6,5,1,3,5,2,5]
print(numbers)
print(type(numbers))

numbers.append(7)
print(numbers)

numbers.remove(1)
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.insert(3,8)
print(numbers)


# Factorial
def factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r

print(factorial(4))

# Palindrome
def palindrome(s):
    s=str(s).lower()
    return s==s[::-1]

print(palindrome('Racecar'))