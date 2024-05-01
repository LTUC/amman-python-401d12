import re
def welcome ():
    """
    this function display a welcoming message to the user
    """
    
    print("""
          Welcome to CV generator programm :D 
       
          this program requires you to fill some inputs about you and 
          then make your CV
          
          """)

welcome()
with open('./cv.txt','r+') as file :
    x = file.read()
    words  = re.findall('{(.*?)}', x)
    cv = {}
    for word in words : 
        cv[word] = input(f'{word}: ')
    print(x.format(**cv))
    