import random
import numpy as np
import tcod #python3 -m pip install --user tcod

class Pathfinder:

    def prepareGraph(self, graph, start):
        # Change 0, P and D to 1, because 0 are obstacles here
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == 0 or isinstance(graph[i][j], str) and ("P" in graph[i][j] or "D" in graph[i][j]):
                    if isinstance(graph[i][j], str) and "A" in graph[i][j]:
                        continue
                    graph[i][j] = 1

        x = start[0]
        y = start[1]

        # Add agents to map
        if x - 1 >= 0:
            if isinstance(graph[x-1][y], str) and "A" in graph[x-1][y]:
                graph[x-1][y] = 0
        if x + 1 < len(graph):
            if isinstance(graph[x+1][y], str) and "A" in graph[x+1][y]:
                graph[x-1][y] = 0
        if y - 1 >= 0:
            if isinstance(graph[x][y-1], str) and "A" in graph[x][y-1]:
                graph[x][y-1] = 0
        if y + 1 < len(graph):
            if isinstance(graph[x][y+1], str) and "A" in graph[x][y+1]:
                graph[x][y+1] = 0

        print(graph)
        #Change not neighbour agents to 1 because they are not obstacles
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if isinstance(graph[i][j], str) and "A" in graph[i][j]:
                    graph[i][j] = 0

        # Change * to 0 for obstacles
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                if graph[i][j] == "*":
                    graph[i][j] = 0



        return graph

    def randomStep(self, graph, start):
        print("RANDOMSTEP INPUT", start)
        for i in range(4):
            x = start[0]
            y = start[1]
            j = random.randint(0, 3)
            print("HERE I AM",j)

            if j == 0:
                x += 1
                if x < len(graph[0]) and graph[x][y] == 1:
                    return x,y
            elif j == 1:
                x -= 1
                if x >= 0 and graph[x][y] == 1:
                    return x,y
            elif j == 2:
                y += 1
                if y < len(graph[0]) and graph[x][y] == 1:
                    return x,y
            elif j == 3:
                y -= 1
                if y >= 0 and graph[x][y] == 1:
                    return x,y
        return start[0], start[1]


    def solve(self, agentId, graph, start, end):
        print("SOLVER\\","agentId:",agentId, "start:", start,"end:", end)

        print(graph)


        self.x = start[0]
        self.y = start[1]
        preparedGraph = self.prepareGraph(graph, start)
        preparedGraph = graph.astype(dtype=np.int8, order="F")

        print(preparedGraph)
        tcodGraph = tcod.path.SimpleGraph(cost=preparedGraph,cardinal=1,diagonal=0)

        pf = tcod.path.Pathfinder(tcodGraph)
        pf.add_root(start)
        pf.resolve()

        solution = pf.path_to(end)

        if len(solution) > 1:
            self.x = np.uint32(solution[1][0]).item()
            self.y = np.uint32(solution[1][1]).item()
            return self.x, self.y
        else:
            x, y = self.randomStep(preparedGraph, start)
            print("x and y", x, y)
            return x, y
