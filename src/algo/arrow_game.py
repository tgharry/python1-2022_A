def find_score(x, y):
    centers = [(4, 4), (3, 3), (3, 6), (6, 3), (6, 6)]
    distances = [0.5, 1.5, 2.5, 3.5, 4.5]

    for center, distance in zip(centers, distances):
        if (x - center[0])**2 + (y - center[1])**2 <= distance**2:
            return 5 - distances.index(distance)
    return 1

def get_scores(test_cases):
    results = []
    for grid in test_cases:
        total_score = 0
        for i in range(10):
            row = grid[i]
            for j, char in enumerate(row):
                if char == 'X':
                    total_score += find_score(i, j)
        results.append(total_score)
    return results

def test():
    # Test Case 1: An arrow at the center
    input1 = [
        "..........",
        "..........",
        "..........",
        "..........",
        "....X.....",
        "..........",
        "..........",
        "..........",
        "..........",
        ".........."
    ]
    assert get_scores([input1]) == [5]

    # Test Case 2: Multiple arrows in different rings
    input2 = [
        "..........",
        "..........",
        "....X.....",
        "...X......",
        "....X.....",
        "..........",
        "..........",
        "..........",
        "..........",
        ".........."
    ]
    assert get_scores([input2]) == [11]

    # Test Case 3: Multiple test grids
    input3 = [
        "..........",
        "..........",
        "..........",
        "...X......",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        ".........."
    ]
    input4 = [
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        "..........",
        ".........."
    ]
    assert get_scores([input3, input4]) == [4, 0]

    print("All tests passed!")

test()