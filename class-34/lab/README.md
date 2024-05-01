# LAB-01: Authentcation and Authorization

- in this lab, we will be building a  authentication system in django that will allow users to login and logout utilizing JWT

- you also have to dockerize your application

## Steps
1. Create a new repo on Github called `Django_auth` , then set it up based on the following structure.



```
├── README.md
├── requirements.txt
├── things_api
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── things
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── .gitignore
```



2. Work on a `lab-01` branch.
3. After completing the lab, create a PR from your `lab-01` branch to `main` then merge your code.
4. Deploy your server on Heroku from `main` branch.

## Lab Requirements
- build a django api that uses JWT authentication  
- create a custom user model
- add a new model of your choice (ex: `Thing`)



## Testing Requirements
- Add the testing requirements if applied


## Submission Instructions
- submit a link to your project `README.md` file

- add a pull request link to the readme file

