from loggingontips.Logger import Logger
from loggingontips.LogLevels import LogLevel
l2=Logger()

def run():
    l2.log(LogLevel.INFO,'Is it working?')

if __name__=="__main__":
    run()