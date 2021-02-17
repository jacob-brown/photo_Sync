import sys
import searchMedia
import copyFiles
import cleanUp
from timer import timer
from parseArguments import parseArguments

### Main ###
def main(args):

    timeKeeper = timer()
    timeKeeper.startTimer()

    ###
    # 0. Clean at start
    print("pre-run cleaning.")
    cleanUp.removeBlankLines(args.excludeFrom)

    ####
    # 1. run search media
    print("\nSearch")
    acceptedExtensions = searchMedia.openFileToTuple(args.supportedFileTypes)

    print("searching for files...")
    searchMedia.findContent(args.inFile, acceptedExtensions, args.tempFile)

    ####
    # 2. run copy files
    # when `dirOut=` etc. is removed it fails....
    print("\nCopy")
    copyFiles.copyController(
        dirOut=args.outFile,
        excludeList=args.excludeFrom,
        copyList=args.tempFile,
    )

    ####
    # 3. run clean-up
    print("\nClean-up")
    print("cleaning exclude list.")
    cleanUp.removeBlankLines(args.excludeFrom)
    print("removing temp files")
    cleanUp.removeFile(args.tempFile)

    timeKeeper.timeCheck()


if __name__ == "__main__":
    main(parseArguments())
