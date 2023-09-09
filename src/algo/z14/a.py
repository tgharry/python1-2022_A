def is_on_board(position: tuple[int, int], max_dim: tuple[int, int] = (8, 8)):
    x,y = position
    x_d, y_d = max_dim

    if x>=0 and y>=0 and x_d>=0 and x_d>=0:
        if x <x_d and y<y_d:
            return True
        else:
            return False
    else:
        return False



