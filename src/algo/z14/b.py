def make_move(position: tuple[int, int], move: tuple[int, int]):
    makes_move = tuple(map(lambda x, xy: x + xy, position, move))
    return makes_move