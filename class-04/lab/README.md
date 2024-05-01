# LAB-04: CV Generator

In this lab assignment you will be creating a command line application which takes advantage of Python's built in capabilities for reading and writing files.

- You will have a [text cv template](https://github.com/LTUC/asac-advanced-python-guide-2/blob/class04-FileIO-Exceptions/material/class-04/lab/cv_template.txt), you should fill this template and update it with the necessary data from a user


## Resources
- [starter test script](https://github.com/LTUC/asac-advanced-python-guide-2/blob/class04-FileIO-Exceptions/material/class-04/lab/test_cv_generator.py)  is supplied and should be moved to your application's tests folder.
NOTE: All included tests must pass as written.
though you can add more tests if you like.
- [Python String format() Method](https://www.w3schools.com/python/ref_string_format.asp)
- [Unpacking Arrays](https://realpython.com/python-kwargs-and-args/#unpacking-with-the-asterisk-operators)

## Steps
1. Please follow the below steps as an example.
1. Create a new repo on Github called `CV-generator` , then set it up based on the following structure.
    
```text
├── .venv
├── assets
    ├── cv_template.txt
├── cv_generator
│   ├── cv_generator.py
    |──__init__.py
├── test
│   ├── test_cv_generator.py
    |──__init__.py
├── .gitignore
├── README.md
```
2. Work on a `lab-04` branch.
3. After completing the lab, create a PR from your `lab-04` branch to `main` then merge your code.


## Lab Requirements
## Feature Tasks and Requirements
- Create a file called cv_generator.py at root of cv_generator folder, which will contain all of the Python code.
Keeping in mind the concept of Single Responsibility Principle{:target="_blank"}, build a command line tool which will perform the following:
- Print a welcome message to the user, explaining the CV generator  and command line interactions.
- Read a template cv_generator file, and parse that file into usable parts.
- Prompt the user to submit a series of words to fit each of the required components of the CV template.
With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
- After the resulting CV has been completed, provide the completed response back to the user in the command line.
- Write the completed text to a new file on your file system (Example: cv_output.txt).

Note: A smaller example file(personal_summary.txt) is included as well which can be handy when developing/testing.

## Testing Details

- Create and test a read_template function that takes in a path to text file and returns a stripped string of the file's contents.
- read_template should raise a FileNotFoundError if path is invalid.
- Create and test a parse_template function that takes in a template string and returns a string with language parts removed and a separate tuple of those language parts.
- Create and test a merge function that takes in a text and a list of user entered language parts, and returns a string with the language parts inserted into the template.

## Stretch Goal

Figure a way to verify/validate terminal input/output.

## Submission Instructions
- Submit a link to the README.md from your assignment branch in D2L
- you should share your pull request link
- answer the following questions in the comment section
   - what is you reflection about the lab
   - how much time does it take you to finish the lab
