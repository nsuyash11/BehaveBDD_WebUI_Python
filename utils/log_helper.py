import logging


def get_logger(caller, filename):
    logger = logging.getLogger(caller)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "%(asctime)s : %(name)s - %(funcName)s - %(lineno)s - %(levelname)s : %(message)s"
    )
    fh = logging.FileHandler("./logs/" + filename + ".log")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger


def remove_logfile_handler(logger):
    logger.handlers.clear()
