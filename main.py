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
    ######
    ### Clean
    #
    logging.info("pre-run cleaning.")
    cleanUp.removeBlankLines(args.excludeFrom)

    ######
    ### Search
    #
    logging.info("searching for files")

    searchMedia.searchController(
        args.supportedFileTypes, args.inFile, args.tempFile
    )

    ######
    ### Copy
    #
    proceedWithCopy = searchMedia.checkFilesWereFound(args.tempFile)

    if proceedWithCopy:

        logging.info("files found")
        logging.info("copying files")
        newMoves = copyFiles.fileDifference(args.excludeFrom, args.tempFile)

        if len(newMoves) != 0:
            logging.info("moving files")
            copyFiles.copyFilesInList(newMoves, args.outDir)

            # check move was successful
            successMove, failMove = copyFiles.returnSuccessAndFailedCopies(
                args.outDir, newMoves
            )

            logging.info("successfully copied: " + str(len(successMove)))
            logging.info("failed to copy: " + str(len(failMove)))

            if len(failMove) != 0:

                logging.error(
                    logger.makeCopiedFileString(
                        "files failed to copy:", failMove
                    )
                )

            logging.info("updating excludes list")
            copyFiles.appendListToFile(args.excludeFrom, successMove)
            logging.info("finished")

            ########
            ### What to do with failed copies?

        else:
            logging.warning(
                "directory appears up-to-date, no files were moved."
            )
    else:
        logging.warning(
            "no files found in this directory, extensions did not match."
        )

    ######
    ### Clean
    #
    logging.info("cleaning copy reference list.")
    cleanUp.removeBlankLines(args.excludeFrom)

    logging.info("removing all temporary files")
    cleanUp.removeFile(args.tempFile)

    ######
    ### Exit
    #
    timeEnd = timeKeeper.timeCheck()
    logging.info(timeEnd)
    logging.info("DONE")


if __name__ == "__main__":
    main(parseArguments())
