from easylogger.Logger import Logger
from easylogger.LogLevels import LogLevel
l1=Logger()

def run():
    l1.log(LogLevel.DEBUG,'Is it working?')

if __name__=="__main__":
    run()