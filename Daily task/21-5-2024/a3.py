class IncrementingIterator:
    def __init__(self, start=0, limit=10):
        self.current = start
        self.limit = limit
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        current_value = self.current
        self.current += 1
        return current_value


iterator = IncrementingIterator(start=0, limit=10)


for value in iterator:
    print(value)
