print("Hi")
number = input()
print(number)

def sum(a,b):
    return a+b

print(sum(2,3))

x=10

# type hint
def fun_name(x:str,y:int)->str:
    """
    this is called a doc string
    this function accept 2 par str & int and 
    returns a string
    """
    print("finc1")
    # pass
    return("Hi")

print(fun_name("roaa",5))