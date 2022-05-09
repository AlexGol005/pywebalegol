from datetime import datetime
from random import random

from django.shortcuts import render
from django.views import View
from django.http import  HttpResponse, HttpRequest


class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)

class RandomNumView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        randomnum = random()

        return HttpResponse(randomnum)
