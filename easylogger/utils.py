from datetime import datetime
def getTime():
    current_time = datetime.now()
    return current_time.strftime("%Y%m%d_%H%M%S")
    