import requests
import json
from .models import UserFeedback
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data


def get_feedback(url):
    results = []
    json_result = get_request(url)
    if json_result:
        feedbacks = json_result["body"]
        for feedback in feedbacks:
            fb_doc = dealer["doc"]
            fb_obj = UserFeedback(
                name=fb_doc["name"],
                surname=fb_doc["surname"],
                email=fb_doc["email"],
                feedback=fb_doc["feedback"]  
            )
            results.append(fb_obj)
    return results


def post_request(url, payload, **kwargs):
    print(kwargs)
    print("POST to {} ".format(url))
    print(payload)
    response = requests.post(url, params=kwargs, json=payload)
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

