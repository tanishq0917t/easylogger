from loggingontips.Logger import Logger
from loggingontips.LogLevels import LogLevel
l1=Logger()

def run():
    for i in range(1000000):
        l1.log(LogLevel.DEBUG,'Working?')

if __name__=="__main__":
    run()