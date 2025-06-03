from abc import ABC, abstractmethod
from datetime import datetime

class Formatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass

class SimpleFormatter(Formatter):
    def format(self, message: str) -> str:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"[{now}] {message}"

class UpperCaseFormatter(Formatter):
    def format(self, message: str) -> str:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f"[{now}] {message.upper()}"

class Handler(ABC):
    @abstractmethod
    def handle(self, formatted_message: str):
        pass

class ConsoleHandler(Handler):
    def handle(self, formatted_message: str):
        print(formatted_message)

class FileHandler(Handler):
    def __init__(self, filename):
        self.filename = filename

    def handle(self, formatted_message: str):
        with open(self.filename, 'a') as f:
            f.write(formatted_message + '\n')

class Logger:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter
        self.handlers = []

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)

    def log(self, message: str):
        formatted = self.formatter.format(message)
        for handler in self.handlers:
            handler.handle(formatted)

if __name__ == "__main__":
    logger = Logger(SimpleFormatter())
    logger.add_handler(ConsoleHandler())
    logger.add_handler(FileHandler("pattern_log.txt"))

    logger.log("перше повідомлення")
    logger.log("друге повідомлення")
