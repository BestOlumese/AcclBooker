from django.shortcuts import render
from .models import Board
from rooms.models import Room
from django.utils import timezone

def home(request):
    boards = Board.objects.all() # Get all boards ordered by latest
    rooms = Room.objects.all()
    return render(request, 'index.html', {'boards': boards, 'rooms': rooms})

def today(request):
    today = timezone.now().date()
    boards = Board.objects.filter(date=today)  # Get all boards ordered by latest
    rooms = Room.objects.all()
    return render(request, 'today.html', {'boards': boards, 'rooms': rooms})

def completed(request):
    boards = Board.objects.filter(is_completed=True)  # Get all boards ordered by latest
    rooms = Room.objects.all()
    return render(request, 'completed.html', {'boards': boards, 'rooms': rooms})

def uncompleted(request):
    boards = Board.objects.filter(is_completed=False)  # Get all boards ordered by latest
    rooms = Room.objects.all()
    return render(request, 'uncompleted.html', {'boards': boards, 'rooms': rooms})
