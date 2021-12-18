import unittest


def grading_students(grades: list) -> list:
    for j in range(len(grades)):
        grade = grades[j]
        next_mul_of_5 = None
        if grade >= 38:
            for i in range(grade, grade + 3):
                if i % 5 == 0:
                    next_mul_of_5 = i

            if next_mul_of_5:
                if (next_mul_of_5 - grade) < 3:
                    grades[j] = next_mul_of_5

    return grades


class TestSolution(unittest.TestCase):
    def test_1(self):
        grades = [4, 73, 67, 38, 33]
        expected = [4, 75, 67, 40, 33]
        result = grading_students(grades)
        self.assertEqual(expected, result)
