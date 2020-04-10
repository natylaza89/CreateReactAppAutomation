from threading import Lock
import logging


class Logger:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if Logger.__instance is None:
            lock = Lock()
            with lock:
                if Logger.__instance is None:
                    Logger.__instance = super().__new__(cls, *args, **kwargs)
                    cls.__logger_init()
        return Logger.__instance

    @classmethod
    def __logger_init(cls):
        setattr(Logger.__instance, 'logger', logging.getLogger(__name__))
        setattr(Logger.__instance, 'formatter',
                logging.Formatter('[%(asctime)s]:[*%(levelname)s*]: %(name)s: %(message)s', "%H:%M:%S, %d/%m/%Y"))
        setattr(Logger.__instance, 'file_handler', logging.FileHandler("logger.log"))
        Logger.__instance.logger.setLevel(logging.ERROR)
        Logger.__instance.file_handler.setFormatter(Logger.__instance.formatter)
        Logger.__instance.logger.addHandler(Logger.__instance.file_handler)