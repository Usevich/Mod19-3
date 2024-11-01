from django.shortcuts import render
from django.views import View
from .forms import UserRegister
from django.http import HttpResponse
from .models  import *
# Create your views here.
def index_view(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})


def shop_view(request):
    games = ["Atomic Heart", "Cyberpunk 2077"]
    context = {'games': games}
    return render(request, 'shop.html', context)


def cart_view(request):
    return render(request, 'cart.html')

def register_buyer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        balance = request.POST.get('balance')
        age = request.POST.get('age')

        # Проверка, существует ли покупатель
        buyers = Buyer.objects.all()
        if not any(buyer.name == name for buyer in buyers):
            Buyer.objects.create(name=name, balance=balance, age=age)
            return HttpResponse('Регистрация успешна!<br><li> <a href="/">Главная страница</a></li>')

        return HttpResponse('Пользователь с таким именем уже существует.<br><li> <a href="/">Главная страница</a></li>')
    return render(request, 'register.html')

def list_games(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})






