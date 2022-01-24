# Add a vertex to the dictionary
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

def heuristic(graph, start, goal):
    x1 = graph.get(start)[0][0]
    x2 = graph.get(goal)[0][0]
    y1 = graph.get(start)[0][1]
    y2 = graph.get(goal)[0][1]
    return abs(x1 - x2) + abs(y1 - y2)

import queue
def a_star(graph, start, goal):
    O = queue.PriorityQueue()
    O.put((0, start)) # Queue is just ints of state names
    came_from = {}
    cost_so_far= {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not O.empty():
        current = O.get()
        current = current[1]
        if current == goal:
            break
        for next in range(len(graph.get(current))-1): #check neighbours
            new_cost = cost_so_far[current] + graph.get(current)[next+1][1]
            if new_cost > 1000:
                break
            if graph.get(current)[next+1][0] not in cost_so_far or new_cost < cost_so_far[graph.get(current)[next+1][0]]:
                cost_so_far[graph.get(current)[next+1][0]] = new_cost
                priority = new_cost + heuristic(graph, graph.get(current)[next+1][0], goal)
                O.put((priority, graph.get(current)[next + 1][0]))
                came_from[graph.get(current)[next+1][0]] = current

    return came_from, cost_so_far


###########################################----FIND PATH TIMES----################################################
sols = {}
speed = 0.2
(a, b) = a_star(graph,29,30)
for i in range(6):
    start = 29
    goal = i + 1
    (a, b) = a_star(graph, start, goal)
    sols[str(0) + '-' + str(goal)] = b[goal]*speed # Warehouse is now state 0 for solving purposes
    sols[str(goal) + '-' + str(0)] = b[goal]*speed # Warehouse is now state 0 for solving purposes
    # print('~~~~~~~~~~~~~~~~~~~')
    # print('goal:', goal)
    # print('a', a)
    # print('b', b)
    # print('akeys ',list(a))
    # print('cost to goal', b[goal])
    # print('~~~~~~~~~~~~~~~~~~~')
for i in range(6):
    for j in range(6):
        start = i+1
        goal = j+1
        if(start!=goal):
            (a, b) = a_star(graph, start, goal)
            sols[str(start) + '-' + str(goal)] = b[goal]*speed
            sols[str(goal) + '-' + str(start)] = b[goal]*speed
for i in range(6):
    start = i+1
    goal = 30
    (a, b) = a_star(graph, start, goal)
    sols[str(start) + '-' + str(7)] = b[goal]*speed # Delivery is now state 0 for solving purposes
    sols[str(7) + '-' + str(start)] = b[goal]*speed # Delivery is now state 0 for solving purposes
#print(sols)
Traveltime = sols

#######################################---------------------GUROBI---------------------#############################################
from gurobipy import *
import csv
from gurobipy import *
import pathlib
from timeit import default_timer as timer
jobpath = pathlib.Path.cwd() / "jobs" / "ft06"

with open(jobpath, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

(num_tasks, num_machines) = data[6][0].split()
jobs = int(num_machines)
tasks = int(num_tasks)
Problem = []
for i in range(len(data) - 7):
    job_int = []
    for j in range(0, tasks * 2, 2):
        a = data[i + 7][0].split()
        a = list(map(int,a))
        job_int.append([a[j], a[j + 1]])
    Problem.append(job_int)

M = 0
for j in range(jobs):
    for m in range(tasks):
        M += Problem[j][m][1]
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Model ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
model = Model("facility")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
t = model.addVars(jobs,tasks)  # Start time of each task
makespan = model.addVar() # Total time to complete jobs
y = model.addVars(jobs, jobs, tasks, vtype=GRB.BINARY) # Mutex variables

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Constraints ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# BOUNDS
for j in range(jobs):
    for m in range(tasks):
        model.addConstr(
            t[j,m] >= 0
        )

for j in range(jobs):
    for m in range(tasks):
        model.addConstr(
            t[j,m]+Problem[j][m][1] <= makespan
        )

# No task can be started before previous task is complete and travelled there
for j in range(jobs):
    for m in range(tasks-1):
        model.addConstr(
            t[j,m]+Problem[j][m][1] + Traveltime[str(Problem[j][m-1][0]+1) + '-' + str(Problem[j][m][0]+1)] <= t[j,m+1]
        )

# Mutex Constraint
for job1 in range(jobs):
    for job2 in range(jobs):
        for t1 in range(tasks):
            for t2 in range(tasks):
                if job1 != job2:
                    if Problem[job1][t1][0] == Problem[job2][t2][0]:
                        model.addConstr(
                            t[job1, t1] >= t[job2, t2] + Problem[job2][t2][1] - M*y[job1, job2, t1]
                        )

for job1 in range(jobs):
    for job2 in range(jobs):
        for t1 in range(tasks):
            for t2 in range(tasks):
                if job1 != job2:
                    if Problem[job1][t1][0] == Problem[job2][t2][0]:
                        model.addConstr(
                        t[job2, t2] >= t[job1, t1] + Problem[job1][t1][1] - M*(1-y[job1,job2,t1])
                        )

# Add traveltime to last task of each job
for j in range(jobs):
    for m in range(tasks):
        model.addConstr(
            t[j,m]+Problem[j][m][1] + Traveltime[str(Problem[j][m-1][0]+1) + '-' + str(7)] <= makespan
        )

#Cannot start the first task before it has travelled there
for j in range(jobs):
    model.addConstr(
        t[j,0] >=Traveltime[str(0) + '-' + str(Problem[j][1][0]+1)]
    )
# ~~~~~~~~~~~~~~~~~~~~ Objective Function ~~~~~~~~~~~~~~~~~~~~
model.setObjective(makespan, GRB.MINIMIZE)

# ~~~~~~~~~~~~~~~~~~~~ Optimize ~~~~~~~~~~~~~~~~~~~~
model.optimize()
print(model.display())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(makespan)
print(sols)
