# write a program

# 1. len of string -> multiline SyntaxWarning
# 2. assign a multi line variable string and split it based on " "
# 3. concatinate first 5 words

a = '''Data engineering involves the design, construction, and management of systems that collect, store, and analyze data at scale. 
    It encompasses tasks such as data extraction, transformation, loading (ETL), and ensuring that data is structured, clean, 
    and available for analysis or machine learning.'''

print(len(a))
words = a.split(' ')
print(words)
print(len(words))
c = ' '
b = c.join(a.split(' ')[:5])
print(b)