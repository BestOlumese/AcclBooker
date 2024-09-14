from django.shortcuts import render
from boards.models import Board
from .models import Room

# Create your views here.
def roomBoard(request, id):
    boards = Board.objects.filter(room=id)  # Get all boards ordered by latest
    rooms = Room.objects.all()
    return render(request, 'room.html', {'boards': boards, 'rooms': rooms})