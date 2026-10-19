# In-degree, out-degree and Jaccard similarity
graph = {"A": ["B", "C"], "B": ["C"], "C": ["A"]}

for node in graph:
    indegree = sum(node in neighbours for neighbours in graph.values())
    outdegree = len(graph[node])
    print(node, "In-degree:", indegree, "Out-degree:", outdegree)

a, b = set(graph["A"]), set(graph["B"])
print("Jaccard similarity:", len(a & b) / len(a | b))
