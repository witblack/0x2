import sys
import os

def __init__():
    Path = os.getcwd()
    sys.path.insert(1, Path)

__init__()

import update

update.update_url('https://github.com/razyar/0x2')
update.update_github()
