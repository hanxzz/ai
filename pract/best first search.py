# This class represent a graph
class Graph:
 # Initialize the class
 def __init__(self, graph_dict=None, directed=True):
 self.graph_dict = graph_dict or {}
 self.directed = directed
 if not directed:
 self.make_undirected()
 # Create an undirected graph by adding symmetric edges
 def make_undirected(self):
 for a in list(self.graph_dict.keys()):
 for (b, dist) in self.graph_dict[a].items():
13 | Page self.graph_dict.setdefault(b, {})[a] = dist
 # Add a link from A and B of given distance, and also add the inverse link if the
graph is undirected
 def connect(self, A, B, distance=1):
 self.graph_dict.setdefault(A, {})[B] = distance
 if not self.directed:
 self.graph_dict.setdefault(B, {})[A] = distance
 # Get neighbors or a neighbor
 def get(self, a, b=None):
 links = self.graph_dict.setdefault(a, {})
 if b is None:
 return links
 else:
 return links.get(b)
 # Return a list of nodes in the graph
 def nodes(self):
 s1 = set([k for k in self.graph_dict.keys()])
 s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
 nodes = s1.union(s2)
 return list(nodes)
# This class represent a node
class Node:
 # Initialize the class
 def __init__(self, name:str, parent:str):
 self.name = name
 self.parent = parent
 self.g = 0 # Distance to start node
 self.h = 0 # Distance to goal node
 self.f = 0 # Total cost
 # Compare nodes
 def __eq__(self, other):
 return self.name == other.name
 # Sort nodes
 def __lt__(self, other):
 return self.f < other.f
 # Print node
 def __repr__(self):
 return ('({0},{1})'.format(self.position, self.f))
# Best-first search
def best_first_search(graph, heuristics, start, end):

 # Create lists for open nodes and closed nodes
 open = []
 closed = []
14 | Page # Create a start node and an goal node
 start_node = Node(start, None)
 goal_node = Node(end, None)
 # Add the start node
 open.append(start_node)

 # Loop until the open list is empty
 while len(open) > 0:
 # Sort the open list to get the node with the lowest cost first
 open.sort()
 # Get the node with the lowest cost
 current_node = open.pop(0)
 # Add the current node to the closed list
 closed.append(current_node)

 # Check if we have reached the goal, return the path
 if current_node == goal_node:
 path = []
 while current_node != start_node:
 path.append(current_node.name + ': ' + str(current_node.g))
 current_node = current_node.parent
 path.append(start_node.name + ': ' + str(start_node.g))
 # Return reversed path
 return path[::-1]
 # Get neighbours
 neighbors = graph.get(current_node.name)
 # Loop neighbors
 for key, value in neighbors.items():
 # Create a neighbor node
 neighbor = Node(key, current_node)
 # Check if the neighbor is in the closed list
 if(neighbor in closed):
 continue
 # Calculate cost to goal
 neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
 neighbor.h = heuristics.get(neighbor.name)
 neighbor.f = neighbor.h
 # Check if neighbor is in open list and if it has a lower f value
 if(add_to_open(open, neighbor) == True):
 # Everything is green, add neighbor to open list
 open.append(neighbor)
 # Return None, no path is found
 return None
# Check if a neighbor should be added to open list
15 | Pagedef add_to_open(open, neighbor):
 for node in open:
 if (neighbor == node and neighbor.f >= node.f):
 return False
 return True
# The main entry point for this module
def main():
 # Create a graph
 graph = Graph()
 # Create graph connections (Actual distance)
 graph.connect('Jaipur', 'Gurugram', 111)
 graph.connect('Jaipur', 'Mumbai', 85)
 graph.connect('Gurugram', 'Noida', 104)
 graph.connect('Gurugram', 'Sitapur', 140)
 graph.connect('Gurugram', 'Delhi', 183)
 graph.connect('Mumbai', 'Noida', 230)
 graph.connect('Mumbai', 'Kolkata', 67)
 graph.connect('Kolkata', 'Bilaspur', 191)
 graph.connect('Kolkata', 'Sitapur', 64)
 graph.connect('Noida', 'Delhi', 171)
 graph.connect('Noida', 'Madurai', 170)
 graph.connect('Noida', 'Pondicherry', 220)
 graph.connect('Sitapur', 'Delhi', 107)
 graph.connect('Bilaspur', 'Bern', 91)
 graph.connect('Bilaspur', 'Zurich', 85)
 graph.connect('Bern', 'Zurich', 120)
 graph.connect('Zurich', 'Memmingen', 184)
 graph.connect('Memmingen', 'Delhi', 55)
 graph.connect('Memmingen', 'Madurai', 115)
 graph.connect('Madurai', 'Delhi', 123)
 graph.connect('Madurai', 'Pondicherry', 189)
 graph.connect('Madurai', 'Raipur', 59)
 graph.connect('Raipur', 'Shimla', 81)
 graph.connect('Pondicherry', 'Lucknow', 102)
 graph.connect('Shimla', 'Lucknow', 126)
 # Make graph undirected, create symmetric connections
 graph.make_undirected()
 # Create heuristics (straight-line distance, air-travel distance)
 heuristics = {}
 heuristics['Bilaspur'] = 204
 heuristics['Bern'] = 247
 heuristics['Jaipur'] = 215
 heuristics['Kolkata'] = 137
 heuristics['Lucknow'] = 318
16 | Page heuristics['Mumbai'] = 164
 heuristics['Madurai'] = 120
 heuristics['Memmingen'] = 47
 heuristics['Noida'] = 132
 heuristics['Pondicherry'] = 257
 heuristics['Raipur'] = 168
 heuristics['Sitapur'] = 75
 heuristics['Shimla'] = 236
 heuristics['Gurugram'] = 153
 heuristics['Zurich'] = 157
 heuristics['Delhi'] = 0
 # Run search algorithm
 path = best_first_search(graph, heuristics, 'Jaipur', 'Delhi')
 print(path)
 print()
# Tell python to run main method
if __name__ == "__main__": main()