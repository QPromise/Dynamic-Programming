graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}
def bfs(graph,s):
    queue=[]
    queue.append(s)
    seen=set()
    seen.add(s)
    while (len(queue)>0):
        vertex=queue.pop(0)
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)
bfs(graph,"A;  ")