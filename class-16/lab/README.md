# ServerLess Functions

Serverless is a deployment architecture where servers are not explicitly provisioned by the deployer. Code is instead executed based on developer-defined events that are triggered, for example when an HTTP POST request is sent to an API a new line written to a file.

## Steps
1. Create a new repository on Github called `questions-competition`.
2. Sign up to Vercel [Link](https://vercel.com/).
3. link your github repo on Vercel.
4. Work on a `serverless-lab` branch.
5. After completing the lab, create a PR from your `serverless` branch to `main` then merge your code.
6. Use requests library to interact with REST Countries API [link](https://opentdb.com/api_config.php).

## Lab Requirements
1. Create folder called `api` that have your serverless functions file.
2. Create file called questions that handel your serverless functions.
3. Create a serverless function following Vercel's get-started directions that handles two kinds of queries:
a. The serverless function should handle a GET http request with a given questions from our api.
- E.g./questions?amount=20 should generate an http response that given 20 questions with them answers and every question must be in new line.
- E.g./questions?amount=51 should handle a GET http request with a given the maximum questions that your api given.\
b. The serverless function should handle a GET http request with a given 10 questions depends on category.
- E.g./questions?category=21 should generate an http response that given 10 question of Sports category and don't forget to display the name of category and every question must be in new line.
- E.g./questions?category=33 should generate an http response that given 10 `You have just 32 category`.

## Testing Requirements
- Add five deployed links `versel-link` to your README.md that given difference response.
- Two of them depends on amount.
- Two of them depends on category.
- The last must be without any query.


## Submission Instructions
- Your PR link.
- Your README link.
- Tell us how mush time you needed to solve this lab.