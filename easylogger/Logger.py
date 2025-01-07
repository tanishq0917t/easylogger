import os
from .LogLevels import LogLevel
from .utils import getTime

class Logger:
    __instance = None
    __file = None
    __log_file = None
    __max_file_size = 100*1024
    __last_time=None

    def __new__(cls, log_file='app.log', max_file_size=None):
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
            cls.__instance.__initialize(log_file, max_file_size)
        return cls.__instance

    def __initialize(self, log_file, max_file_size):
        self.__log_file = log_file
        if max_file_size is not None:
            self.__max_file_size = max_file_size
        self.__last_time=getTime()
        self.__open_log_file()

    def __open_log_file(self):
        if self.__file is None:
            self.__file = open(self.__log_file, 'a')

    def __rotate_file(self):
        self.__file.close()
        # Code to rotate the file starts here
        backup_name=f"{self.__log_file}_{self.__last_time}"
        if os.path.exists(self.__log_file):
            os.rename(self.__log_file, backup_name)
            self.__file=None
        # Code to rotate the file ends here
        self.__open_log_file()

    def log(self, level: LogLevel, message: str):
        if self.__file.tell() >= self.__max_file_size:
            self.__rotate_file()
        log_entry = f"{level.name}: {message}\n"
        self.__file.write(log_entry)
        self.__file.flush()

    def close(self):
        if self.__file:
            self.__file.close()
            self.__file = None
