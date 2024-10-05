import matplotlib.pyplot as plt
import numpy as np

#Задаём списки данных
numbers_of_lessons = [4, 4, 3, 3, 2, 2, 2, 1]
subjects = ["Общая \nфизика", "Математический \nанализ", "Химия", "Информатика","Аналитическая \nгеометрия", "Иностранный \nязык", "Физическая \nкультура", "Безопасность \nжизнедеятельности"]
colors = ['purple', 'pink', 'goldenrod', 'ivory', 'lightgreen', 'navy', 'teal', 'tan']

#Строим диаграмму
fig, ax = plt.subplots(figsize=(12, 8), layout = 'constrained')
plt.bar(subjects, numbers_of_lessons, color = colors, edgecolor = 'black', label='Данные с календаря', alpha=0.1 )

#Делаем заголовок
plt.title("Количество пар в неделю", family = 'serif', size = 14, weight = 'bold')

#Поворачиваем подписи в диагональ
ax.set_xticks(subjects, labels = subjects, rotation = 45)

#Выводим график
plt.show()

