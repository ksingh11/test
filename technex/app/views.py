from django.contrib.auth.forms import UserCreationForm
from technex.app.models import UserProfile, College, Team, Event
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from simplejson import dumps

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'username', 'password1', 'password2', 'email', 'contact', 'gender', 'college',)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    
    templateData = {
                    'form': form,
                    }
    return render_to_response('form.html', templateData, context_instance=RequestContext(request))

def home(request):
    return render_to_response('index.html',context_instance=RequestContext(request))


def serialize_to_json(request):
    try:
        eventname = request.POST.get('event_name', None)
        event = Event.objects.get(name=eventname)
        event_dict = {'event_name': event.name, 'intro': event.introduction , 'probstat': event.problem_statement ,'rules': event.rules_and_regulations,\
        'contacts': event.contacts}
        data = dumps(event_dict)
        response = HttpResponse(data, mimetype="application/json")
    except Event.DoesNotExist:
        raise Http404
    return HttpResponse(response)
