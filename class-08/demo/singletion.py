class Singleton:

    _instance = None # class attr

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls) # calling super's __new__ to create new obj
        return cls._instance

# Test
obj1 = Singleton()
obj2 = Singleton()

if obj1 is obj2:
    print(obj1)
    print(obj2)
else:
    print(False)