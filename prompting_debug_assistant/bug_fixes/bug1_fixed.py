def get_last_n_items(items, n):
    """Returns the last n elements from the given list safely."""
    if not items or n <= 0:
        return []
    return items[-n:]


if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    print(get_last_n_items(sample_list, 2))  # [40, 50]
    print(get_last_n_items(sample_list, 5))  # [10, 20, 30, 40, 50]s