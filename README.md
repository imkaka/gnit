# gnit
Automate the Project inatialization process for any brand new project.

What it does on the fly (see no magic!):
  - [x] Create and initialize git Project Repo locally
  - [x] Create Project Repo at github
  - [x] Add remote to local project.
  - [x] Create `README.md` file
  - [x] Add, commit & push `initial commit`.
  - [x] Open local project directory in `code`.

### Configurations

1. Clone the repo `git clone git@github.com:imkaka/imkaka.gnit.git`
2. `cd gnit`
3. `pip install -r requirements.txt`

* Update `TOKEN` with your github Token or you can use your `username` and `password` as `Github(username, password).get_user()` in `create.py` and `remove.py`.

* Update file path to your appropriate path. `/home/<username>/path/to/file/`.
* Update `.gnit.sh` to put your github username.

#### Temporarily
```terminal
$ source .gnit.sh
``` 
to make command gnit available on current shell session.

### OR

#### Install the .gnit.sh as permanent command.

* open  .bashrc 
> .bashrc file is located in your user directory

```terminal 
$ vi ~/.bashrc
```
* at end of the file add
```sh
source <path to .gnit.sh> 
Ex: source /home/imkaka/.gnit.sh
```
### Usage:
1. Initalize Project
```terminal 
$ gnit <project_name>
```
2. Remove any project repo from github:
```terminal
$ python remove.py <repo_name>
```