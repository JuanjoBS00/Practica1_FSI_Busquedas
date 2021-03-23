# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                       , search.romania)
zc = search.GPSProblem('Z', 'C'
                       , search.romania)
sn = search.GPSProblem('S', 'N'
                       , search.romania)
lg = search.GPSProblem('L', 'G'
                       , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())
#print(search.branch_and_bound_search(ab).path())
#print(search.branch_and_bound_subestimation_search(ab).path())


print("Traslado de Arad a Bucarest")
print("\nBúsqueda en anchura")
nodeBFS, visitedNodesBFS = search.breadth_first_graph_search(ab)
print("\nRuta obtenida: " + str(nodeBFS.path()))
print("\nNodos visitados: " + str(visitedNodesBFS))

print("\nBúsqueda en profundidad")
nodeDFS, visitedNodesDFS = search.depth_first_graph_search(ab)
print("\nRuta obtenida: " + str(nodeDFS.path()))
print("\nNodos visitados: " + str(visitedNodesDFS))

print("\nComparación entre las búsquedas BnB con y sin subestimación")
nodeBB, visitedNodesBB = search.branch_and_bound_search(ab)
nodeBBS, visitedNodesBBS = search.branch_and_bound_subestimation_search(ab)
print("Sin subestimación: " + str(nodeBB.path()) + "\nCon subestimación: " + str(nodeBBS.path()))
print("Sin subestimación: " + str(visitedNodesBB) + "\nCon subestimación: " + str(visitedNodesBBS))

print("----------------------------------------------------------------------------------------------------------")

print("Traslado de Oradea a Eforie")
print("\nBúsqueda en anchura")
nodeBFS, visitedNodesBFS = search.breadth_first_graph_search(oe)
print("\nRuta obtenida: " + str(nodeBFS.path()))
print("\nNodos visitados: " + str(visitedNodesBFS))

print("\nBúsqueda en profundidad")
nodeDFS, visitedNodesDFS = search.depth_first_graph_search(oe)
print("\nRuta obtenida: " + str(nodeDFS.path()))
print("\nNodos visitados: " + str(visitedNodesDFS))

print("\nComparación entre las búsquedas BnB con y sin subestimación")
nodeBB, visitedNodesBB = search.branch_and_bound_search(oe)
nodeBBS, visitedNodesBBS = search.branch_and_bound_subestimation_search(oe)
print("Sin subestimación: " + str(nodeBB.path()) + "\nCon subestimación: " + str(nodeBBS.path()))
print("Sin subestimación: " + str(visitedNodesBB) + "\nCon subestimación: " + str(visitedNodesBBS))

print("----------------------------------------------------------------------------------------------------------")

print("Traslado de Zerind a Craiova")
print("\nBúsqueda en anchura")
nodeBFS, visitedNodesBFS = search.breadth_first_graph_search(zc)
print("\nRuta obtenida: " + str(nodeBFS.path()))
print("\nNodos visitados: " + str(visitedNodesBFS))

print("\nBúsqueda en profundidad")
nodeDFS, visitedNodesDFS = search.depth_first_graph_search(zc)
print("\nRuta obtenida: " + str(nodeDFS.path()))
print("\nNodos visitados: " + str(visitedNodesDFS))

print("\nComparación entre las búsquedas BnB con y sin subestimación")
nodeBB, visitedNodesBB = search.branch_and_bound_search(zc)
nodeBBS, visitedNodesBBS = search.branch_and_bound_subestimation_search(zc)
print("Sin subestimación: " + str(nodeBB.path()) + "\nCon subestimación: " + str(nodeBBS.path()))
print("Sin subestimación: " + str(visitedNodesBB) + "\nCon subestimación: " + str(visitedNodesBBS))

print("----------------------------------------------------------------------------------------------------------")

print("Traslado de Sibiu a Neamt")
print("\nBúsqueda en anchura")
nodeBFS, visitedNodesBFS = search.breadth_first_graph_search(sn)
print("\nRuta obtenida: " + str(nodeBFS.path()))
print("\nNodos visitados: " + str(visitedNodesBFS))

print("\nBúsqueda en profundidad")
nodeDFS, visitedNodesDFS = search.depth_first_graph_search(sn)
print("\nRuta obtenida: " + str(nodeDFS.path()))
print("\nNodos visitados: " + str(visitedNodesDFS))

print("\nComparación entre las búsquedas BnB con y sin subestimación")
nodeBB, visitedNodesBB = search.branch_and_bound_search(sn)
nodeBBS, visitedNodesBBS = search.branch_and_bound_subestimation_search(sn)
print("Sin subestimación: " + str(nodeBB.path()) + "\nCon subestimación: " + str(nodeBBS.path()))
print("Sin subestimación: " + str(visitedNodesBB) + "\nCon subestimación: " + str(visitedNodesBBS))

print("----------------------------------------------------------------------------------------------------------")

print("Traslado de Lugoj a Giurgiu")
print("\nBúsqueda en anchura")
nodeBFS, visitedNodesBFS = search.breadth_first_graph_search(lg)
print("\nRuta obtenida: " + str(nodeBFS.path()))
print("\nNodos visitados: " + str(visitedNodesBFS))

print("\nBúsqueda en profundidad")
nodeDFS, visitedNodesDFS = search.depth_first_graph_search(lg)
print("\nRuta obtenida: " + str(nodeDFS.path()))
print("\nNodos visitados: " + str(visitedNodesDFS))

print("\nComparación entre las búsquedas BnB con y sin subestimación")
nodeBB, visitedNodesBB = search.branch_and_bound_search(lg)
nodeBBS, visitedNodesBBS = search.branch_and_bound_subestimation_search(lg)
print("Sin subestimación: " + str(nodeBB.path()) + "\nCon subestimación: " + str(nodeBBS.path()))
print("Sin subestimación: " + str(visitedNodesBB) + "\nCon subestimación: " + str(visitedNodesBBS))


#Recorrido de Arad a Bucarest
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# DFS
# [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>] : 101 + 138 + 120 + 75 + 70 + 111 + 118 = 733
# BNB
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418

#Parte 2. Tomar 5 pares de ciudades y comprobar que uno visitan menos nodos que otro.
# Los mismos nodos son el resultado final pero uno visita mucho menos nodos que otro
