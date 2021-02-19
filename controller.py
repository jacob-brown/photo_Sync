import sys
import searchMedia
import copyFiles
import cleanUp
import logger
import logging
from timer import timer
from parseArguments import parseArguments

### Main ###
def main(args):

    timeKeeper = timer()
    timeKeeper.startTimer()
    logger.initiateLogging()

    logging.info("pre-run cleaning.")
    cleanUp.removeBlankLines(args.excludeFrom)

    logging.info("searching for files")

    # if returns empty file, i.e. no files with the extensions where found
    searchMedia.searchController(
        args.supportedFileTypes, args.inFile, args.tempFile
    )

    # if up to date, i.e. no changes needed exit the program
    logging.info("copying files")
    newMoves = copyFiles.fileDifference(args.excludeFrom, args.tempFile)

    if len(newMoves) != 0:
        logging.info("Moving files")
        copyFiles.copyFilesInList(newMoves, args.tempFile)
        logging.info(logger.makeCopiedFileString(newMoves))
        # check move was successful 
        logging.info("Updating excludes list")
        copyFiles.appendListToFile(args.excludeFrom, newMoves)
        logging.info("Finished")
    else:
        logging.info("Up to date, no moves.")

    logging.info("Cleaning up")
    logging.info("cleaning exclude list.")
    cleanUp.removeBlankLines(args.excludeFrom)
    logging.info("removing temp files")
    cleanUp.removeFile(args.tempFile)

    timeEnd = timeKeeper.timeCheck()
    logging.info(timeEnd)
    logging.info("DONE")


if __name__ == "__main__":
    main(parseArguments())
