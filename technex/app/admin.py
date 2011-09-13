from django.contrib import admin
from technex.app import models

class UserProfileAdmin(admin.ModelAdmin):
    fields = ('name', 'username', 'email', 'contact', 'gender', 'college',)

admin.site.register(models.College)
admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.register(models.Team)
admin.site.register(models.Event)
admin.site.register(models.GeneralNotification)
admin.site.register(models.EventNotification)
