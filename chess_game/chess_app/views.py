from django.shortcuts import render
from django.http import JsonResponse
import chess

# Create a global board (optional; better to manage per session/user)
board = chess.Board()

def index(request):
    return render(request, 'index.html', {'board': board})

def make_move_view(request):
    if request.method == 'POST':
        from_square = request.POST.get('from')
        to_square = request.POST.get('to')
        move = chess.Move.from_uci(from_square + to_square)

        if move in board.legal_moves:
            board.push(move)
            return JsonResponse({'status': 'ok', 'fen': board.fen()})
        else:
            return JsonResponse({'status': 'illegal move'}, status=400)

    return JsonResponse({'status': 'bad request'}, status=400)
