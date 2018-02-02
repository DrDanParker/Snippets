
# coding: utf-8

# In[ ]:


###############################################################################
###
### Path Loader
### This file is part of Snippets
### This file was created by Dr Daniel Parker 
###    Twitter: @DrDanParker     GitHub:https://github.com/DrDanParker 
###     
### Code adapted from Stack Overflow User Droogans  
### Source: https://stackoverflow.com/a/10038074/6922652
###
###############################################################################

import sys, os.path, pprint

def all_from(folder='', abspath=None):
    """add all dirs under `folder` to sys.path if any .py files are found.
    Use an abspath if you'd rather do it that way.

    Uses the current working directory as the location of using.py. 
    Keep in mind that os.walk goes *all the way* down the directory tree.
    With that, try not to use this on something too close to '/'

    """
    add = set(sys.path)
    if abspath is None:
        cwd = os.path.abspath(os.path.curdir)
        abspath = os.path.join(cwd, folder)
    for root, dirs, files in os.walk(abspath):
        
        for f in files:
            (fileBaseName, fileExtension)=os.path.splitext(f)
            if fileExtension == '.ipynb':
                add.add(root)
                break
            elif fileExtension == '.py':
                add.add(root)
                break
    for i in add: sys.path.append(i)


# In[ ]:


all_from('py') #if in ~, /home/user/py/
pprint.pprint(sys.path)

