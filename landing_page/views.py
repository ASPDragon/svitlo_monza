from django.shortcuts import render

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
    return render(request, "landing_page/index.html", {"buttons": navigation_bar})