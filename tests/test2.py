from easylogger.Logger import Logger
from easylogger.LogLevels import LogLevel
l2=Logger()

def run():
    l2.log(LogLevel.INFO,'Is it working?')

if __name__=="__main__":
    run()