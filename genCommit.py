#!/usr/bin/python3

import subprocess
import os

os.chdir('/home/griffin/FakeCommitGraph')

subprocess.call(['git','pull'])
subprocess.call(['python3','genFakeFile.py'])
subprocess.call(['git','add','.'])
subprocess.call(['git','commit','-m','adding fake files ... again'])
subprocess.call(['git','push','origin','master'])
