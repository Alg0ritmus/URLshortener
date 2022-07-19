from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, JsonResponse
import json

from .models  import *
import hashlib 
# Create your views here.
def index(request):
    longurl_=""
    shorturl_=""
    context = {
        'longurl_': longurl_,
        'shorturl_':shorturl_
    }  
    return render(request,'shortURL/index.html',context)

def post_url(request):
    longurl_=""
    shorturl_=""
    if request.method == 'POST':
        #get data from ajax
        data = json.loads(request.body.decode())

        # get long url
        longurl_=data["longurl"]
        # init hasher
        hasher = hashlib.sha3_224()
        hasher.update(longurl_.encode())
        shorturl_ = hasher.digest().hex()[:5]
        # add url to db
        try:
            if not UrlHandler.objects.filter(longurl=longurl_).exists():
                UrlHandler(longurl=longurl_,shorturl=str(shorturl_)).save()
        except:
            raise Http404("Adding to DB failed")
        
    context = {
        'longurl_': longurl_,
        'shorturl_':shorturl_
    }    
    return JsonResponse(context)

def get_url(request,shorturl):
    get_long_url_object = UrlHandler.objects.get(shorturl=shorturl).longurl
    return redirect(get_long_url_object)
    
