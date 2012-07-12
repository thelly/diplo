# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.core import serializers
import models
import simplejson as json
import helper
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def index(request):
    t=loader.get_template("index.html")
    c=RequestContext(request)
    return HttpResponse(t.render(c))

def companie(request):
    t=loader.get_template("companie.html")
    c=RequestContext(request)
    return HttpResponse(t.render(c))

def student(request):
    t=loader.get_template("student.html")
    c=RequestContext(request)
    return HttpResponse(t.render(c))


def articol(request):
    idArticle=request.GET.get("idArticle")
    article=models.Article.objects.get(idArticle=idArticle)
    #if the article is private and the user is not authenticated
    if article.rights==1:
        if request.user.is_authenticated()==False:
            t=loader.get_template("login.html")
            c=RequestContext(request)
            return HttpResponse(t.render(c))
    else:
        t=loader.get_template("articol.html")
        c=RequestContext(request, {"article": article})
        return HttpResponse(t.render(c))
    
def login(request):
    t=loader.get_template("login.html")
    c=RequestContext(request)
    return HttpResponse(t.render(c))

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def api_login(request):
    #linkedinID= request.POST.get("profile")
    profile=json.loads(request.POST.get('value'))
    
    #extract the id
    if profile['id']!="" and profile['id']!='private':
        try:
            student=models.StudentLinkedinprofile.objects.get(linkedinId=profile['id'])
            #if the id exists in the linkedinprofile table
            #get the user corresponding to the profile
            user=student.user
            #this is really weird, i have to authenticate the user even if he's already authenticated
            user=authenticate(user.username,user.password)
            login(request,user)
            #then authenticate the user
            #TODO:if the user is authenticated fill in the authentication menu!!!
            auth="true"
        except models.StudentLinkedinprofile.DoesNotExist:
        #else create the user and then authenticate    
            #the username has to be changed to something smarter
            try:
                user = User.objects.create_user(profile['firstName']+profile['lastName'], "anonymous@linkedin.com", 'noPassword')
                user.first_name=profile['firstName']
                user.last_name=profile['lastName']
                import pdb; pdb.set_trace()
                helper.createUserLinkedinProfile(profile,user)
            except Exception:#most likely an integrity error
                #username already exists redirect to some create username
                return createUsername(request)
                #delete the user
                #user.delete()
        except Exception,x:
            print x
                
                
    
    
    
    data=str(profile)
    mimetype="application/xml"
    return HttpResponse(data,mimetype)

def createUsername(request):
    #TODO: page for creating a username
    pass
