import sys
import searchMedia
import copyFiles
import cleanUp
from parseArguments import parseArguments

args = parseArguments()

### Main ###

pathMedia = args.inFile
# "sandbox/flattenSyncTest/A/" # "sandbox/raw_photos"

pathOutput = args.outFile
# "sandbox/flattenSyncTest/B/"

pathExtension = args.supportedFileTypes  # "info/includeExtensions"

excludeListFile = args.excludeFrom  # "info/excludeCopy"

tmpFile = args.tempFile  # "info/filesCopy"

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


# def main(some_args):
#    do_stuff...
#
# def parse_arguments():
#    argument_parse_code
#    return arguments
#
# if __name__ == '__main__':
#    arguments = parse_arguments()
#    main(*arguments)