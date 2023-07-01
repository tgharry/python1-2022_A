


def get_best_value_package(costs: list[int], values: list[int], max_total_cost: int) -> int:
    # znaleźć najlepszą możliwą wartość podzbioru itemów, ale takich by łączny "cost" tych itemów nie przekraczał
    # wartości max_total_cost
    num_items=len( costs )
    dp=[0] * (max_total_cost + 1)

    for i in range( num_items ) :
        for j in range( max_total_cost, costs[i] - 1, -1 ) :
            dp[j]=max( dp[j], values[i] + dp[j - costs[i]] )

    return dp[max_total_cost]








