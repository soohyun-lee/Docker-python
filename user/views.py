import re, requests
import json
import jwt

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from datetime import datetime, timedelta

from settings_common import SECRET_KEY, ALGORITHM
from .models import User

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']

        today = datetime.now()

        if not User.objects.filter(name=name):
            create_user = User.objects.create(
                name = name
            )
            token = jwt.encode(
                {
                    'user_id' : create_user.id,
                    'exp' : today + timedelta(days=730)
                }, SECRET_KEY, ALGORITHM
            ).decode('utf-8')

            User.objects.filter(name=name).update(
                token = token
            )
            return JsonResponse({'data' : token}, status = 200)
        
        db_token = User.object.filter(name=name)[0].token
        return JsonResponse({'data': db_token}, status=200)


    

        

