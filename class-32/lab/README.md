# LAB-32: Django Custom Permission 

- you are required to do a CRUD app that have a custom permission so anyone who own the item he can update and delete it  

## Steps
1. Please follow the below steps as an example.
2. Create a new repo on Github and name it \<your project name> ,then set it up based on the following structure.
    
```text
.
├── things_project
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── things_app
    ├── __init__.py
    ├── __pycache__
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── permissions.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```
2. Work on a `lab-32` branch.
3. After completing the lab, create a PR from your `lab-32` branch to `main` then merge your code.


## Lab Requirements

- update your README with your name ,date and description of your project   
- you should do a CRUD app using restfullAPIs

- your model should contain the user as a foreign key 
- your list api can be viewed and edited by just authenticated people 
- do a custom permission (IsOwnerOrReadOnly) for your app
    - user can delete or update his own things 
    - user can not delete or update other user work 

- you should implement docker and docker compose in your app  
- your database should be set to be postgres 


## Testing Requirements

- test model
- test list api
- test auth required to view the list
- test your custom permission IsOwnerOrReadOnly


## Submission Instructions

- submit your PR link

- answer the following questions in the comment section 

    1) what is you reflection about the lab 
    2) how much time does it take you to finish the lab

