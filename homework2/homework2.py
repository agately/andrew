# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What's the difference between Git, GitHub, and Git Bash?

'''
Git tracks changes to your code
GitHub is a cloud platform that hosts Git repositories online. It allows you to you share your code with others, collaborate, and contribute to open-source.
Git Bash is a terminal to run Git commands
'''

# 2) What's the difference between the terminal and the command line?
'''
The interface where you type text commands for the computer to execute
The terminalis the application/window that lets you access the command line
'''

# 3) How does Windows PowerShell differ from Git Bash?

'''
PowerShell and Git Bash are command-line shells

Git Bash provides a Bash emulation layer
'''

# 4) What's the difference between Anaconda, conda, and Python?

'''
Python is the programming language itself and comes with the interpreter that runs your code

Conda is a tool used to manage packages and create isolated environments so you can keep different projects separate, and it can handle more than just Python packages.

Anaconda is a larger distribution that bundles Python, Conda, and many commonly used scientific and data science packages all in one, making it convenient for people working in fields like machine learning and scientific computing.

'''

# 5) What is VS Code? 

'''
VS code is an IDE
'''

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
'''
A Jupyter Notebook is an interactive document where you can write and run code (usually Python) alongside text, math equations, and visualizations.
JupyterLab, on the other hand, is like the “next generation” interface: it can open and manage multiple notebooks, terminals, text editors, and data files in one flexible workspace, almost like an IDE (Integrated Development Environment)
'''

# 7) What does ~/ mean?

"""
shorthand for your home directory
"""

# 8) What's the difference between an absolute path and a relative path?

'''
An absolute path and a relative path are two different ways of specifying the location of a file or directory in a filesystem

Absolute path starts from the root directory but relative path starts from your current working directory

Example of absolute path
/Users/droogately/python_decal_fall2025/andrew/homework2

Versus relative path
andrew/homework2

'''

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".

'''
absolute
/Users/droogately/python_decal_fall2025/andrew/course_assignments/homework2

relative
andrew/course_assignments/homework2

'''
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?

'''
cd ..
'''

# 11) What would rm ./ do in your current directory? (Don't try it!)

'''
delete your current directory
'''

# 12) What do the following commands do?
# git add stages changes (files you modified, created, or deleted) so that Git knows you want to include them in the next commit.
# git commit takes a “snapshot” of all staged changes and saves it to the local Git repository.
# git push sends your commits from your local repository to a remote repository

# 13) What's the difference between "git add ." and "git add <file>"?

'''
gid add <file> stages only that specific file 

gid add . stages all changes in the current directory and all subdirectories
'''

# 14) What do "git status" and "git log -1" do?
'''
git status shows the current state of your working directory and staging area

git log -1 shows the most recent commit
'''

# 15) What's the difference between cloning a repository and pulling from it?

'''
Cloning makes a complete copy of a remote repository

Pulling fetches new commits/changes from the remote repository and merges them into your local branch.
'''

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?

'''
f-string wasn't working
'''

# 17) What's a question you still have? What's something you're confused about?

# 18) Tell me a fun fact!
'''
There are more real numbers between 0 and 1 than there are natural numbers
'''

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)

print(12 % 5) # Prints: 2, the % operation gives you the remaineder of two numbers
