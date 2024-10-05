import matplotlib.pyplot as plt
import numpy as np

#Задаём списки данных
numbers_of_lessons = [4, 4, 3, 3, 2, 2, 2, 1]
subjects = ["Общая физика", "Математический анализ", "Химия", "Информатика","Аналитическая геометрия", "Иностранный язык", "Физическая культура", "Безопасность жизнедеятельности"]
colors = ['purple', 'pink', 'goldenrod', 'ivory', 'lightgreen', 'navy', 'teal', 'tan']

#Строим диаграмму
fig, ax = plt.subplots(figsize=(12, 8), layout = 'constrained')
wedges = plt.pie(numbers_of_lessons, colors = colors, textprops = {'family': 'monospace', 'size': 10, 'style': 'italic'},
        wedgeprops=dict(width=0.5), autopct='%1.f%%')[0]

#Добавляем контур
for i, wedge in enumerate(wedges):
    wedge.set_edgecolor('black')
    wedge.set_alpha(0.5)

#Добавляем легенду
plt.title("Количество пар в неделю", family = 'serif', size = 14, weight = 'bold')
ax.legend(subjects, title="Предмет", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize = 10)

#Выводим диаграмму
plt.show()

