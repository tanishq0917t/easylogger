class InvalidFileException(Exception):
    def __init__(self, message="Invalid file extension. It should be .log"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"MyCustomException: {self.message}"
