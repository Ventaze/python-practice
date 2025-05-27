import sys
from datetime import datetime

def log(message):
    now = datetime.now()
    timestamp = now.strftime("[%Y-%m-%d %H:%M:%S]")
    print(f"{timestamp} {message}", file=sys.stderr)

log("Test message")
