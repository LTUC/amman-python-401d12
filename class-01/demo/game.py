"""
Let's create the shap guessing game...
- A list of shaps to guess
  - Each shap should be a dictionary(obj) with name and hints attributes
  - name is a string
  - hints is a list of strings
"""
shaps=[
    {
    'name':"rectangle",
    'hint':[
        "has 4 corners",
        "the sum of its corners is 360 degree, same value of the corners",
        "an example of it: a book"
    ]

},
{
    'name':"circle",
    "hint":[
        "no cornars",
        "rounded",
        "an exmaple of it: an apple pie"
        ]
},
{
    'name':"triangle",
    "hint":[
        "3 corners",
        "the sum of its corners is 180 degree",
        "an exmaple of it: Egypt Pyramid"
        ]
}

]

def guess_the_shap(attempts):
    shap = shaps[attempts]
    answer = shap['name']
    guess=input("let's geuss a shape ???")
    hints=shap['hint']

    while len(hints):

        if guess == answer:
            break
        else:
            hint=hints.pop(0)
            print("sorry, but here is a hint %s"%hint)
            guess=input("let's geuss a shap ??")
    
    if guess.lower() == answer:
        print("Bravooo")
    else : 
        print(f'sorry bad answer, the correct answer is {answer}')







    

if __name__=="__main__":
    attempts=0
    response=input("do you want to play (y,n)")

    while response != 'n':
        guess_the_shap(attempts)
        attempts +=1

        if attempts> len(shaps)-1:
            break




