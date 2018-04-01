import requests
import time
import os

TRAIN_URL = "http://whale.hacking-lab.com:2222/train"
SCRIPT_DIR = os.path.dirname(__file__)

def fetch_record():
    r = requests.get(TRAIN_URL)
    r.raise_for_status()
    return r.text

def main():
    with open(os.path.join(SCRIPT_DIR, 'data.jsonl'), 'a') as f:
        for n in range(0, 100_000):
            f.write(fetch_record() + "\n")
            f.flush()
            time.sleep(0.5)
            if n % 1000 == 0:
                print(n)

if __name__ == "__main__":
    main()

