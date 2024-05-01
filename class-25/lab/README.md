# LAB-20: Django CRUD and Forms

In general CRUD means performing Create, Retrieve, Update and Delete operations on a table in a database.

## Steps and Requirements

*  Create a Django project and called cars_store.

*  Create a cars app.

* The cars app should have a  Car model that have these fields:
   - model field - (required)
   - brand field - (required)
   - price field - (required)
   - is_bought field- (required)
   - buyer_id field ( refer to a user) - (not required)
   - buy_time field - (not required)


- Create CarListView that extends appropriate generic view
associated url path is an empty string
- Create CarDetailView that extends appropriate generic view
associated url path is <int:pk>/
- Create CarCreateView that extends appropriate generic view
associated url path is create/
- Create CarUpdateView that extends appropriate generic view
associated url path is <int:pk>/update/
- Create CarDeleteView that extends appropriate generic view
associated url path is <int:pk>/delete/

- Add urls to support all views, with appropriate names.
- Add templates to support all views.
   - ListView template
      - card for every car, that contain the car-model, car-brand, and a button for the details
      - Create button

   - DetailsView template
      - Show all the properties 
      - Have two buttons
         - Delete
         - Update

   - CreateView template
      - Form to create a new Car

   - CarUpdateView template
      - Form to update a Car

   - CarDeleteView template
      - Confirmation message before delete
      - Button for delete

- Add navigation harder that links in appropriate locations to access all pages.
- Make all the necessary changes to project level files for project to run.
In other words, make it work

## Test
- Test all Views
- Test Model
   -   string representation
   -   all fields

## Submission Instructions

1. Create a new repo on Github called car-store
2. Work on a lab-01 branch.
3. After completing the lab, create a PR from your lab-25 branch to main then merge your code.
4. Submit the PR link