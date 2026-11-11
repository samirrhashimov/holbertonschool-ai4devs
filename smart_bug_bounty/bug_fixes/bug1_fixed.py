def last_n_items(items, n):
    """Return the last n items of a list."""
    if n <= 0:
        return []
    # FIX: items[-n:] is the correct slice (no "+ 1")
    return items[-n:]


def main():
    assert last_n_items([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert last_n_items([1, 2, 3], 0) == []
    assert last_n_items([1, 2], 5) == [1, 2]
    print("All 3 test cases passed")


if __name__ == "__main__":
    main()