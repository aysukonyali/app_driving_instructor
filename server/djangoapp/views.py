from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from .models import UserFeedback
from .restapis import get_feedback,post_request
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json
from datetime import date

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...


# Create a `contact` view to return a static contact page
#def contact(request):

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_feedbacks(request):
    if request.method == "GET":
        url = "https://439290d0.eu-de.apigw.appdomain.cloud/driving/feedbacks"
        feedbacks = get_feedback(url)
        context = {}
        feedbacks.sort(key=lambda x: x.date,reverse=True)
        context["feedbacks"] = feedbacks
        return render(request, 'djangoapp/index.html', context)
    elif request.method == "POST":
        feedback = {}
        form = request.POST
        feedback["name"] = form["name"]
        feedback["surname"] =form["surname"]
        feedback["email"]=form["email"]
        feedback["feedback"] = form["fback"]
        feedback["date"]= date.today().strftime("%d/%m/%Y")
        post_url = "https://439290d0.eu-de.apigw.appdomain.cloud/driving/feedbacks"
        json_payload = { "feedback": feedback }
        post_request(post_url, json_payload)
        return redirect("djangoapp:index")



# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

   


