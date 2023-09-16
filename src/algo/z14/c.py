def gen_new_positions(position: tuple[int, int], max_dim: tuple[int,int]) -> list[tuple[int,int]]:
    knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    makes_move = []
    for item in knight_moves:
        makes_move.append((position[0] + i[0], position[1] + i[1]))
    return makes_move

