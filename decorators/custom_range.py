class CustomRange:
    def __iter__(self):
        return self
     
    def __init__(self, start, end = None, step=1):
        if end is None:
            self.start = 0
            self.end = start
        else:
            self.start = start
            self.end = end
        self.step = step
        self.current = self.start


    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or (self.step < 0 and self.current <= self.end):
            raise StopIteration
        current_value = self.current
        self.current += self.step
        return current_value


for i in CustomRange(5): 
    print(i)

print("--------------------------------")

for i in CustomRange(3, 15, 2):
    print(i)

print("--------------------------------")

for i in CustomRange(13, 3, -2):
    print(i)