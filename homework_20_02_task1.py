#ввод
n = int(input())
trust_len = int(input())
trust = [tuple(map(int, input().split())) for i in range(trust_len)]

#матрица смежности
graph = {}
for person in range (1, n+1):
    graph[person] = []
for edge in trust:
    graph[edge[0]].append(edge[1])

judge = -1
for person in range (1, n+1):
    flag = True
    for key in graph:
        if key == person:
            if graph[key] != []:
                flag = False
                break
        elif not person in graph[key]:
            flag = False
            break
    if flag == True:
        judge = person
        break
print(judge)
