def get_min_moves(target_x, target_y, start_x, start_y, chess_board_size):
    # Jeśl x,y poza, error
    if target_x < 0 or target_x >= chess_board_size or target_y < 0 or target_y >= chess_board_size:
        return -1

    """""
    0 1   1 0
    1       1
        K
  
    1       1 
    0 1   1 0
    """""
    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    seen = set()
    game = [(start_x, start_y, 0)]
    while game:
        start_x, start_y, steps = game.pop(0)
        if start_x == target_x and start_y == target_y:
            return steps
        seen.add((start_x, start_y))
        for new_x, new_y in knight_moves:
            next_x = start_x + new_x
            next_y = start_y + new_y
            if (next_x, next_y) not in seen:
                game.append((next_x, next_y, steps + 1))
    return -1


if get_min_moves == -1:
    print("Nie można wykonać tego ruchu")
else:
    print(f"Ruch zajmie {get_min_moves} ruchów")