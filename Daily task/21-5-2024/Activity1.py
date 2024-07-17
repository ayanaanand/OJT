class IncrementingIterator:
    def __init__(self, start=0):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        current_value = self.current
        self.current += 1
        return current_value

iterator = IncrementingIterator()


print(next(iterator))
print(next(iterator))  
print(next(iterator))  
