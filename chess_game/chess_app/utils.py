import chess

# Store the board globally for now (not ideal for multiplayer)
board = chess.Board()

def get_board_fen():
    return board.fen()

def is_move_legal(move_uci):
    try:
        move = chess.Move.from_uci(move_uci)
        return move in board.legal_moves
    except:
        return False

def make_move(move_uci):
    if is_move_legal(move_uci):
        move = chess.Move.from_uci(move_uci)
        board.push(move)
        return True
    return False
