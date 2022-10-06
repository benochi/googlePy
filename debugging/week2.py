#!/usr/bin/env python
from multiprocessing import Pool
import os
import subprocess

src = "/home/student-03-5421ad70b5d7/data/prod/"
dirs = next(os.walk(src))[1]

def backup(dirs):
    dest = "/home/student-03-5421ad70b5d7/data/prod_backup"
    subprocess.call(["rsync", "-arq", src+'/'+ dirs, dest])

p = Pool(len(dirs))
p.map(backup, dirs)

#!/usr/bin/env python
from multiprocessing import Pool
import os
import subprocess

src = "/home/student-03-5421ad70b5d7/data/prod/"
dirs = next(os.walk(src))[1]

def backup(dirs):
    dest = "/home/student-03-5421ad70b5d7/data/prod_backup"
    subprocess.call(["rsync", "-arq", src+'/'+ dirs, dest])

p = Pool(len(dirs))
p.map(backup, dirs)

