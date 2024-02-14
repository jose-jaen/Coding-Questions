from typing import List


def grading_students(grades: List[int]) -> List[int]:
    for i in range(len(grades)):
        if grades[i] >= 38:
            cond1 = (grades[i] + 1) % 5 == 0
            cond2 = (grades[i] + 2) % 5 == 0
            if grades[i] % 5 != 0 and cond1:
                grades[i] += 1
            elif grades[i] % 5 != 0 and cond2:
                grades[i] += 2
    return grades
