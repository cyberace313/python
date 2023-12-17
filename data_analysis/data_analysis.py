def calculate_average_price(prices):
    if not prices:
        raise ValueError("List must not be empty")

    total_sum = sum(prices)
    return total_sum / len(prices)


def find_maximum_price(prices):
    if not prices:
        raise ValueError("List must not be empty")

    max_price = max(prices)
    return max_price


def count_occurrences(prices, target_price):
    count = prices.count(target_price)
    return count


def compute_cumulative_sum(prices):
    cumulative_sum = []
    current_sum = 0
    for price in prices:
        current_sum += price
        cumulative_sum.append(current_sum)
    return cumulative_sum


# Example usage:
prices_list = [10.0, 20.0, 30.0, 10.0, 40.0]
average_price = calculate_average_price(prices_list)
maximum_price = find_maximum_price(prices_list)
target_occurrences = count_occurrences(prices_list, 10.0)
cumulative_sum = compute_cumulative_sum(prices_list)

print("Average Price:", average_price)
print("Maximum Price:", maximum_price)
print("Occurrences of 10.0:", target_occurrences)
print("Cumulative Sum:", cumulative_sum)
