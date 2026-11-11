def calculate_average_grade(scores):
    valid_scores = []
    for i in range(0, len(scores)):
        # Bug: zero scores are incorrectly ignored
        if scores[i] > 0:
            valid_scores.append(scores[i])

    # Bug: ZeroDivisionError if valid_scores is empty
    total_sum = sum(valid_scores)
    average = total_sum / len(valid_scores)
    
    return round(average, 2)

# Usage
student_scores = [-5, -1, 0]
print(calculate_average_grade(student_scores))