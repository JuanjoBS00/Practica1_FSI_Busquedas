# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                       , search.romania)
zc = search.GPSProblem('Z', 'C'
                       , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())
#print(search.branch_and_bound_search(ab).path())
#print(search.branch_and_bound_subestimation_search(ab).path())


print("Recorrido de Arad a Bucarest")
nodeBB, expandedNodesBB = search.branch_and_bound_search(ab)
nodeBBSubestimation, expandedNodesBBSubestimation = search.branch_and_bound_subestimation_search(ab)
print("Without heuristic: " + str(nodeBB.path()) + "\nWith heuristic: " + str(nodeBBSubestimation.path()))
print("Without heuristic: " + str(expandedNodesBB) + "\nWith heuristic: " + str(expandedNodesBBSubestimation))

print("Recorrido de Oradea a Eforie")
nodeBB, expandedNodesBB = search.branch_and_bound_search(oe)
nodeBBSubestimation, expandedNodesBBSubestimation = search.branch_and_bound_subestimation_search(oe)
print("Without heuristic: " + str(nodeBB.path()) + "\nWith heuristic: " + str(nodeBBSubestimation.path()))
print("Without heuristic: " + str(expandedNodesBB) + "\nWith heuristic: " + str(expandedNodesBBSubestimation))

print("Recorrido de Zerind a Craiova")
nodeBB, expandedNodesBB = search.branch_and_bound_search(zc)
nodeBBSubestimation, expandedNodesBBSubestimation = search.branch_and_bound_subestimation_search(zc)
print("Without heuristic: " + str(nodeBB.path()) + "\nWith heuristic: " + str(nodeBBSubestimation.path()))
print("Without heuristic: " + str(expandedNodesBB) + "\nWith heuristic: " + str(expandedNodesBBSubestimation))


# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# DFS
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 101 + 138 + 120 + 75 + 70 + 111 + 118 = 733
# BNB
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418

#Parte 2. Tomar 5 pares de ciudades y comprobar que uno visitan menos nodos que otro.
# Los mismos nodos son el resultado final pero uno visita mucho menos nodos que otro
