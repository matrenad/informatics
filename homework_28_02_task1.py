#ввод
n = int(input('n = '))
dislikes_len = int(input('Количество рёбер = '))
dislikes = [tuple(map(int, input(f'Введите {i+1}-е ребро (два числа через пробел):' + '\n').split())) for i in range(dislikes_len)]

#матрица смежности
graph = {}
for person in range (1, n+1):
    graph[person] = []
for edge in dislikes:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
#так как в этой задаче ориентация ребра не играет роли, делаем из графа неориентированный

def is_bipartite_dfs(graph, node, colors=None, color=0):
    if colors is None:
        colors = {}  # Словарь для хранения цветов вершин
    
    if node in colors:
        return colors[node] == color  # Проверяем, что вершина уже окрашена правильно
    
    colors[node] = color  # Красим текущую вершину в текущий цвет
    
    for neighbor in graph[node]:
        # Рекурсивно проверяем соседей, окрашивая их в противоположный цвет
        if not is_bipartite_dfs(graph, neighbor, colors, 1 - color):
            return False
    
    return True

def check_bipartite(graph):
    colors = {}  # Словарь для хранения информации о цветах вершин
    for node in graph:
        if node not in colors:  # Проверяем каждую компоненту связности
            if not is_bipartite_dfs(graph, node, colors):
                return False  # Если хоть одна компонента не двудольная, возвращаем False
    return True

print("Граф двудольный" if check_bipartite(graph) else "Граф не двудольный")
