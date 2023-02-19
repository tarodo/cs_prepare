from heapq import *


def find_maximum_capital(capital, profits, number_of_projects, initial_capital):
    min_capital_heap = []
    max_profit_heap = []

    for i in range(len(profits)):
        heappush(min_capital_heap, (capital[i], i))

    available_capital = initial_capital
    for _ in range(number_of_projects):
        while min_capital_heap and min_capital_heap[0][0] <= available_capital:
            capital, i = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[i], i))

        if not max_profit_heap:
            break

        available_capital += -heappop(max_profit_heap)[0]

    return available_capital


def main():
    print("Maximum capital: " + str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print(
        "Maximum capital: "
        + str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0))
    )


main()
