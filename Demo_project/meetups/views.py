from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound
from . import models
from .form import RegistrationForm

def index(request):
    meetups = models.Meetup.objects.all() 
    return render(request, 'meetups/index.html', {'meetups': meetups})

def meetup_details(request, meetup_slug):
    try:
        meetup = models.Meetup.objects.get(slug=meetup_slug)
        if request.method == 'POST':
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = models.Participant.objects.get_or_create(email=user_email)
                meetup.participants.add(participant)
                return redirect('success_page')
        else:
            registration_form = RegistrationForm()
        
        return render(request, 'meetups/meetup_details.html', {
            'meetup': meetup,
            'form': registration_form
        })
    except models.Meetup.DoesNotExist:
        return HttpResponseNotFound('<h1>Meetup not found</h1>')
def success_page(request):
    return render(request, 'meetups/success_page.html')