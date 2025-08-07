from django.shortcuts import render,redirect
from .models import Player

# Create your views here.

def player_name(request, player_id):
    print("The PLAYER Arena !!", player_id)

def Football(request):
    print("The FOOTBALL Arena !!")

def index(request):
    
    players = Player.objects.all()
    
    
    context={
        'players':players
    }
    return render(request, 'thefbproject/index.html',context)
    

def add_player(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        position = request.POST.get('position')
        birth_date = request.POST.get('birth_date')
        player = Player(name=name, age=age, position=position, birth_date=birth_date)
        player.save()
        return redirect('players')
    return render(request, 'thefbproject/add_player.html')