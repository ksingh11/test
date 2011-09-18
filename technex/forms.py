from technex.app.models import UserProfile
from django.forms import form_for_model

RegisterForm = form_for_model(UserProfile)
