from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime, now


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        delta = now() - visit.entered_at

        non_closed_visits.append({
            "who_entered": visit.passcard,
            "entered_at": visit.entered_at,
            "duration": delta,
            "is_strange": is_strange(delta)
        }
        )

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)


def is_strange(delta, minutes=60):
    threshhold_seconds = minutes * 60
    return delta.seconds > threshhold_seconds
