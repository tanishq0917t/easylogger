from .LogLevels import LogLevel

class Logger:
    _instance = None
    _file = None

    def __new__(cls, log_file='app.log'):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize(log_file)
        return cls._instance

    def _initialize(self, log_file):
        if self._file is None:
            self._file = open(log_file, 'a')

    def log(self, level: LogLevel, message: str):
        log_entry = f"{level.name}: {message}\n"
        self._file.write(log_entry)
        self._file.flush()

    def close(self):
        if self._file:
            self._file.close()
            self._file = None
