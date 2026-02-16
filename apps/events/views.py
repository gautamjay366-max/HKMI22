from django.shortcuts import render

# Create your views here.
def events_home(request):
    return render(request, 'pages/event.html')
