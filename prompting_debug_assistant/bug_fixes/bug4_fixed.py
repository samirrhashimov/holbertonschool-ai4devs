import json

def process_user_scores(file_path):
    """Reads a JSON file containing user scores and computes average score safely."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0.0

    users = data.get('users', [])
    if not users:
        return 0.0

    scores = [u.get('score', 0) for u in users if isinstance(u, dict) and 'score' in u]
    
    if not scores:
        return 0.0
        
    return sum(scores) / len(scores)


if __name__ == "__main__":
    test_data = {"users": []}
    with open("test_scores.json", "w") as f:
        json.dump(test_data, f)

    print("Average:", process_user_scores("test_scores.json"))