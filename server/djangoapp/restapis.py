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
        feedbacks = json_result["body"]["data"]["docs"]
        for feedback in feedbacks:
            fb_obj = UserFeedback(
                name=feedback["name"],
                surname=feedback["surname"],
                email=feedback["email"],
                feedback=feedback["feedback"]  
            )
            results.append(fb_obj)
    return results


def post_request(url, payload):
    #print(kwargs)
    print("POST to {} ".format(url))
    print(payload)
    response = requests.post(url, json=payload)
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

