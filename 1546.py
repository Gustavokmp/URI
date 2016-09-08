import os
for fileName in os.listdir("."):
    os.rename(fileName, fileName.replace(fileName[4:], ".py"))
