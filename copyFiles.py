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
    files.remove("")
    if returnError:
        return files, er
    else:
        return files


def fileDifference(file1, file2):
    grpCommand = "grep -v -f  {} {}".format(file1, file2)
    return subprocessToList(grpCommand)


def copyFilesInList(listIn, copyLocation):
    for element in listIn:
        shutil.copy2(element, copyLocation)


def appendListToFile(file, listWrite):
    with open(file, "a") as appender:
        for newEntry in listWrite:
            appender.write("\n" + newEntry)


dirOut = "sandbox/flattenSyncTest/B/"
copyList = "info/filesCopy"
excludeList = "info/excludeCopy"


newMoves = fileDifference(excludeList, copyList)
if len(newMoves) != 0:
    print("Moving files\n")
    copyFilesInList(newMoves, dirOut)
    print("Updating excludes list\n")
    appendListToFile(excludeList, newMoves)
    print("Finished\n")
else:
    print("Up to date, no moves.")
