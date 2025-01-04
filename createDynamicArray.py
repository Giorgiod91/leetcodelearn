class DynamicArray:
    
    def __init__(self, capacity:int):
        if capacity >0:
            self.capacity = capacity
            self.array = [None] * capacity
            self.size  = 0

    def __str__(self):
        return f"DynamicArray(capacity={self.capacity}, size={self.size}, array={self.array})"



newArray = DynamicArray(7)
print(newArray)