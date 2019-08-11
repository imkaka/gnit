from github import Github
from create import TOKEN

imkaka = Github(TOKEN)

for repo in imkaka.get_user().get_repos():
    print(repo.name)