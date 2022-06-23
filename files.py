"""
The files "module" develeloped by _swtlcodes may be used if given credit.
Credit may be given by:
    1. Keeping this comment in the "module"
    2. Crediting with words.
This "module" is in its infancy, so don't expect it to be good.
This is the files module version 0.1.
"""

# This function can be used to find a specific character in a file and replace it with a character of your choice.
def findAndReplace(filePath,find,replace):
    editedList = []
    file = open(filePath)
    fileText = file.readlines()
    for lines in range(len(fileText)):  
        for chars in fileText[lines]:   
            if chars == find:
                editedList.append(replace)
            else:
                editedList.append(chars)
    newFile = ""
    for items in range(len(editedList)):
        newFile += editedList[items]
    file.close()
    return newFile
# This function can be used to find the path of a file.
def findFile(file,directory):
    import os
    os.system("cd "+directory)
    return os.system("where "+file)
# This function can run any file with python syntax as a .py file.
def runAsPy(file):
    ogFile = open(file,"r")
    # Reused code from the "findAndReplace" function
    fileText = ogFile.readlines()
    pyTextList = []
    for lines in range(len(fileText)):
        for chars in fileText[lines]:
            pyTextList.append(chars)
    pyTextList.insert(0,"    ")
    for items in range(len(pyTextList)):
        if pyTextList[items] == "\n":
            pyTextList.insert(items+1,"    ")
        else:
            continue
    pyText = ""
    for items in range(len(pyTextList)):
        pyText += pyTextList[items]
  
    pyText = "def run():\n" + pyText
    dummyFile = open("dummy.py","w")
    dummyFile.write(pyText)
    dummyFile.close()
    import dummy
    import os
    dummy.run()
    os.remove("dummy.py")
