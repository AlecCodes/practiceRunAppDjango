from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from .helper import GetBody
from .models import Run
from django.views import View
# Create your views here.

class RunView(View):
    def get(self, request):
        #get all runs
        all = Run.objects.all()
        #turn into json string
        serialized = serialize("json", all)
        #turn json string into dict
        finalData = json.loads(serialized)
        #send json reponse
        return JsonResponse(finalData, safe=False)
