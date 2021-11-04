import os
import shlex
import subprocess
import pandas as pd

os.chdir("C:\\Users\\Younes\\Desktop\\gnucash-android")
pa = 'G:\\gnu'
df = pd.read_csv('gnucash.csv', sep=';')
a = df.loc[~df.CommitHash.duplicated(keep='last')]
repo_Name = a['CommitHash']
b = repo_Name.to_frame(name=None)
print(b)

n = 800
for elem in b['CommitHash']:
    print(elem)
    path = pa+"//"+str(n)
    n += 1
    commande = 'git worktree add "%s" %s'
    commande = commande % (path, elem)
    args = shlex.split(commande)
    p = subprocess.Popen(args)
