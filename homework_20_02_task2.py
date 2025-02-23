def check(words):
    #ПЕРВАЯ ПРОВЕРКА
    flcounter = {i[0]: [0] for i in words}
    llcounter = {i[-1]: [0] for i in words}
    all_letters = set()
    start = -1
    end = -1
    for i in words:
        all_letters.add(i[0])
        all_letters.add(i[-1])
        flcounter[i[0]][0] = flcounter[i[0]][0] + 1
        llcounter[i[-1]][0] = llcounter[i[-1]][0] + 1
    for i in all_letters:
        diff = flcounter[i][0] - flcounter[i][0]
        if abs(diff) > 1:
            return 'Error1'
        if diff == 1 and start == -1:
            start = i
        elif diff == 1:
            return 'Error1'
        if diff == -1 and end == -1:
            end = i
        elif diff == -1:
            return 'Error1'
    if start == -1:
        start = all_letters.pop()
        all_letters.add(start)
        
    #ВТОРАЯ ПРОВЕРКА
    #матрица смежности
    graph = {}
    for letter in all_letters:
        graph[letter] = set()
    for word in words:
        graph[word[0]].add(word)

    #обход
    not_visited = all_letters
    gray = set()
    while True:
        not_visited.discard(start)
        if len(graph[start]) > 1:
            gray.add(start)
            start = graph[start].pop()[-1]
        elif len(graph[start]) == 1:
            gray.discard(start)
            start = graph[start].pop()[-1]
        else:
            gray.discard(start)
            if len(gray) == 0 and len(not_visited) != 0:
                return 'Error2'
            elif len(gray) == 0:
                return True
            else:
                start = gray.pop()

words = input().split()
flag = check(words)
if flag == True:
    print('True')
else:
    print(flag)
