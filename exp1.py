# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое,
# среднее квадратичное отклонение,
# смещенную и несмещенную оценки дисперсий для данной выборки.

import numpy as np
from math import sqrt

salary = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
salary.sort()
print(salary)
#  ищем среднее арифместическое без спец.методов:
sum = 0
for i in range(0, len(salary)):
    sum += salary[i]
average = sum / len(salary)
print(average)
# проверка спец.методов mean
avg = salary.mean()
print(avg)
#  ищем CКО:
sum_sqrt = 0
for i in range(0, len(salary)):
    sum_sqrt += (salary[i] - average) ** 2
st_deviation = sqrt(sum_sqrt / len(salary))
print(st_deviation)
#  Проверка методом std
dev_control = np.std(salary)
print(dev_control)
# Смещенная дисперсия:
shift_var = sum_sqrt/len(salary)
print(shift_var)
print(np.var(salary, ddof=0))
# Несмещенная дисперсия:
unshift_var = sum_sqrt/(len(salary)-1)
print(unshift_var)
print (np.var(salary, ddof=1))