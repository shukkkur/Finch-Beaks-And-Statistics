'''
Сабзалиев Шаханшо
https://hh.ru/resume/d6a613eaff07dd96660039ed1f7364664d6362
03/06/2021
'''

import pandas as pd
from io import StringIO

file = input('Название файла или данные (нажмите Enter в конце ввода): ').strip()
contents=[]
try:
      df = pd.read_csv(file, header=None, names=['Surname', 'Salary'], sep=' ')
except Exception as e:
      try:
            df = pd.read_csv(file + '.txt', header=None, names=['Surname', 'Salary'], sep=' ')
      except Exception as e:
            try:
                  df = pd.read_csv(file + '.csv', header=None, names=['Surname', 'Salary'], sep=' ')
            except Exception as e:
                  while True:
                        line = input()
                        if not line:
                              break
                        else:
                              contents.append(line)
if contents:
      contents = [i.split() for i in contents]
      df = pd.DataFrame(contents, columns=['Surname', 'Salary'])
      df['Salary'] = pd.to_numeric(df['Salary'])

print('Кол-во сотрудников: ', df.shape[0])
print('Общая сумма зарплат: ', int(df.Salary.sum()))
print('Средняя зарплата: ', float(df.Salary.mean()))
print('Медиана от зарплат: ', float(df.Salary.median()))
print('Минимальная зарплата: ', float(df.Salary.min()))
print('Максимальная зарплата: ', float(df.Salary.max()))
print('Кол-во сотрудников, получающих сумму строго большую, чем средняя зарплата: ', df[df.Salary > df.Salary.mean()].shape[0])
df.dropna(inplace=True)
print('Количество сотрудников, чьи фамилии начинаются на букву «K»: ', df[df.Surname.str.startswith('K')].shape[0])
