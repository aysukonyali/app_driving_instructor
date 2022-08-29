from django.db import models
from django.utils.timezone import now
from django.core import serializers 
import uuid
import json

class UserFeedback:
    def __init__(self, name, surname, feedback,email,date):
        self.name = name
        self.surname = surname
        self.email = email
        self.feedback = feedback
        self.date=date


    def __str__(self):
        return "Feedback: " + self.feedback
