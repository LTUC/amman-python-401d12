# LAB-29: Django REST Framework & Docker
Learn how you can use Django REST Framework to create API and containerize it with Docker
## Steps and Requirements
### Django Part
*  Create a Django project and called cars_store.
*  Create a cars_api app.
* The cars app should have a  Car model that have these fields:
   - model field - (required)
   - brand field - (required)
   - price field - (required)
   - is_bought field- (required)
   - buyer_id field ( refer to a user) - (not required)
   - buy_time field - (not required)
   
* Use REST Framework to create CRUD system.
* base api uel: /api/v1/car_store

### Docker Part
- NOTE Refer to the class demo for built out Dockerfile and docker-compose.yml examples.
- Update Dockerfile and docker-compose.yml if needed.
## Test
- No tests
## Submission Instructions
1. Create a new repo on Github called car-store
2. Work on a lab-29 branch.
3. After completing the lab, create a PR from your lab-29 branch to main then merge your code.
4. Submit the PR link