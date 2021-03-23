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