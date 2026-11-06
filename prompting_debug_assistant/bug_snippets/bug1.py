def get_last_n_items(items, n):
    """Returns the last n elements from the given list."""
    if n <= 0:
        return []
    start_index = len(items) - n + 1
    return items[start_index:]


# Test execution
sample_list = [10, 20, 30, 40, 50]
print(get_last_n_items(sample_list, 2))  # Expected [40, 50]
print(get_last_n_items(sample_list, 5))  # Expected [10, 20, 30, 40, 50]