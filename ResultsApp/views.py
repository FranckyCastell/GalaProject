from django.shortcuts import render
from HomeApp.models import Participant

# Create your views here.


def results(request):
    nickname = []  # ALL PARTICIPANTS
    poty = []  # ALL VALUES ( POTY )
    moty = []  # ALL VALUES ( MOTY )

    objects = Participant.objects.all()

    for participant in objects:
        nickname.append(participant.nickname)
        poty.append(participant.poty)
        moty.append(participant.moty)

    return render(request, 'ResultsApp/results.html', {'nickname': nickname, 'poty': poty, 'moty': moty})
