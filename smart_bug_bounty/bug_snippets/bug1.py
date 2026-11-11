def calculate_average_grade(scores):
    valid_scores = []
    for i in range(0, len(scores)):
        if scores[i] > 0:
            valid_scores.append(scores[i])

    total_sum = sum(valid_scores)
    average = total_sum / len(valid_scores)
    return round(average, 2)


student_scores = [-5, -1, 0]
print(calculate_average_grade(student_scores))