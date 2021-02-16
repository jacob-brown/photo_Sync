import searchMedia
import copyFiles
import cleanUp

pathMedia = "sandbox/flattenSyncTest/A/"
# "sandbox/raw_photos"

pathOutput = "sandbox/flattenSyncTest/B/"
pathExtension = "info/includeExtensions"

excludeListFile = "info/excludeCopy"
tmpFile = "info/filesCopy"

###
# 0. Clean at start
print("pre-run cleaning.")
cleanUp.removeBlankLines(excludeListFile)

####
# 1. run search media
print("\nSearch")
acceptedExtensions = searchMedia.openFileToTuple(pathExtension)

print("searching for files...")
searchMedia.findContent(pathMedia, acceptedExtensions, tmpFile)

####
# 2. run copy files
# when `dirOut=` etc. is removed it fails....
print("\nCopy")
copyFiles.copyController(
    dirOut=pathOutput, excludeList=excludeListFile, copyList=tmpFile
)

####
# 3. run clean-up
print("\nClean-up")
print("cleaning exclude list.")
cleanUp.removeBlankLines(excludeListFile)
print("removing temp files")
cleanUp.removeFile(tmpFile)
