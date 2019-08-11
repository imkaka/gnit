import sys
import os
from github import Github

path = "/home/<your_username>/Documents/Projects/"

TOKEN = 'your github token'

def create(folderName):
    os.makedirs(path + folderName)

    user = Github(TOKEN).get_user()
    repo = user.create_repo(folderName)
    
    print("Succesfully created repository {}".format(folderName))

if __name__ == "__main__":
    try:
        folderName = sys.argv[1]
        create(folderName)
    except IndexError:
        print('Input Project name in command line.')