from z3 import *
def add_vertex(v, x, y):
  global graph
  global vertices_no
  if v in graph:
    print("Vertex ", v, " already exists.")
  else:
    vertices_no = vertices_no + 1
    graph[v] = []
    graph[v].append([x,y])

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
  global graph
  # Check if vertex v1 is a valid vertex
  if v1 not in graph:
    print("Vertex ", v1, " does not exist.")
  # Check if vertex v2 is a valid vertex
  elif v2 not in graph:
    print("Vertex ", v2, " does not exist.")
  else:
    # Since this code is not restricted to a directed or
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    temp = [v2, e]
    graph[v1].append(temp)

# Print the graph
def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

# driver code
graph = {}
# stores the number of vertices in the graph
vertices_no = 30
add_vertex(1, 73, 51), add_vertex(2, 53, 17), add_vertex(3, 91, 17), add_vertex(4, 28, 70), add_vertex(5, 28, 34)
add_vertex(6, 119, 70), add_vertex(7, 7, 70), add_vertex(8, 7, 51), add_vertex(9, 7, 34), add_vertex(10, 7, 17)
add_vertex(11, 7, 0), add_vertex(12, 28, 51), add_vertex(13, 28, 17), add_vertex(14, 28, 0), add_vertex(15, 53, 51)
add_vertex(16, 53, 34), add_vertex(17, 53, 0), add_vertex(18, 73, 70), add_vertex(19, 73, 34), add_vertex(20, 73, 17)
add_vertex(21, 91, 70), add_vertex(22, 91, 51), add_vertex(23, 91, 34), add_vertex(24, 91, 0), add_vertex(25, 119, 51)
add_vertex(26, 119, 34), add_vertex(27, 119, 17), add_vertex(28, 119, 0), add_vertex(29, 0, 34), add_vertex(30, 127, 34)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 18, 19), add_edge(1, 22, 18), add_edge(1, 19, 17), add_edge(1, 15, 20)
add_edge(2, 16, 17), add_edge(2, 20, 20), add_edge(2, 17, 17)
add_edge(3, 23, 17), add_edge(3, 27, 28), add_edge(3, 24, 17)
add_edge(4, 18, 45), add_edge(4, 7, 21)
add_edge(5, 12, 17), add_edge(5, 16, 25), add_edge(5, 9, 21)
add_edge(6, 21, 28)
add_edge(7, 4, 21), add_edge(7, 8, 19)
add_edge(8, 12, 21), add_edge(8, 9, 17), add_edge(8, 7, 19)
add_edge(9, 8, 17), add_edge(9, 5, 21), add_edge(9, 10, 17), add_edge(9, 29, 7)
add_edge(10, 9, 17), add_edge(10, 13, 21), add_edge(10, 11, 17)
add_edge(11, 10, 17), add_edge(11, 14, 21)
add_edge(12, 15, 25), add_edge(12, 5, 17), add_edge(12, 8, 21)
add_edge(13, 14, 17), add_edge(13, 10, 21)
add_edge(14, 13, 17), add_edge(14, 17, 25), add_edge(14, 11, 21)
add_edge(15, 1, 20), add_edge(15, 16, 17), add_edge(15, 12, 25)
add_edge(16, 15, 17), add_edge(16, 2, 17), add_edge(16, 5, 25)
add_edge(17, 2, 17), add_edge(17, 24, 38), add_edge(17, 14, 25)
add_edge(18, 21, 18), add_edge(18, 1, 19), add_edge(18, 4, 45)
add_edge(19, 1, 17), add_edge(19, 23, 18), add_edge(19, 20, 17)
add_edge(20, 19, 17), add_edge(20, 2, 20)
add_edge(21, 6, 28), add_edge(21, 22, 19), add_edge(21, 18, 18)
add_edge(22, 21, 19), add_edge(22, 25, 28), add_edge(22, 23, 17), add_edge(22, 1, 18)
add_edge(23, 22, 17), add_edge(23, 26, 28), add_edge(23, 3, 17), add_edge(23, 19, 18)
add_edge(24, 3, 17), add_edge(24, 28, 28), add_edge(24, 17, 38)
add_edge(25, 26, 17), add_edge(25, 22, 28)
add_edge(26, 25, 17), add_edge(26, 30, 8), add_edge(26, 27, 17), add_edge(26, 23, 28)
add_edge(27, 26, 17), add_edge(27, 28, 17), add_edge(27, 3, 28)
add_edge(28, 27, 17), add_edge(28, 24, 28)
add_edge(29, 9, 7)
add_edge(30, 26, 8)
##########################################################################################

s = Optimize()
nodecount= 30
node = [Bool("t_%s" % (i+1)) for i in range(30)]
#######################################################################################################################################'
# DICTIONARIES
nodedict = {} #nodedict[node] = [edge1, edge2, edge3, ... ]
nodedict[1] = [20, 26, 41, 21]
nodedict[2] = [18,23,19]
nodedict[3] = [30,35,31]
nodedict[4] = [11,6]
nodedict[5] = [13,14,8]
nodedict[6] = [32]
nodedict[7] = [6,2]
nodedict[8] = [2,7,3]
nodedict[9] = [3,8,4,1]
nodedict[10] = [4,9,5]
nodedict[11] = [5,10]
nodedict[12] = [12,13,7]
nodedict[13] = [15,9]
nodedict[14] = [15,16,10]
nodedict[15] = [41,17,12]
nodedict[16] = [17,18,14]
nodedict[17] = [19,24,16]
nodedict[18] = [25,20,11]
nodedict[19] = [21,27,22]
nodedict[20] = [22,23]
nodedict[21] = [32,28,25]
nodedict[22] = [28,33,29,26]
nodedict[23] = [29,34,30,27]
nodedict[24] = [31,36,24]
nodedict[25] = [37,33]
nodedict[26] = [37,40,38,34]
nodedict[27] = [38,39,35]
nodedict[28] = [39,36]
nodedict[29] = [1]
nodedict[30] = [40]

