# -*- coding: utf-8 -*-
import time
import jwt
import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from application import models
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@require_http_methods(['POST', ])
@csrf_exempt
def create_token(request):
    key = settings.PRIV_KEY
    try:
        data = request.POST
        if data.get('grant_type') != 'client_credentials':
            return HttpResponse(content=b'Wrong grant_type', status=400)

        client_id = data.get('client_id')
        client_secret = data.get('client_secret')
        aud = data.get('audience', '')

        if not models.APP.objects.is_authorized_app(client_id, client_secret):
            return HttpResponse(status=401)

        now = int(time.time())

        token = {'iss': 'https://tokendealer.zwidny.com',
                 'aud': aud,
                 'iat': now,
                 'exp': now + 3600 * 24}
        token = jwt.encode(token, key, algorithm='RS512')
        return JsonResponse({'access_token': token.decode('utf-8')})
    except Exception as e:
        return HttpResponse(content=bytes(e), status=400)


@require_http_methods(['POST', ])
@csrf_exempt
def verify_token(request):
    key = settings.PUB_KEY
    try:
        body = json.loads(request.body.decode('utf-8'))
        token = body['access_token']
        audience = body.get('audience', '')
        return JsonResponse(jwt.decode(token, key, audience=audience))
    except Exception as e:
        return HttpResponse(content=bytes(e), status=400)
