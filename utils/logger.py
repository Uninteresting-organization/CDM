from datetime import datetime

def log(message):
    with open("cdm_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {message}\n")
    print(message)
