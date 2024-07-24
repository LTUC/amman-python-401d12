# LAB-26: Function Based Views

you have to make a image_project django project, rather than use a class based view you will learn how make the same functionality by function based view.

## Steps
1. Please follow the below steps as an example.
1. Create a new repo on Github called `Image-project` ,then set it up based on the following structure.
    
```text
.
├── README.md
├── image_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── images
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── templates
```
2. Work on a `lab-26` branch.
3. After completing the lab, create a PR from your `lab-26` branch to `main` then merge your code.

## Lab Requirements
- you should create a project called image_project
- create an app called image
- setup your app inside your project settings.py
- create your model (feel free to choose what fields you want to store)
- create your views (remember function based views)
- create an account in [pixabay](https://pixabay.com/api/docs/), figure out how you should handle it 😉
  - make the category query equal food.
- fetch the api and get the data
- store the data inside your model
- keep in mind you should store your data once (not every refresh)
- create a template to show the list of images, each image should display as a bootstrap card
- create a template to show details for specific image.
- use [bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) to style your project in interesting way 😎

## Testing Requirements
- Add the testing requirements if applied
-


## Submission Instructions
- Add the submission instructions