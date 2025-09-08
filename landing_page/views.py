from django.shortcuts import render

from consultation.forms import ConsultationForm
from contact_us.forms import ContactUsForm

# Create your views here.
navigation_bar = {
    '#events' : 'Домашнi групи',
    '#consultation' : 'Консультацiя',
    '#public_worship' : 'Служiння',
    '#faq' : 'FAQ',
    'privacy_policy' : 'Полiтика Конфiденцiйностi',
    '#about' : 'Про нас',
}

def index(request):
    consultation_form = ConsultationForm()
    contact_us_form = ContactUsForm()
    return render(request, "landing_page/index.html", {"consultation_form" : consultation_form, "contact_us_form" : contact_us_form, "buttons": navigation_bar})


def privacy_policy(request):
    contact_us_form = ContactUsForm()
    return render(request, "landing_page/privacy_policy.html", {"contact_us_form" : contact_us_form, "buttons": navigation_bar})