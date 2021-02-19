import logging
import os

import pymongo

from bson.json_util import dumps
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        url = os.environ["DB_URL_STRING"]
        client = pymongo.MongoClient(url)
        database = client["rkd-m-db"]
        collection = database["rkd-notes"]

        note = collection.find({})
        print('A sample document:')
        print(note)
        result = dumps(note)

        return func.HttpResponse(result, mimetype="application/json", charset="utf-8")
    
    except ConnectionError:
        return func.HttpResponse("Unable to connect to MongoDB", status_code=400)
