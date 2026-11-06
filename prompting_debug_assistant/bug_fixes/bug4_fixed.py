import json

def process_user_scores(file_path):
    """Reads a JSON file containing user scores and computes average score safely."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"File loading error: {e}")
        return 0.0

    users = data.get('users', [])
    if not users:
        return 0.0

    # Defensive extraction of valid numeric scores
    scores = [u.get('score', 0) for u in users if isinstance(u, dict) and 'score' in u]
    
    if not scores:
        return 0.0
        
    average = sum(scores) / len(scores)
    return average


# Unit Test Validations
if __name__ == "__main__":
    # Test case 1: Empty users array (Handles ZeroDivisionError)
    test_data_empty = {"users": []}
    with open("test_scores_empty.json", "w") as f:
        json.dump(test_data_empty, f)
    
    result_empty = process_user_scores("test_scores_empty.json")
    assert result_empty == 0.0, "Test 1 Failed"

    # Test case 2: Valid users array
    test_data_valid = {"users": [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 80}]}
    with open("test_scores_valid.json", "w") as f:
        json.dump(test_data_valid, f)
    
    result_valid = process_user_scores("test_scores_valid.json")
    assert result_valid == 85.0, "Test 2 Failed"

    print("bug4_fixed.py: Defensive checks passed! ✅")