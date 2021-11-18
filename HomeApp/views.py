from django.shortcuts import render, redirect
from HomeApp.models import Participant
from django.db.models import F

# Create your views here.


def home(request):
    participants = Participant.objects.all()
    if request.method == 'POST':
        if 'poty' in request.POST:
            Participant.objects.filter(
                id=request.POST.get("id")).update(poty=F('poty') + 1)
        elif 'moty' in request.POST:
            Participant.objects.filter(
                id=request.POST.get("id")).update(moty=F('moty') + 1)
        return redirect('/')

    return render(request, 'HomeApp/home.html', {"participants": participants})
