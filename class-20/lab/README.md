# LAB-20: Automation

- Today's lab you will help TA's at ASAC to take attendance by using the concept of automation in python based on Zoom reports.

## Steps

1. Create a new repo on Github called `automation` , then set it up based on the following structure.

```text

├── automation.ipynb

├── data.csv

```
2. Work on a `lab-20` branch.
3. Create lab's environment and activate it.
4. Install following packages:
   - ```pandas```
   - ```matplotlib```
   - ```Jinja2```
   - ```openpyxl``` 


3. After completing the lab, create a PR from your `lab-20` branch to `main` then merge your code.

## Lab Requirements

1. Read the data from the provided dataset => [Zoom report of the attendance](./new_report.csv).

2. Divide the data into DataFrame as you see fit.

3. Get the Students ID.

4. Calculate the sum of duration each student spend in the meeting based on their IDs.

5. In new column, specify the state of each student.

   - Student is **Present** if he/she attended the whole meeting or was late 10 minutes.

   - Student is **Late** if he/she was late 20 minutes.

   - Student is **Absent** if he/she was late more than 20 minutes.

6. Change a degree of cells' color depending on percentage of the attendance; to achieve that:

* Use HSV color to control lightness.

> Example:

![EXAMPLE](./degree%20of%20the%20color.PNG)

> Example:

![EXAMPLE](./Example%20of%20panads%20colors.PNG)

* You should convert HSV to hex color because pandas does not recognize HSV colors. Hint -> use ```matplotlib.colors```

* Save the result in excel sheet. 

## Submission Instructions

- Submit a link to the README.md from your assignment branch in D2L