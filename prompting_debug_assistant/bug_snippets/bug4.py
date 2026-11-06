import json

def process_user_scores(file_path):
    """Reads a JSON file containing user scores and computes average score."""
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    total_score = 0
    valid_users = 0

    for user in data['users']:
        total_score += user['score']
        valid_users += 1
        
    average = total_score / valid_users
    return average

# Simulated call (will raise runtime exception on missing key or empty list)
test_data = {"users": []}
with open("test_scores.json", "w") as f:
    json.dump(test_data, f)

print("Average:", process_user_scores("test_scores.json"))