# LAB-02: Modules, Testing And Recursion

This Lab will make you practice on modules and testing by write some functions and import them to another file to test them because as you learned today a module is a Python object with arbitrarily named attributes that you can bind and reference. Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

## Steps
- Please follow the below steps as an example.
 
1. Create a local git repo with root folder named `modules_and_testing`.
2. Create a new repo on Github called `modules_and_testing`.
3. Link your local and remote repositories
4. then set it up based on the following structure.
    
```module_testing
├── .venv
├── module_name
    ├── __init__.py
│   ├── name.py
├── test
    ├── __init__.py
│   ├── test_module_name.py
├── .gitignore
├── README.md

Please make sure don't use the names as its here its just an example.
```
5- create a new branch and called it `factorial`.\
6. Work on a `factorial` branch.\
7. After completing the lab, create a PR from your `factorial` branch to `main` then merge your code.


## Lab Requirements

- Create a file `factorial_module.py` and place it inside the factorial module that called `factorial_module`.
- Add a file `test_factorial.py`, place it inside `test` module and write your tests inside it.
+ Create two functions for `factorial`, this functions shuold take one parameter `n`, and the number must be positeve number. The functions must return the factorial of the `n` number.\
a. first one is called factorial_iterative it must use loop to get factorial.\
b. second one is called factorial_recursion it must use recursion to get factorial.\
<span style="background:#669933">Hint: </span> The factorial of a positive integer n is the product of all positive integers less than or equal to n.\
For example, `factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1`.







### stretch goal

2. Create a clumsy factorial function and called it clumsy that take one parameter and return the clumsy factorial of it.\
what is clumsy factorial:
We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations with multiply `*`, divide `/`, add `+`, and subtract `-` in this order.

For example, `clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1`.\
<span style="background:#669933">Hint :</span> However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.\
Additionally, the division that we use is floor division such that `10 * 9 / 8 = 90 / 8 = 11`.


## Testing Requirements
- Create a three test for factorial_iterative function.
- Create a three test for factorial_recursion function.
- Create a five test for clumsy function.


## Submission Instructions
- Submit your pull request.
- Tell us if you faced any issue.
- Tell us the time you used to solved the lab. 
- Ensure that your functions has a well-formed docstring.
- Ensure you have a `README.md` file that explain your lab. 