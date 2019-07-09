from glob import glob
import os
import requests
import json
CWD = os.path.abspath(os.path.dirname(__file__))

MAPPING_PATH = os.path.join(CWD, "ranking.json")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(prog="update_ranking")
    parser.add_argument("--host", help="Host of Elasticsearch", default="localhost:9200")
    parser.add_argument("--index", help="Index of Elasticsearch", default="aozorabunko")
    args = parser.parse_args()

    res = requests.post(url='http://{}/{}/_close?pretty'.format(args.host, args.index))
    if res.json().get("acknowledged"):
        print("Index '{}' has been closed".format(args.index))
    else:
        raise Exception(res.text)

    data = open(MAPPING_PATH, "rb").read()
    res = requests.put(url='http://{}/{}/_settings?pretty'.format(args.host, args.index),
                       data=data,
                       headers={'Content-Type': 'application/json'})
    if res.json().get("acknowledged"):
        print("Index '{}' has been updated".format(args.index))
    else:
        raise Exception(res.text)

    res = requests.post(url='http://{}/{}/_open?pretty'.format(args.host, args.index))
    if res.json().get("acknowledged"):
        print("Index '{}' has been opened".format(args.index))
    else:
        raise Exception(res.text)
