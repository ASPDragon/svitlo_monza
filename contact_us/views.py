from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from contact_us.forms import ContactUsForm


# Create your views here.
@require_POST
def contact_us(request):
    form = ContactUsForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("index")
    return None