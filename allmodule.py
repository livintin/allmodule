grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
sr_grades = [sum(grades[0])/len(grades[0]),
             sum(grades[1])/len(grades[1]),
             sum(grades[2])/len(grades[2]),
             sum(grades[3])/len(grades[3]),
             sum(grades[4])/len(grades[4])]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_alf = sorted(list(students))
average_score = dict([[students_alf[0], sr_grades[0]],
                      [students_alf[1], sr_grades[1]],
                      [students_alf[2], sr_grades[2]],
                      [students_alf[3], sr_grades[3]],
                      [students_alf[4], sr_grades[4]]])
print(average_score)
