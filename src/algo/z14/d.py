from __future__ import annotations


def how_many_moves(start: tuple[int, int], finish: tuple[int, int], max_dim: tuple[int, int]) -> int | None:
    reached = set([start])
    current_positions = set([start])
    move_set = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    moves = 0

    def moving(current_positions: tuple[int, int], moves) -> int | None:
        if current_positions == finish:
            return moves
        if moves > 2*max(max_dim):
            return None
        for x, y in move_set:
            newx, newy = current_positions[0] + x, current_positions[1] + y

            if 0 <= newx < max_dim[0] and 0 <= newy < max_dim[1]:
                new_position = (newx, newy)
                if new_position not in reached:
                    reached.add(new_position)
                    result = moving(new_position, moves + 1)

                    if result != None:
                        return result
                    reached.remove(new_position)
    return moving(start, moves)

a = how_many_moves(start=(0,0), finish=(8,9), max_dim=(10,10))
print(a)