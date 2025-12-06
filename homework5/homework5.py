# 1. Git vs. GitHub
# Git is a version control system that tracks changes to files locally.
# GitHub is an online platform that hosts Git repositories and lets you share them.

# 2. Terminal vs. Command Line
# The command line is a text-based interface for typing commands.
# The terminal is the program that provides access to the command line.

# 3. Local vs. Remote Repository
# A local repository is the copy of your project on your own computer.
# A remote repository is the copy stored on a server (like GitHub).

# 4. Version Control
# Version control is a system that records changes to files over time so you can track and revert them.

# 5. Staging Area
# The staging area is where Git stores changes that are marked to be included in the next commit.

# 6. git add
# `git add` adds changes in your working directory to the staging area.

# 7. git commit
# `git commit` saves the staged changes to the repository history with a message.

# 8. git push
# `git push` uploads your local commits to the remote repository.

# 9. git status
# `git status` shows the current state of the working directory and staging area.

# 10. git pull
# `git pull` fetches and merges changes from the remote repository into your local branch.

# 11. pwd
# `pwd` prints the path of the current working directory.

# 12. ls
# `ls` lists the files and directories in the current directory.

# 13. cd
# `cd` changes the current working directory.

# 14. nano
# `nano` opens a simple text editor in the terminal.

# 15. touch
# `touch` creates an empty file or updates the timestamp of an existing file.

# 16. mv
# `mv` moves or renames files and directories.

# 17. rm
# `rm` deletes files (and with options, directories).

# 18. cat
# `cat` prints the contents of a file to the terminal.


def checkDataType(value):
    return type(value).__name__

result = checkDataType(3.14)
print(result)

result = checkDataType(True)
print(result)



def evenOrOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

result = evenOrOdd(7)
print(result)
result = evenOrOdd(10)
print(result)

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
result = sumWithLoop(numbers)
print(result) 

def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list


def square(num):
    return num * num


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(sumWithLoop(numbers))

