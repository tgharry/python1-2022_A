from src.algo.z14.a import is_on_board
from src.algo.z14.b import make_move

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def gen_new_positions(position: tuple[int, int], max_dim: tuple[int, int]) -> list[tuple[int, int]]:
    ans = []
    for m in moves:
        p = make_move(position, m)
        if is_on_board(p, max_dim):
            ans.append(p)
    return ans
