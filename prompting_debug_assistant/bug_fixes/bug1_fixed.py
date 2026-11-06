def get_last_n_items(items, n):
    """Returns the last n elements from the given list safely."""
    if not items or n <= 0:
        return []
    # Negative slicing correctly retrieves the last n elements
    return items[-n:]


# Unit / Manual Test Assertions
if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    
    # Standard slicing test
    assert get_last_n_items(sample_list, 2) == [40, 50], "Test 1 Failed"
    
    # Edge case: n equals list length
    assert get_last_n_items(sample_list, 5) == [10, 20, 30, 40, 50], "Test 2 Failed"
    
    # Edge case: n is larger than list length
    assert get_last_n_items(sample_list, 10) == [10, 20, 30, 40, 50], "Test 3 Failed"
    
    # Edge case: n <= 0
    assert get_last_n_items(sample_list, 0) == [], "Test 4 Failed"
    
    print("bug1_fixed.py: All tests passed successfully! ✅")