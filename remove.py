import sys
from github import Github

TOKEN = '<your_github_token>'

def remove(repo_name):
    user = Github(TOKEN).get_user()
    try:
        repo = user.get_repo(repo_name)
    except Exception as e:
        print(f'{e} has occoured while fetching the repo.')
        return
    repo.delete()
    print(f'{repo_name} has been deleted from Github successfully.')

if __name__ == '__main__':
    try:
        repo_name = sys.argv[1]
        remove(repo_name)
    except IndexError:
        print("Provide Repo Name as command line argument.")
