def string_formatter(name:str,mark:int)->str:
    # return (f"congrats {name} you got {mark}% !")
    # return ("congrats {} you got {}".format(name,mark))
    return ("congrats %s you got %s"%(name,mark))

print(string_formatter("Ahmad",90))

x=10

if __name__ == "__main__":
    result = string_formatter("roaa",70)
    print(result)
    print("well done")
