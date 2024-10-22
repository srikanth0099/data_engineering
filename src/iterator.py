# # An iterator in python is a  object that allows you to traverse through 
# # a collection like lists, tuples, sets and dictionaries.

# # The iterator implements following two methods:

# # 1. __iter__(): This method returns the iterator object itself
# # and it is called when an iterator is initialized.

# # 2. __next__(): This method returns the next value from the sequence.
# # When the iterator is exhausted, it raises a StopIteration exception.

# # ex:
# l=[1,2,3,4,5]
# # convert it into a iterator
# i=iter(l)
# # next() is used to iterate through list
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# #print(next(i))

# #The for loop actually creates an iterator object and executes the next() method for each loop.

# numbers = [10, 20, 30]
# iter_obj = iter(numbers)



# while True:
#     try:
#         # Get the next item
#         item = next(iter_obj)
#         print(item)
#     except StopIteration:
#         # If StopIteration is raised, break from the loop
#         break

# Key Points about Iterators:

#     Stateful: Iterators keep track of where they are in the iteration.




# tup = ('a', 'b', 'c', 'd', 'e')
 
# # creating an iterator from the tuple
# tup_iter = iter(tup)
 
# print("Inside loop:")
# # iterating on each item of the iterator object
# for index, item in enumerate(tup_iter):
#     print(item)
 
#     # break outside loop after iterating on 3 elements
#     if index == 2:
#         break
 
# # we can print the remaining items to be iterated using next()
# # thus, the state was saved
# print("Outside loop:")
# print(next(tup_iter))
# print(next(tup_iter))


#     Single-use: Once an iterator is exhausted (i.e., it raises StopIteration), it cannot be reused. You need to create a new iterator if you want to iterate again.
#     Memory-efficient: Iterators do not store the entire collection in memory; they generate each value only when requested. This makes them more memory efficient, especially for large data sets or infinite sequences.


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# #The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)