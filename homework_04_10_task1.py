import numpy as np
import matplotlib.pyplot as plt

#Задаём массивы данных
concentrations = np.array ([0.01, 0.02, 0.03, 0.04, 0.05])
time1 = np.array ([156, 72, 46, 32, 24])
time2 = np.array ([77, 37, 26, 18, 14])
speed1 = 1/time1
speed2 = 1/time2

def approximation(X, Y):
    k, b = np.polyfit (X, Y, 1)
    new_X = np.linspace (np.min(X), np.max(X), np.size(X))
    new_Y = k*X + b
    return new_X, new_Y

x1, y1 = approximation(concentrations, speed1)
x2, y2 = approximation(concentrations, speed2)

#Строим график
fig, ax = plt.subplots(figsize=(12, 9), layout = 'constrained')
ax.plot(x2, y2, label = 'T = 307 K', color = 'crimson')
ax.plot(x1, y1, label = 'T = 297 K', color = 'goldenrod')
ax.scatter(concentrations, speed1, s = 15, facecolor = 'goldenrod', edgecolor = 'black')
ax.scatter(concentrations, speed2, s = 15, facecolor = 'crimson', edgecolor = 'black')

#Делаем заголовок и подписи
ax.set_title('Зависимость скорости реакции $Na_2S_2O_3$ и $H_2SO_4$ \nот концентрации $Na_2S_2O_3$ \n ', family = 'serif', size = 14, )
ax.legend()
ax.set_ylabel('\nСкорость реакции', labelpad = 14, family = 'monospace', size = 12) 
ax.set_xlabel('Концентрация $Na_2S_2O_3$ \n', labelpad = 14, family = 'monospace', size = 12) 

#Строим сетку
ax.grid(True, which = 'major', color = 'navy', linestyle = '-', linewidth = 0.25)
ax.grid(True, which = 'minor', color = 'navy', linestyle = '--', linewidth = 0.15)

#Рисуем стрелки на осях
ax.set_xlim(0, 0.06)
ax.set_ylim(0, 0.08)
plt.arrow(0, 0, 0.0615, 0, width = 0.0001, head_width = 0.001, head_length = 0.0005, fc = 'black', ec = 'black', clip_on = False)
plt.arrow(0, 0, 0, 0.085, width = 0.00004, head_width = 0.0004, head_length = 0.0008, fc = 'black', ec = 'black', clip_on = False)

#Делаем шкалу
ax.set_yticks(np.arange(0, 0.081, 0.01), labels = np.arange(0, 0.081, 0.01), rotation = 45)
ax.set_yticks(np.arange(0, 0.08, 0.002), minor = True)
ax.set_xticks(np.arange(0, 0.061, 0.01), labels = np.arange(0, 0.061, 0.01), rotation = 45)
ax.set_xticks(np.arange(0, 0.06, 0.002), minor = True)

#Выводим график
fig.show()
