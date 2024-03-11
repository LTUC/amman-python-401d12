# Get Started with Python

- Complete the [Python for Beginners](https://learn.microsoft.com/en-us/training/paths/beginner-python/) training course.
    - Step by step directions for installing Python for Windows, Mac and Linux are included.
    - **NOTE:** Windows users should install for Windows, **NOT** WSL/Linux.

## Windows Users - Leaving WSL Behind

**NOTE:** These steps are for Windows users only.

Windows Subsystem for Linux (WSL) will **NOT** be used in Python 401. This will make many things easier but will require a couple changes to use Windows native tools.

There aren’t too many changes needed. Give them a shot and reach out to instructional team if you run into any issues.

### GitBash

- You will switch to using GitBash for your terminal instead of Ubuntu shell.
    - GitBash “emulates” the unix environment so it will feel like the Ubuntu shell.
    - GitBash is bundled in when you install Git.
    - To access GitBash enter `GitBash` in Windows search bar at bottom of screen.
        - You can optionally add GitBash to dock for easy access.
    - From here on out `terminal` means `GitBash` unless explicitly told otherwise.

### Git

- [Git for Windows](https://git-scm.com/download/win)
    - Choose the first link that says `Click here to download`
    - Run the installer and click ‘Next’ for each prompt. Keep the default options selected on all screens **EXCEPT** the prompt titled `Choosing the default editor used by Git`.
        - On that screen, click the dropdown menu and choose Use `Visual Studio Code as Git’s default editor`.
    - When done installing Git, open a new terminal window and enter `git --version`
    - You should get something close to `git version 2.43.0.windows.1`
    - If you don’t then reach out to instructional team.

- [GitHub CLI](https://cli.github.com/)
    - Click `Download for Windows` button.
    - Run the installer with default options.
    - Once installation complete, open a new terminal window and type `gh --version`
        - You should get something close to `gh version 2.40.1 (2023-12-13)`
        - If you don’t then reach out to instructional team.

    - Authorize Github CLI
        - In terminal enter `gh auth login`
        - Select `Github.com`
        - Select `HTTPS`
        - Choose `Y` to authenticate using GitHub credentials.
        - Choose `Login with a web browser`
        - Follow the instructions to copy code and enter it a github.com
        - Authorize GitHub CLI’s request by clicking `Authorize GitHub` button at bottom of screen.
        - Confirm Access if using Multi Factor Authentication.

## STRETCH
Creat an account at [Exercism](https://exercism.org/) and begin the [Python track](https://exercism.org/tracks/python).

## Submission Instructions
Submit your thoughts on these prompts in the assignment’s text field in Canvas.

List any features of Python that you like/dislike most so far.
List some of the ways that Python is similar and different to JavaScript.