from easylogger.Logger import Logger
from easylogger.LogLevels import LogLevel
l1=Logger()

def run():
    for i in range(100000):
        l1.log(LogLevel.DEBUG,'Working?')

if __name__=="__main__":
    run()