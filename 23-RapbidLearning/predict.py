import base64
import difflib
import random

import requests
import tensorflow as tf
import pandas as pd

import constants
import train


DATA_URL = 'http://whale.hacking-lab.com:2222/gate'
SUBMIT_URL = 'http://whale.hacking-lab.com:2222/predict'
REWARD_URL = 'http://whale.hacking-lab.com:2222/reward'

def decode_attribute_names(attr_list):
    """Takes a list of encoded attribute names and decodes them
    into the corresponding known fieldnames."""
    decoded_attrs = []
    for attr in attr_list:
        # Each attribute is base64 encoded
        attr_str = base64.b64decode(attr).decode('utf-8')
        # And may have some characters altered (e.g. "ag3" vs "4ge", etc.)
        if attr_str in constants.FIELDNAMES:
            decoded_attrs.append(attr_str)
        else:
            best_ratio = 0
            best_attr = ""
            for known_attr in constants.FIELDNAMES:
                ratio = difflib.SequenceMatcher(None, attr_str, known_attr).ratio()
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_attr = known_attr
            decoded_attrs.append(best_attr)
    return decoded_attrs


def fetch_predict_data(session):
    """Fetches and format data to predict.
    [{'n4m3': 'Janet', 'g3nd3r': 'female', 'ag3': 4, 'c0l0r': 'red', 'w31ght': 2, 'l3ngth': 46, 'sp00n': 14, 't41l': 11}, ...]
    """
    raw_data = session.get(DATA_URL).json()
    attributes = decode_attribute_names(raw_data["attributes"])
    data = []
    for raw_entry in raw_data["data"]:
        entry = {}
        for i, attr in enumerate(attributes):
            entry[attr] = raw_entry[i]
        data.append(entry)
    return data


def predict(model, data):
    df = pd.DataFrame(data)
    input_fn = tf.estimator.inputs.pandas_input_fn(x=df, shuffle=False)
    predictions = model.predict(input_fn=input_fn)
    return [int(p["classes"]) for p in predictions]


def submit_prediction(session, prediction):
    cookies = {"session_id": session.cookies["session_id"]}
    return session.post(SUBMIT_URL, json=prediction, cookies=cookies).text


def claim_reward(session):
    cookies = {"session_id": session.cookies["session_id"]}
    return session.post(REWARD_URL, cookies=cookies).text


def main():
    model = train.build_estimator(train.MODEL_DIR)
    session = requests.session()

    data = fetch_predict_data(session)
    prediction = predict(model, data)
    submit_res = submit_prediction(session, prediction)
    if "This was crap - try again!" in submit_res:
        return
    print("Submission Res: ", submit_res)
    print("Claim Res:", claim_reward(session))


if __name__ == "__main__":
    main()
