from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
#from technex.app.models import UserProfile, College, Team, Event, EventNotification, GeneralNotification
from technex.app.models import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from simplejson import dumps

class RegistrationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'username', 'password1', 'password2', 'email', 'contact', 'gender', 'college',)

class TeamRegistrationForm(ModelForm):
    class Meta:
        model = Team
        #fields = ('name', 'name', 'name', 'name', 'name',)

class EventRegistrationForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'participant_teams',)

def index(request):
    #Registration Check
    error = False
    reg_success = False
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():         
            form.save()
            reg_success = True
        else:
            error = True
    else:
        form = RegistrationForm()
    template_data = {
        'form': form,
        'error': error,
        'registration_successful': reg_success
    }
    
    #General Notifications
    general_notifs = GeneralNotification.objects.all()
    template_data['general_notifs'] = general_notifs
    
    return render_to_response('index.html', template_data, context_instance=RequestContext(request))

def team_registration(request):
    #Team Registration form generator & validator
    error = False
    reg_success = False
    if request.method == "POST":
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():         
            form.save()
            reg_success = True
        else:
            error = True
    else:
        form = TeamRegistrationForm()
    template_data = {
        'form': form,
        'error': error,
        'registration_successful': reg_success
    }
    return render_to_response('registration/registration_team.html', template_data, context_instance=RequestContext(request))

def event_registration(request):
    #Event Registration form generator & validator
    error = False
    reg_success = False
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():         
            form.save()
            reg_success = True
        else:
            error = True
    else:
        form = EventRegistrationForm()
    template_data = {
        'form': form,
        'error': error,
        'registration_successful': reg_success
    }
    return render_to_response('registration/registration_event.html', template_data, context_instance=RequestContext(request))

def serialize_to_json(request):
    try:
        eventname = request.POST.get('event_name', None)
        event = Event.objects.get(name=eventname)
        event_dict = {
                      'event_name': event.name, 
                      'intro': event.introduction , 
                      'probstat': event.problem_statement ,
                      'rules': event.rules_and_regulations,
                      'contacts': event.contacts
                     }
        data = dumps(event_dict)
        response = HttpResponse(data, content_type="application/json")
    except Event.DoesNotExist:
        raise Http404
    return HttpResponse(response)
    
@login_required
def my_page(request):
    #Selecting the event_notification queryset relating to the currently logged in user. 
    #(on the basis of the events he has registered for)
    user = UserProfile.objects.get(name = str(request.user))
    team_set = user.team_set.all()
    for team in team_set:
        event_set = team.event_set.all()
        for event in event_set:
            eventnotif_set = event.eventnotification_set.all()
    eventnotif_set = eventnotif_set.distinct()

    #Converting  the eventnotif_set queryset object to a JSON response
    eventnotif_list = []
    for i in range(0,len(eventnotif_set)):
        eventnotif_list +=[{ 
                                'title' : eventnotif_set[i].title,
                                'body': eventnotif_set[i].body
                               }]

    eventnotif_dict = {'event_notifications' : eventnotif_list }
    data = dumps(eventnotif_dict)
    return HttpResponse(data, content_type="application/json")
