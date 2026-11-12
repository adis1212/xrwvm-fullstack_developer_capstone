import json
import os
import urllib.error
import urllib.request

from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"

    request_url = backend_url + endpoint
    if params:
        request_url = request_url + "?" + params

    print(f"GET from {request_url}")
    try:
        req = urllib.request.Request(request_url)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        req = urllib.request.Request(request_url)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        json_data = json.dumps(data_dict).encode('utf-8')
        req = urllib.request.Request(
            request_url,
            data=json_data,
            headers={'Content-Type': 'application/json'},
            method='POST',
        )
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
        return None
