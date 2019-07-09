from glob import glob
import os
import requests
CWD = os.path.abspath(os.path.dirname(__file__))

JSON_PATH = os.path.join(CWD, "aozorabunko_json_data", "*.json.*")
MAPPING_PATH = os.path.join(CWD, "mapping.json")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(prog="insert_aozorabunko")
    parser.add_argument("--host", help="Host of Elasticsearch", default="localhost:9200")
    parser.add_argument("--index", help="Index of Elasticsearch", default="aozorabunko")
    args = parser.parse_args()

    res = requests.delete(url='http://{}/{}?pretty'.format(args.host, args.index))
    if res.json().get("acknowledged"):
        print("Index '{}' has been deleted".format(args.index))

    data = open(MAPPING_PATH, 'rb').read()
    res = requests.put(url='http://{}/{}?pretty'.format(args.host, args.index),
                       data=data,
                       headers={'Content-Type': 'application/json'})
    if res.json().get("acknowledged"):
        print("Index '{}' has been initialized".format(args.index))

    total_doc_num = 0
    for input_filepath in sorted(glob(JSON_PATH)):
        print("Inserting data from '{}' ...".format(input_filepath))
        data = open(input_filepath, 'rb').read()
        res = requests.post(url='http://{}/_bulk?pretty'.format(args.host),
                            data=data,
                            headers={'Content-Type': 'application/x-ndjson'})
        doc_num = len(res.json()["items"])
        total_doc_num += doc_num
        print("Inserted {} documents".format(doc_num))
        print()

    print("Inserted {} documents in total".format(total_doc_num))
