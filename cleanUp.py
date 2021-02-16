import os
import subprocess


def removeTempFiles():
    os.remove("info/filesCopy")


# remove spaces from excludeCopy
def removeBlankLines(file):
    tmpBasename = os.path.basename(file)
    fileDir = os.path.dirname(file)
    tmpFile = os.path.join(fileDir, "tmp_" + tmpBasename)

    with open(file, "r") as reader:
        with open(tmpFile, "w") as writer:
            for line in reader:
                if line != "\n":
                    writer.write(line)
    os.replace(tmpFile, file)


removeBlankLines("info/excludeCopy")
