class MyHashSet:

    def __init__(self):
        self.arr = [False] * 10001
        
        

    def add(self, key: int) -> None:
        self.arr[key] = key
        

    def remove(self, key: int) -> None:
        del self.arr[key]

    def contains(self, key: int) -> bool:
        if self.arr[key]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)