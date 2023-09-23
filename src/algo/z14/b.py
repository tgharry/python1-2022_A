# move = (+1, +2)
#
# pos = [2, 3]
#
# pos += move
#
# print(pos)


def make_move(position: tuple[int, int], move: tuple[int, int]) -> tuple[int, int]:
    return (position[0] + move[0], position[1] + move[1])
