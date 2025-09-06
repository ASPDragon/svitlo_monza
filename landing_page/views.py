from django.shortcuts import render

from consultation.forms import ConsultationForm

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
    form = ConsultationForm()
    return render(request, "landing_page/index.html", {"form" : form, "buttons": navigation_bar})