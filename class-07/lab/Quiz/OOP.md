# OOP

1. What is an abstract class?

- [ ] An abstract class is the name for any class from which you can instantiate an object.
- [ ] Abstract classes must be redefined any time an object is instantiated from them.
- [ ] Abstract classes must inherit from concrete classes.
- [x] An abstract class exists only so that other "concrete" classes can inherit from the abstract class.

2. What statement about static methods is true?

- [ ] Static methods are called static because they always return `None`.
- [ ] Static methods can be bound to either a class or an instance of a class.
- [x] Static methods serve mostly as utility methods or helper methods, since they can't access or modify a class's state.
- [ ] Static methods can access and modify the state of a class or an instance of a class.

3. What are attributes?

- [ ] Attributes are long-form version of an `if/else` statement, used when testing for equality between objects.
- [x] Attributes are a way to hold data or describe a state for a class or an instance of a class.
- [ ] Attributes are strings that describe characteristics of a class.
- [ ] Function arguments are called "attributes" in the context of class methods and instance methods.


4. What is the correct syntax for defining a class called Game, if it inherits from a parent class called LogicGame?

- [x] `class Game(LogicGame): pass`
- [ ] `def Game(LogicGame): pass`
- [ ] `def Game.LogicGame(): pass`
- [ ] `class Game.LogicGame(): pass`

5. What is the correct syntax for defining a class called "Game", if it inherits from a parent class called "LogicGame"?

- [ ] `class Game.LogicGame(): pass`
- [ ] `def Game(LogicGame): pass`
- [x] `class Game(LogicGame): pass`
- [ ] `def Game.LogicGame(): pass`


6. What is the purpose of the "self" keyword when defining or calling instance methods?

- [ ] `self` means that no other arguments are required to be passed into the method.
- [ ] There is no real purpose for the `self` method; it's just historic computer science jargon that Python keeps to stay consistent with other programming languages.
- [x] `self` refers to the instance whose method was called.
- [ ] `self` refers to the class that was inherited from to create the object using `self`.

**Simple example**

```python
class my_secrets:
    def __init__(self, password):
        self.password = password
        pass
instance = my_secrets('1234')
instance.password
>>>'1234'
```

7. What is an instance method?

- [x] Instance methods can modify the state of an instance or the state of its parent class.
- [ ] Instance methods hold data related to the instance.
- [ ] An instance method is any class method that doesn't take any arguments.
- [ ] An instance method is a regular function that belongs to a class, but it must return `None`.

8. Which statement does NOT describe the object-oriented programming concept of encapsulation?

- [ ] It protects the data from outside interference.
- [ ] A parent class is encapsulated and no data from the parent class passes on to the child class.
- [ ] It keeps data and the methods that can manipulate that data in one place.
- [x] It only allows the data to be changed by methods.


9. What is the correct syntax for instantiating a new object of the type Game?

- [ ] `my_game = class.Game()`
- [ ] `my_game = class(Game)`
- [x] `my_game = Game()`
- [ ] `my_game = Game.create()`


10. What is the purpose of the `pass` statement in Python?

- [ ] It is used to skip the `yield` statement of a generator and return a value of None.
- [x] It is a null operation used mainly as a placeholder in functions, classes, etc.
- [ ] It is used to pass control from one statement block to another.
- [ ] It is used to skip the rest of a `while` or `for loop` and return to the start of the loop.

11. What is the correct syntax for calling an instance method on a class named Game?

_(Answer format may vary. Game and roll (or dice_roll) should each be called with no parameters.)_

- [x]

```python
>>> dice = Game()
>>> dice.roll()
```

- [ ]

```python
>>> dice = Game(self)
>>> dice.roll(self)
```

- [ ]

```python
>>> dice = Game()
>>> dice.roll(self)
```

- [ ]

```python
>>> dice = Game(self)
>>> dice.roll()
```


12. What is the definition of abstraction as applied to object-oriented Python?

- [ ] Abstraction means that a different style of code can be used, since many details are already known to the program behind the scenes.
- [x] Abstraction means the implementation is hidden from the user, and only the relevant data or information is shown.
- [ ] Abstraction means that the data and the functionality of a class are combined into one entity.
- [ ] Abstraction means that a class can inherit from more than one parent class.


13. Suppose a Game class inherits from two parent classes: BoardGame and LogicGame. Which statement is true about the methods of an object instantiated from the Game class?

- [ ] When instantiating an object, the object doesn't inherit any of the parent class's methods.
- [ ] When instantiating an object, the object will inherit the methods of whichever parent class has more methods.
- [ ] When instantiating an object, the programmer must specify which parent class to inherit methods from.
- [x] An instance of the Game class will inherit whatever methods the BoardGame and LogicGame classes have.

14. What does a class's `init()` method do?

- [ ] The `__init__` method makes classes aware of each other if more than one class is defined in a single code file.
- [ ] The`__init__` method is included to preserve backwards compatibility from Python 3 to Python 2, but no longer needs to be used in Python 3.
- [x] The `__init__` method is a constructor method that is called automatically whenever a new object is created from a class. It sets the initial state of a new object.
- [ ] The `__init__` method initializes any imports you may have included at the top of your file.

**Example:**

```python
class test:
    def __init__(self):
        print('I came here without your permission lol')
        pass
t1 = test()
>>> 'I came here without your permission lol'
```

15. What statement about the class methods is true?

- [ ] A class method is a regular function that belongs to a class, but it must return None.
- [x] A class method can modify the state of the class, but they can't directly modify the state of an instance that inherits from that class.
- [ ] A class method is similar to a regular function, but a class method doesn't take any arguments.
- [ ] A class method hold all of the data for a particular class.


16. Why would you use a decorator?

- [ ] A decorator is similar to a class and should be used if you are doing functional programming instead of object oriented programming.
- [ ] A decorator is a visual indicator to someone reading your code that a portion of your code is critical and should not be changed.
- [x] You use the decorator to alter the functionality of a function without having to modify the functions code.
- [ ] An import statement is preceded by a decorator, python knows to import the most recent version of whatever package or library is being imported.