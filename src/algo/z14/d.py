from datetime import datetime

from src.algo.z14.c import gen_new_positions


def how_many_moves(start: tuple[int, int], finish: tuple[int, int], max_dim: tuple[int, int]) -> int | None:
    reached = set([start])
    current_positions = set([start])

    moves = 0

    while finish not in reached:
        new_positions = set()

        # przejść przez wszystkie pozycje z current_positions
        for pos in current_positions:
            # dla kazdej wygenerowac nowe poprawne pozycje i wrzucić do n_positions
            for p in gen_new_positions(pos, max_dim):
                if p not in reached:
                    new_positions.add(p)
                    reached.add(p)

        moves += 1
        current_positions = new_positions
        if moves > 2 * max(max_dim):
            return None

    return moves


if __name__ == '__main__':
    SZ = 10000
    st = datetime.now().timestamp()
    mvs = how_many_moves((0, 0), (SZ - 1, SZ - 1), (SZ, SZ))
    en = datetime.now().timestamp()
    print(f'{SZ=}, {mvs=}, duration={en-st:.3f}s')
