# LAB-24: Django Models 2

Django has a powerful Object Relational Mapper that allows us to persist data using Python instead of SQL.

Today you'll build out a project with one model and wire up that model using Django Views.

## Steps

Please follow the below steps as an example.

1. Create a new repo on Github called `cars-project` , then set it up based on the following structure.

```text
├── .venv
├── car
    ├── migrations
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
├── car_project
    ├── __pycache__
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
├── templates
    ├── base.html
    ├── car_list.html
    ├── car_detail.html
├── static
    ├── style.css
├── media
├── db.sqlite3
├── manage.py
├── README.md
├── requirements.txt
├── .gitignore
```

2. Work on a `lab-24` branch.

3. After completing the lab, create a PR from your `lab-24` branch to `main` then merge your code.

## Lab Requirements

- design the car schema ( note that one car can have just one owner).

- create django project that called cars_project.

- create django app called car.

- you should have a Car model that containes (owner(FK),car_name , model, color,car_img, year_of_manufacture).

- regeister your model to admin.

- create two pages car list page and car details page.
  - Add templates folder in the root of project.
  - create a base.html template.
  - create car_list.html and car_detail.html that extends from base.html
  - add CarListView and CarDetailView.
  - add them to the app url.
  - include your urls in the project urls.

- car list page should have a url to car detail page.
- car list page should have a list of cars.
- car detail page should have all information about specific car.

- make sure to use django templeting language when adding the links.
- add styling
  - create static folder at root of project.
  - update STATICFILES_DIRS.
  - create base.css file which styles base.html elements.
  - load static css in base.html file.

## Testing Requirements

- make sure test extends TestCase instead of SimpleTestCase.

- test if car list page and car detail page are running will.

- status testing.

- template testing.
- use url name instead of hard coded path
TIP: django.urls.reverse will help with that.

## Submission Instructions

- Add the submission instructions
