# Lab: vehicle factory with OOP
## Overview
---------------
Creating a `vehicle factory` with Object Oriented Programming.

## Configuration
------------------------

Use Python classes to model a `Factory`, `Car` , `Motorcycle` classes


1. Create a local git repo with root folder named `vehicleFactory`.
2. Create a new repo on Github called `vehicleFactory`.
3. Link your local and remote repositories
4. then set it up based on the following structure.

```
├── .venv
├── module_name
    ├── __init__.py
│   ├── factory.py
│   ├── motorcycle.py
│   ├── car.py
├── test
    ├── __init__.py
│   ├── test_module_name.py
├── .gitignore
├── README.md
Please make sure don't use the names as its here its just an example.
```
5- create a new branch and called it `oop1`.\
6. Work on a `oop1` branch.\
7. After completing the lab, create a PR from your `oop1` branch to `main` then merge your code.




## User story
------ 
a customer asked our company to create a system for his factory 
his factory is a vehicle factory that has two department 


1. **motorcycle department :** 
    where the customer can request a car with specific requirements 
    - the customer can choose the type of fuel , either (electric, petrol, diesel )
    - the customer can't choose a color for the motorcycle


2. **car department :**
    where the customer can request a car with specific requirements :
    - he can choose the color of the car 
    - he can choose a specific Brand 
    - he can choose the number of doors either (2 or 4 ) 
    - he can choose the type of fuel either (electric, petrol, diesel )



## Technical requirements
---------- 

- Car class and Motorcycle class belong to Factory class .
- we need to count how many cars and how many motorcycles were created overall .
- motorcycle class has attributes (number of wheels, model name, fuel type )

    - the number of wheels is 2 by default .
    - there is a method to change the model name
    - there is a method to change the fuel type , either (electric, petrol, diesel ) your method should guarantee that.
    - there is a method to print how many motorcycles have been created .

- car class has attributes (number of doors, model name, fuel type , color of the car ) : 
    - the number of wheels is 4 by default .
    - there is a method to change the model name.
    - there is a method to change the fuel type , either (electric, petrol, diesel ) your method should guarantee that.
    - there is a method to change the color of the car.
    - there is a method to change the number of doors either( 2 or 4 doors) your method should guarantee that .
    - there is a method to print how many cars have been created .


**General notes :**
- there is a method for reading any attribute.
- make sure to use `__str__` in both classes to print all the attributes that belong to the object .
- all the attributes should be protected 
- every class is a module 
- the common methods should be abstract methods in the parent class 

## Testing Requirements
------- 
add tests to your project and make sure you are covering all the cases 

## Submission instruction 
------

submit your pull request 