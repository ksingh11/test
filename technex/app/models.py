from django.db import models
from django.contrib.auth.models import User, UserManager

class College(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name

class UserProfile(User):
    GENDER_CHOICES = (
                      ('M', 'Male'),
                      ('F', 'Female'),
                      )
    
    name = models.CharField(max_length=30)
    contact = models.BigIntegerField()
    college = models.ForeignKey(College)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    def __unicode__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)
    participants = models.ManyToManyField(UserProfile)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=20)
    parent_event = models.ForeignKey('self', null=True, blank=True)
    short_description = models.CharField(max_length=100, null=True, blank=True)
    full_description = models.TextField()
    participant_teams = models.ManyToManyField(Team, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name

class GeneralNotification(models.Model):
    PRIORITIES = (
                ('N', 'Normal'),
                ('U', 'Urgent'),
                )
    
    title = models.CharField(max_length=30, blank=True, null=True)
    body = models.TextField()
    priority = models.CharField(max_length=1, choices=PRIORITIES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-priority', '-modified']

class EventNotification(models.Model):
    PRIORITIES = (
                ('N', 'Normal'),
                ('U', 'Urgent'),
                )
    
    title = models.CharField(max_length=30, blank=True, null=True)
    event = models.ForeignKey(Event)
    body = models.TextField()
    priority = models.CharField(max_length=1, choices=PRIORITIES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-priority', '-modified']
