#!/usr/bin/env python
import os

os.system('git add --all')
os.system('git commit -m "Auto commit by python"')
os.system('git remote show')
listRepos = os.popen('git remote show').read().split()
for repo in listRepos:
	os.system(f'git push {repo} --all')


