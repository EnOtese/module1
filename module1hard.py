grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = sorted(list(students))

count_grades_0 = grades[0].__len__()
count_grades_1 = grades[1].__len__()
count_grades_2 = grades[2].__len__()
count_grades_3 = grades[3].__len__()
count_grades_4 = grades[4].__len__()

sum_grade_0 = sum(grades[0])
sum_grade_1 = sum(grades[1])
sum_grade_2 = sum(grades[2])
sum_grade_3 = sum(grades[3])
sum_grade_4 = sum(grades[4])

middle_grade_0 = sum_grade_0 / count_grades_0
middle_grade_1 = sum_grade_1 / count_grades_1
middle_grade_2 = sum_grade_2 / count_grades_2
middle_grade_3 = sum_grade_3 / count_grades_3
middle_grade_4 = sum_grade_4 / count_grades_4

ready_grades = middle_grade_0, middle_grade_1, middle_grade_2, middle_grade_3, middle_grade_4
dictionary = zip(list_students, ready_grades)
print(dict(dictionary))
