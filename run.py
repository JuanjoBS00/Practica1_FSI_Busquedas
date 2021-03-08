# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.branch_and_bound_search(ab).path())

# Result:
# BFS
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# DFS
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 101 + 138 + 120 + 75 + 70 + 111 + 118 = 733
# BNB
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
