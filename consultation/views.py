from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from consultation.forms import ConsultationForm


@require_POST
def consultation(request):
    form = ConsultationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("index")
    return (None


@require_POST)
def consultation_no_message(request):
    form = ConsultationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("index")
    return None