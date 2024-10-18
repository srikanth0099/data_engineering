# Question 1: List Manipulation and Conditionals
# You are given a list of integers. Write a function separate_and_sum(nums) that:

# Separates the list into two lists: one containing all the even numbers and the other containing all the odd numbers.
# Sums the values in both lists.
# Returns the larger sum along with the list (even or odd) that had the larger sum.
# If both sums are equal, return the even list and the sum.


def separate_and_sum(nums):
    even_numbers = [n for n in nums if n % 2 == 0]
    odd_numbers = [n for n in nums if n % 2 != 0]
    
    even_sum = sum(even_numbers)
    odd_sum = sum(odd_numbers)

    if even_sum == odd_sum:
        return even_sum, even_numbers
    elif even_sum >= odd_sum:
        return even_sum, even_numbers
    else:
        return odd_sum, odd_numbers


l = [1,2,3,4,5,6,7,8,9,10,11,20,35,47,68,93,62,98]
output = separate_and_sum(l)
print(f'Larger sum: {output[0]}')
print(f'List with larger sum: {output[1]}')
