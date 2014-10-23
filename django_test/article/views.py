from article.models import Article
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.core.context_processors import csrf
from django.contrib import auth


def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html' ,c)
def auth_view(request):
    username = request.POST.get('username' , '')
    password = request.POST.get('password' , '')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/account/loggedin')
    else:
        return HttpResponseRedirect('/account/invalid')


def loggedin(request):
    return render_to_response('loggedin.html',
        {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def articles(request):
    language = 'en-gb'
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']

    data = serializers.serialize("json", Article.objects.all())
    return render_to_response('artcles.html',
                              {'artcles': Article.objects.all(),
                               'language' : language,
                               'commant' : session_language,
                                'data' : data})


def article(request,article_id = 1):
    return render_to_response('artcle.html',
                              {'article' : Article.objects.get(id=article_id)})

def language(request, language ='en-gb'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language

    return response