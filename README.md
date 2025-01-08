# LoggingOnTips

`loggingontips` is a Python package that simplifies logging setup and configuration. It eliminates the need for manual handling by allowing users to configure various logging parameters effortlessly, such as log file names and file rotations based on timestamps, file size, or the number of logs.

## Features

- **Customizable Logging**: Set log file names and configure rotation settings with ease.
- **File Rotation**:
  - By timestamp.
  - By file size. (By default)
  - By number of logs.
- **Synchronous Logging**: Fully supported.
- **Thread Safe Logging**: Fully supported.
- **Asynchronous Logging**: Coming soon in future releases!

## Installation

Install the package using pip:

```bash
pip install loggingontips
```
## Usage
<h4>Creating a simple log file with a single log</h4>

```python
from loggingontips.Logger import Logger
from loggingontips.LogLevels import LogLevel
logger=Logger()

def run():
    logger.log(LogLevel.INFO,'Is it working?')

if __name__=="__main__":
    run()
```

<h4>Simulation of file rotation after exceeding size limit</h4>

```python
from loggingontips.Logger import Logger
from loggingontips.LogLevels import LogLevel
l1=Logger()
#In this case log file should be rotated as size limit is 4 MB and logs are of 16 MB+
def run():
    for i in range(10000000):
        l1.log(LogLevel.DEBUG,'Working?')

if __name__=="__main__":
    run()
```

<h4>Simulation of thread_safe_log() function [Should be called from threads]</h4>

```python
import threading
import os
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

```
