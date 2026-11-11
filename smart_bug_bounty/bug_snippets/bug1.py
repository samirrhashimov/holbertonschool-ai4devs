def last_n_items(items, n):
    """Return the last n items of a list."""
    if n <= 0:
        return []
    # BUG: off-by-one error in the slice
    return items[-n + 1:]


def main():
    numbers = [1, 2, 3, 4, 5]
    result = last_n_items(numbers, 3)
    print("Result:", result)  # Expected: [3, 4, 5]


if __name__ == "__main__":
    main()