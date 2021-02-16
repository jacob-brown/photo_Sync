import subprocess
import os
import shutil


def subprocessToList(command, returnError=False):
    """ wrapper for a subprocess command """
    p = subprocess.Popen(
        [command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    out, er = p.communicate()
    out_string = out.decode()
    files = out_string.replace("\t", ":").split("\n")
    if "" in files:
        files.remove("")

    if returnError:
        return files, er
    else:
        return files


def isFileEmpty(file):
    header = subprocessToList("head -5 " + file)
    return not bool(header)


def copyFilesInList(listIn, copyLocation):
    for element in listIn:
        shutil.copy2(element, copyLocation)


def appendListToFile(file, listWrite):
    with open(file, "a") as appender:
        for newEntry in listWrite:
            appender.write("\n" + newEntry)


def fileDifference(file1, file2):
    if isFileEmpty(file1):
        catCommand = "cat {}".format(file2)
        return subprocessToList(catCommand)
    else:
        grepCommand = "grep -v -f {} {}".format(file1, file2)
        return subprocessToList(grepCommand)


dirOut = "sandbox/flattenSyncTest/B/"
excludeList = "info/excludeCopy"
copyList = "info/filesCopy"
# grep -v -f info/excludeCopy info/filesCopy
# grep -v -F -x -f info/excludeCopy info/filesCopy
newMoves = fileDifference(excludeList, copyList)

if len(newMoves) != 0:
    print("Moving files\n")
    copyFilesInList(newMoves, dirOut)
    print("Updating excludes list\n")
    appendListToFile(excludeList, newMoves)
    print("Finished\n")
else:
    print("Up to date, no moves.")
