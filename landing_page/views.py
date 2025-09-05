from django.shortcuts import render

# Create your views here.
navigation_bar = {
    'about' : 'Про нас',
    'events' : 'Домашнi групи',
    'consultation' : 'Консультацiя',
    'public_worship' : 'Служiння',
    'faq' : 'FAQ',
    'privacy_policy' : 'Полiтика Конфiденцiйностi'
}

def index(request):
    return render(request, "landing_page/index.html", {"buttons": navigation_bar})