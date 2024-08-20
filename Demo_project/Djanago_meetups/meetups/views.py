from django.shortcuts import render

def index(request):
    meetups = [
        {'title': 'Django Meetup', 'location':'Newyork'},
        {'title': 'Python Meetup', 'location':'Washnigton'},
        {'title': 'Web Development Meetup', 'location':'Newyork'}
    ]
    return render(request, 'meetups/index.html', {'meetups': meetups})
