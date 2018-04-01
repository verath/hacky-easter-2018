import os
import csv
import json

import constants

SCRIPT_DIR = os.path.dirname(__file__)


def main():
    num_entries = 0
    with open(os.path.join(SCRIPT_DIR, "data.jsonl")) as in_file:
        for i, _ in enumerate(in_file):
            pass
        num_entries = i

    with open(os.path.join(SCRIPT_DIR, "data.jsonl")) as in_file:
        with open(os.path.join(SCRIPT_DIR, "data_train.csv"), 'w',  newline='') as out_train_file:
            with open(os.path.join(SCRIPT_DIR, "data_test.csv"), 'w',  newline='') as out_test_file:
                train_writer = csv.DictWriter(out_train_file, 
                                              fieldnames=constants.FIELDNAMES, 
                                              quoting=csv.QUOTE_NONNUMERIC)
                test_writer = csv.DictWriter(out_test_file, 
                                             fieldnames=constants.FIELDNAMES, 
                                             quoting=csv.QUOTE_NONNUMERIC)
                train_writer.writeheader()
                test_writer.writeheader()
                n = 0
                for entry_json in in_file:
                    n += 1
                    entry = json.loads(entry_json)
                    entry["g00d"] = int(entry["g00d"])
                    if n < num_entries * 0.8:
                        train_writer.writerow(entry)
                    else:
                        test_writer.writerow(entry)                        

if __name__ == "__main__":
    main()
