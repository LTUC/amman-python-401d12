# LAB-01: Books 

- you are required to make a page that display a list of books

## Steps
1. Please follow the below steps as an example.
2. Create a new repo on Github called `books-library` , then set it up based on django structue
    
```text
.
├── README.md
├── books
│   ├── __init__.py
│   ├── __pycache__
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── books_author
│   ├── __init__.py
│   ├── __pycache__
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── templates
    ├── base.html
    ├── home.html
    └── list_of_books.html
```
2. Work on a `lab-23` branch.
3. After completing the lab, create a PR from your `lab-23` branch to `main` then merge your code.


## Lab Requirements

- design the book schema ( note that one book can have just one author )

- create django project that called library

- create django app called book

- you should have a book model that containes (author(FK),title , description, rating , publish_date)

- regeister your model to admin 

- create two pages Home page and Book Page 

    a- create a base.html template
    b- create home.html and book_list.html that extends from base.html
    c- add HomePageView and BookListView
    d- add them to the app url 
    e- include your urls in the project jrls

- home page should have a url to book page 

- Book page should have a list of book and a nav to go to the home page 

- make sure to use django templeting language when adding the links


## Testing Requirements

- test if home page and list page are running will 
- status testing 
- tempate testing 

## Submission Instructions

- you should share your pull request link 

- answer the following questions in the comment section 

    1) what is you reflection about the lab 
    2) how much time does it take you to finish the lab
