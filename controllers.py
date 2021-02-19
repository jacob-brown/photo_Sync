import sys
import searchMedia
import copyFiles
import cleanUp
import logger
import logging
from timer import timer


def preRunCleaning(args):
    logging.info("pre-run cleaning.")
    cleanUp.removeBlankLines(args.copyHistory)


def finalCleaning(args):
    logging.info("cleaning copy reference list.")
    cleanUp.removeBlankLines(args.copyHistory)

    logging.info("removing all temporary files")
    cleanUp.removeFile(args.tempFile)


def searchController(args):
    logging.info("searching for files")
    acceptedExtensions = searchMedia.openFileToInto(args.validExtensions, tuple)
    searchMedia.writeFoundContent(args.inDir, acceptedExtensions, args.tempFile)


def copyFileController(args):

    proceedWithCopy = searchMedia.checkFilesWereFound(args.tempFile)

    if proceedWithCopy:
        logging.info("files found")
        logging.info("copying files")
        filesMatchingExtensionsFound(args)
    else:
        logging.warning(
            "no files found in this directory, extensions did not match."
        )


def filesMatchingExtensionsFound(args):
    filesToCopy = copyFiles.fileDifference(args.copyHistory, args.tempFile)

    if len(filesToCopy) != 0:
        newFilesFoundCopyRequired(filesToCopy, args)
    else:
        logging.warning("directory appears up-to-date, no files were moved.")


def newFilesFoundCopyRequired(filesToCopy, args):
    logging.info("moving files")
    copyFiles.copyFilesInList(filesToCopy, args.outDir)

    successMove, failMove = copyFiles.returnSuccessAndFailedCopies(
        args.outDir, filesToCopy
    )

    logging.info("successfully copied: " + str(len(successMove)))
    logging.info("failed to copy: " + str(len(failMove)))

    if len(failMove) != 0:

        logging.error(
            logger.makeCopiedFileString("files failed to copy:", failMove)
        )

    appendSuccessesToExcludeList(args, successMove)


def appendSuccessesToExcludeList(args, successMove):
    logging.info("updating excludes list")
    copyFiles.appendListToFile(args.copyHistory, successMove)
    logging.info("finished")