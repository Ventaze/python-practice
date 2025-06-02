import sys
from datetime import datetime

class Logger:
    def __init__(self, output_stream, time_format):
        self.output_stream = output_stream
        self.time_format = time_format

    def log(self, message):
        now = datetime.now()
        timestamp = now.strftime(self.time_format)
        print(f"{timestamp} {message}", file=self.output_stream)

# Тест:
if __name__ == "__main__":
    out_stream = sys.stderr
    time_formatter = '%Y-%m-%d %H:%M:%S'
    logger = Logger(out_stream, time_formatter)

    logger.log('message for logging')
