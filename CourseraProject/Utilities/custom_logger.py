import logging


#import


#new changes
class log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\khanacademy.log",format = "%(asctime)s:%(levelname)s:%(message)s",
                                     datefmt="%y-%m-%d%h:%m:%S",force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
