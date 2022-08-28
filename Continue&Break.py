#!/usr/bin/env python3
# continue & break statement
# Require users to enter salaries, if salary is less than 0 you need to re-enter.
# The outputs includ the number of employees, the list of salaries, and the average salary。

empNum = 0
salary = []
salarySum = 0
while True:
    s = input('Enter employee\'s salary (enter Q or q to finish the input):')
    if s.upper() == 'Q':
        print('Salary Entry Completed')
        break
    if float(s) < 0:
        continue
    empNum += 1
    salary.append(float(s))
    salarySum += float(s)

print('The Number of Employees: {}'.format(empNum))
print('The List of Salaries:', salary)
print('The Avarage Salary: {}'.format(salarySum/empNum))
