#!/bin/bash

function gnit() {
    python create.py $1
    cd /home/imkaka/Documents/Projects/$1
    git init
    git remote add origin git@github.com:<your-github-username>/$1.git
    touch README.md
    git add .
    git commit -m ":tada: Initial commit"
    git push -u origin main
    code .
}
