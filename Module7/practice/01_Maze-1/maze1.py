# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)

# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    # список смежности
    [1],             # 0
    [0, 4],          # 1
    [5],             # 2
    [4, 6],          # 3
    [1, 3, 5],       # 4
    [2, 4],         # 5
    [3],            # 6
    [8],             # 7
    [7],             # 8
]
def can_reach_bank(graph, home, bank):
    visited = set()
    stack = [home]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == bank[0] or node == bank[1]:
            return "Можно дойти до банка"
        stack.extend(graph[node])
        return "Невозможно дойти до банка"

print(can_reach_bank(graph, 0, [7, 8]))

# Решите задачу и выведите ответ в нужном формате
