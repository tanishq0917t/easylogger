import threading
import os
from time import sleep
from loggingontips.LogLevels import LogLevel
from loggingontips.Logger import Logger


def test_thread_safe_log():
    log_file = "test_thread_safe_log.log"
    if os.path.exists(log_file):
        os.remove(log_file) 

    logger = Logger(log_file=log_file)

    def worker(thread_id):
        for i in range(100):
            logger.thread_safe_log(LogLevel.INFO, f"Thread-{thread_id} log message {i}")

    threads = []
    for thread_id in range(15):
        thread = threading.Thread(target=worker, args=(thread_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    logger.close()

if __name__ == "__main__":
    test_thread_safe_log()
