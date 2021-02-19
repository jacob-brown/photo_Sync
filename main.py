import controllers as ctr
import logging
import logger
from parseArguments import parseArguments


def main(args):

    # initiate timer and logger
    timeKeeper = ctr.timer()
    timeKeeper.startTimer()
    logger.initiateLogging()

    # body of copying
    ctr.preRunCleaning(args)
    ctr.searchController(args)
    ctr.copyFileController(args)
    ctr.finalCleaning(args)

    # finish up
    timeEnd = timeKeeper.timeCheck()
    logging.info(timeEnd)
    logging.info("DONE")
    return 0


if __name__ == "__main__":
    main(parseArguments())
