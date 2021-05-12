from typing import List
from contents.models import Listup
import re, requests
import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import Listup

class Contents(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Listup.objects.create(
            study_date = data['studya_date'],
            title = data['title'],
            study_contents = data['contents']
        )
        
        return JsonResponse({'message' : 'success'}, status=200)
    
    def get(self, reuquest):
        all_contents = Listup.object.all()

        data = [{
            'id' : content.id,
            'date' : content.study_date,
            'title' : content.title,
            'study_contetns' : content.study_contents
        }for content in all_contents]

        return JsonResponse({'data' : data}, status=200)

    def patch(self, request):
        data = json.loads(request.body)

        Listup.object.filter(id = data['id']).update(
            'date' : data['data']
            'title' : data['title']
            'study_contetns' : data['study_contetns']
            )
        return JsonResponse({'message': 'success'}, status=200)