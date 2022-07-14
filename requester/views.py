from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class RequestView(View):
    def get(self, request):
        return HttpResponse('hey', content_type='text/plain')