# use_edge[edge] = bool
use_edge = {}
for i in range(30):
  for next in range(len(nodedict[i+1])):
    use_edge[nodedict[i+1][next]] = Bool("edge_%s" % (nodedict[i+1][next]))

# edges_weight[edge] = weight
edges_weight = {}
for i in range(30):
  for next in range(len(graph.get(i+1))-1):
    edges_weight[nodedict[i+1][next]] = graph.get(i+1)[next+1][1]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ VARIABLES  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
node = [Bool("node_%s" % (i+1)) for i in range(30)]
# use_edge for booleansq
start = 5
goal = 3
start_node = node[start-1]
goal_node = node[goal-1]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  CONSTRAINTS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FORCE START AND GOAL NODE TRUE
# machine 5, machine 3 true
s.add(start_node == True)
s.add(goal_node == True)
# ONLY FOR START AND GOAL NODE
# Only one edge will be part of the path
# a+b+c = 1
exactly=[
    And(
        PbEq(((use_edge[nodedict[start][0]],1),(use_edge[nodedict[start][1]],1),(use_edge[nodedict[start][2]],1)),1),
        PbEq(((use_edge[nodedict[goal][0]],1),(use_edge[nodedict[goal][1]],1),(use_edge[nodedict[goal][2]],1)),1)
    )
]
s.add(exactly)

# FOR ALL OTHER NODES
# Node is part of the path or not
# 2A' + a + b + c = 2
# A' + A' + a + b + c = 2?
for i in range(30):
  x = [Not(node[i]), Not(node[i])]
  for j in range(len(nodedict[i+1])):
    x.append(use_edge[nodedict[i+1][j]])
  if (i!=start-1) and (i!=goal-1):
    s.add(
      PbEq([(x[i],1) for i in range(len(x))],2)
    )

# FIND NEW PATHS
sols = [[2, 3, 5, 16, 17, 24], [2, 3, 5, 16, 19, 20, 23], [1, 3, 5, 15, 16, 22, 23], [1, 3, 5, 12, 15, 22, 23], [1, 3, 5, 12, 15, 19, 23],
        [1, 3, 5, 15, 16, 19, 23], [3, 5, 9, 10, 11, 14, 17, 24], [3, 5, 9, 10, 13, 14, 17, 24], [1, 3, 5, 12, 15, 22, 25, 26, 27], [1, 3, 5, 15, 16, 22, 25, 26, 27]]
for i in range(len(sols)):
  path = []
  for j in range(len(sols[i])):
    path.append(node[sols[i][j]-1])
  s.add(
    PbLe( [(path[i],1) for i in range(len(path))],len(path)-1)
  )

# OBJECTIVE FUNCTION
s.minimize(Sum([If(use_edge[i+1],edges_weight[i+1],0) for i in range(41)]))
s.check()
m = s.model()
path = []
for i in range(30):
  if (m[node[i]] == True):
    path.append(i+1)
print(path)

'''
# this is how to manually use the EXACTLY ONE function
x=[[Bool('allo_res%s_op%s' % (i+1,j+1)) for j in range(5)] for i in range(5)]
# if I want n variables to be true out of the whole set:
n = 1
# this is how to manually use the EXACTLY ONE function
exactly=[
    And(
        PbEq(((x[0][0],1),(x[0][1],1)),n),
        PbEq(((x[1][0],1),(x[1][1],1)),n)
# N.B. the number 1 in the expression after the variable is required for the constraint to work
    )
]
print(exactly)
for j in range(5):
    for i in range(5):
        print(x[i][j])
# this is how to iterate the EXACTLY one constraint over a list of variables
exactly_2 = [
    PbGe( [    (x[i][j],1) for j in range(5)],n) for i in range(5)
]
print(exactly_2)
# it is possible to define also constraints such as AT MOST and AT LEAST just in the same way
#try to substitute PbEq with PbLe or PbGe
a, b, c = Bools('a b c')
f = PbEq(((a,1),(b,3),(c,2)), 2)
'''
######################################################################################
# SKRÄP

########################################################################
#n=1
#exactly_2 = [
#    PbGe([(use_edge[nodedict[i+1][j]],1) for j in range(len(nodedict[i+1]))],n) for i in range(30)
#    # PbGe([(x[i][j],1) for j in range(5)],n) for i in range(5)
#]
########################################################################
# DICT[NODE] = [BOOLEAN, WEIGHT, DESTINATION]

# DICT[EDGE] = [BOOLEAN, START, DEST]


'''
for i in range(nodecount):

    mega[i+1] = []
    for next in range(len(graph.get(i+1))-1):
        goahead = True

        dest = graph.get(i+1)[next+1][0]
        print(dest)
        if dest in mega:
          for nextt in range((len(graph.get(dest))-1)):
            print('lendest', (len(graph.get(dest))-1))
            print('nextt',nextt)
            print(mega[dest])
            print('wtf',graph.get(i)[next+1])
            if mega[dest][nextt][2] == graph.get(i)[next+1]:
              print(mega[dest][nextt][2])
              goahead = False
        #print('i',i,'  next+1',next+1)
        #mega[str(i+1)+'_'+str(next+1)] = Bool("e_%s" % (next+1))
        weight = 10
        if goahead:
          #mega[i].append([Bool("e_%s" % (next+1)), weight, dest])
          mega[i+1].append(['bool', 'w', dest])
          print('mega is currently' , mega)
'''