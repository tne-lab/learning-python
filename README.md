# TNEL Python Tutorial

Using python for ephys data

## Step 1 (by yourself)
### Setting up Python
Only for windows. Mac and Linux are good to go already.

Option 1) Install anaconda (has a bunch of very useful modules and programs built-in) (https://www.anaconda.com/distribution/)

Option 2) Install basic python (https://www.python.org/)

### Learn basic python
This may take a bit depending on your experience programming. learnpython.org looks like a very good starting point. Lots of other options too. Youtube, w3schools (only up to file handling), etc.

## Step 2 (With us)
### Setting up GitHub
- Create a github account. (DON'T USE UMN EMAIL!)

- Download git (https://gitforwindows.org/).

- Open Git Bash

- Use commands "cd" (change directory) and "ls" (list) to change to where you want to save your files. i.e. "cd Documents"

- Create a new folder for GitHub "mkdir GitHub" (make directory), and go into it "cd GitHub".

- Now back to your browser and go to our github repository (https://github.com/tne-lab/learning-python). Click fork in the upper right corner. Then click on your account. This will make a private version for yourself.

- Now go to your private repo (https://github.com/CHANGETOYOURUSERNAME/learning-python) and copy the link from the green clone button.

- Back to git bash and type "git clone https://github.com/CHANGETOYOURUSERNAME/learning-python". This creates a local copy for yourself.

### Download data from google drive
TNEL-UMN/Protocols and Tutorials/Python

Copy folder OP7 into data folder within learning-python folder.

### Open Main in juypter
Start a juypter notdebook and open up the main.ipynb file which is located in the folder that you cloned from github.

Complete it.

## Step 3
### Push your new changes to github so they will be backed up.
- Return to git bash and "cd" into your learning-python folder.

- Use the command "git add -A" to add all files to be staged to be commited.

- Use the command "git commit -m "My first commit"" to commit the changes. This means that these files are the most up to date changes.

- Use the command "git push" to push the files up your github repository so they will be saved both locally and in the cloud. Go to your github repo (https://github.com/CHANGETOYOURUSERNAME/learning-python) and make sure your new changes are there.
