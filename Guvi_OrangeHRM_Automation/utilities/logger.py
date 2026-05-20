import logging


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(
            filename="logs/orangehrm.log",
            format="%(asctime)s - %(levelname)s - %(message)s",
            level=logging.INFO
        )

        return logging.getLogger()