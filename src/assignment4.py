# create a 9 elememts mixed tuple
# Access the third eleemnt and print
 # slice the tuple to retieve last 3 
# find the index of a aparticluar element
# count how many times eleemnt is repeated
# add new eleement to tuple

# research pack and upack of tuple

# craete 2 sets a and b 
# 4 operations union, intersection, difference ans symmetric difference
# remove duplicates, add new eleemnt, remove an existing element


t = ( 4, 7, 3.14, 'sri', True, 'apple', False, 88, 'Hello', 7)
print("Third element is: ", t[3])
print("The last 3 elements are:", t[-3::1])
print("Index of the element is:", t.index(True))
print("COunt of the element is: ", t.count(7))
tl = list(t)
tl.append('Hi')
t = tuple(tl)
print("Elements after adding new one: ", t)

# Packing of tuple
x = 2, 'Hello', True, 3.14
pt = tuple(x)
print("Packing of tuple: ", pt)
# Tuple Unpack
k,y,z,a = pt
print(k)
print(y)
print(z)
print(a)


a = {2,4,5,6,9,8,2}
b = {1,2,6,7,8,5}
print("Union of elements: ", a | b)
print("Intersection of elements: ", a & b)
print("Difference of elements: ", a - b)
print("Symmetric Difference of elements: ", a ^ b)

print(a)
print(b)

a.add(10)
print("Set after adding elements is: ", a)

a.remove(2)
print("Set after removing elements is: ", a)
