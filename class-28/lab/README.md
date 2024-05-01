# LAB-28: CRUD Books Shop 

- you are required to make the previous `lab 23` as CRUD app and deploy it using docker

## Steps
1. Please follow the below steps as an example.
2. Create a new repo on Github called `CRUD-books-shop` , then set it up based on django structue
    
```text
.
├── Dockerfile
├── README.md
├── book_shop_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── book
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── template
    ├── base.html
    ├── book-create.html
    ├── book-delete.html
    ├── book-detail.html
    ├── book-list.html
    ├── book-update.html
    └── home.html
```
2. Work on a `lab-28` branch.
3. After completing the lab, create a PR from your `lab-28` branch to `main` then merge your code.


## Lab Requirements

- convert your previous `lab-23` into a CRUD app and deploy it using docker

- create django project that called book_shop_project

- create django app called book

- you should have a book model that containes (author(FK),title , description, rating , publish_date)


- create a CRUD views from the `book model` 
    - note that each view should have its own template

- templates:
    - home page: should have a url into the list page
    - list page: should list all the books (each book title should be a link into the book detail page) and have a button to create a new book
    - detail page: should have the details for a certain book and have 2 buttons one for update the book and another for delete the book 
        - update the book: should redirect you to the details page again
        - delete the book: should redirect you to the list page

- create the `requirements.txt` by this `pip freeze > requirements.txt`
- add a `Dockerfile` and `docker-compose.yml` into your project. notice that those 2 files should be as the same level as your django project

```text
Dockerfile content

FROM python:3
ENV BUILDKIT_PROGRESS=plain
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```

```text
docker-compose file content

version: "3.9"
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
```
- add a beautifull style into your project <span style="color:yellow">Amaze Us 😎</span>


## Testing Requirements

- test all the CRUD views.

## Submission Instructions

- you should share your pull request link 

- answer the following questions in the comment section 

    1) what is you reflection about the lab 
    2) how much time does it take you to finish the lab
