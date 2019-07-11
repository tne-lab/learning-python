# TNEL Python Tutorial

Using python for neuroscience

## Step 1 (by yourself)
### Setting up Python
Only for windows. Mac and Linux are good to go already.

Option 1) Install anaconda (has a bunch of very useful modules and programs built-in) (https://www.anaconda.com/distribution/)

Option 2) Install basic python (https://www.python.org/)

### Learn basic python
This may take a bit depending on your experience programming. learnpython.org looks like a very good starting point. I would work through the "Learn the Basics" and "Data Science Tutorials" as a first step. Make sure you understand for loops, dictionaries, arithmetic, and if/else statements. If you want some more help there are lots of other options too. Youtube, w3schools (only up to file handling), etc. If you have no programming experience an hour a day for a week should get you more than ready for our first project on Thursday.

There are also some phone apps that are really great if you're looking to learn while riding the bus!

### Setting up GitHub
- Create a github account. (DON'T USE UMN EMAIL!)

- If on windows or mac, download git (https://git-scm.com/downloads).

### Ensure Jupyter is installed
Open a jupyter notebook and open something like a simple helloworld.py file.

If you can't open jupyter. Open a command line window and type "python pip install jupyter" and try again. If you're struggling I would advise to just install anaconda.

### Download data from google drive
TNEL-UMN/Protocols and Tutorials/Python

Download folder OP7

Contact me (schat107@umn.edu) if you don't have access to our drive.

## Step 2 (With us)
### Setting up GitHub
- Open Git Bash

- Use commands "cd" (change directory) and "ls" (list) to change to where you want to save your files. i.e. "cd Documents"

- Create a new folder for GitHub "mkdir GitHub" (make directory), and go into it "cd GitHub".

- Now back to your browser and go to our github repository (https://github.com/tne-lab/learning-python). Click fork in the upper right corner. Then click on your account. This will make a private version for yourself.

- Now go to your private repo (https://github.com/CHANGETOYOURUSERNAME/learning-python) and copy the link from the green clone button.

- Back to git bash and type "git clone https://github.com/CHANGETOYOURUSERNAME/learning-python". This creates a local copy for yourself.

### Move data into working folder
Create a folder called data in learning-python folder. Copy folder OP7 into here.

### Open Main in juypter (in cmd line type: "jupyter notebook".  You should then see it open in your browser)
Start a juypter notebook and open up the main.ipynb file which is located in the folder that you cloned from github.

## Step 3
### Push your new changes to github so they will be backed up.
- Return to git bash and "cd" into your learning-python folder.

- Use the command "git add -A" to add all files to be staged to be commited.

- Use the command "git commit -m "My first commit"" to commit the changes. This means that these files are the most up to date changes.

- Use the command "git push" to push the files up your github repository so they will be saved both locally and in the cloud. Go to your github repo (https://github.com/CHANGETOYOURUSERNAME/learning-python) and make sure your new changes are there.
