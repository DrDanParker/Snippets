###############################################################################
###
### Jup Convert
### This file is part of Snippets
### This file was created by Dr Daniel Parker 
###    Twitter: @DrDanParker     GitHub:https://github.com/DrDanParker 
###     
### Code adapted from Stack Overflow User CliffordVienna  
### Source: https://stackoverflow.com/a/23292713/6922652 
###
###############################################################################

import IPython.nbformat.current as nbf

def convertPy(file):
    nb = nbf.read(open(file, 'r'), 'py')
    (fileBaseName, fileExtension)=os.path.splitext(file_List[i])
    outfile = fileBaseName+'.ipynb'
    nbf.write(nb, open(outfile, 'w'), 'ipynb')
    print('File Converted to Jupyter: '+outfile)


file = input("prompt")
try:
    convertPy(file)
except:
    print('file not accepted')
