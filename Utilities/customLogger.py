# import logging
import logging
import logging.handlers


class LogGen:
    @staticmethod
    def loggeen():
        logging.basicConfig(filename="Logs/Automation.log", format='%(asctime)s- %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', filemode='w')

        logger = logging.getLogger()
        # logger.addHandler(rotate_file)
        logger.setLevel(logging.INFO)
        return logger
