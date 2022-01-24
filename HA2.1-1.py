from gurobipy import *
import csv
from gurobipy import *
import pathlib
jobpath = pathlib.Path.cwd() / "jobs" / "ft06"

with open(jobpath, newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

(num_tasks, num_machines) = data[6][0].split()
num_machines = int(num_machines)
num_tasks = int(num_tasks)
machines = [i for i in range(num_machines)];
job_data = []

for i in range(len(data) - 7):
    job_int = []
    for j in range(0, num_tasks * 2, 2):
        a = data[i + 7][0].split()
        a = list(map(int,a))
        job_int.append([a[j], a[j + 1]])
    job_data.append(job_int)

Problem = job_data
M = 0
jobs = num_machines
tasks = num_tasks
for j in range(jobs):
    for m in range(tasks):
        M += Problem[j][m][1]
print(M)
# ~~~~~~~~~~~~~~~~~~~~ Model ~~~~~~~~~~~~~~~~~~~~
model = Model("facility")

# ~~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~
t = model.addVars(jobs,tasks)  # Start time of each task
makespan = model.addVar() # Total time to complete jobs
y = model.addVars(jobs, jobs, tasks, vtype=GRB.BINARY) # Mutex variables

# ~~~~~~~~~~~~~~~~~~~~ Constraints ~~~~~~~~~~~~~~~~~~~~

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

# No task can be started before previous task is complete
for j in range(jobs):
    for m in range(tasks-1):
        model.addConstr(
            t[j,m]+Problem[j][m][1] <= t[j,m+1]
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

# ~~~~~~~~~~~~~~~~~~~~ Objective Function ~~~~~~~~~~~~~~~~~~~~
model.setObjective(makespan, GRB.MINIMIZE)

# ~~~~~~~~~~~~~~~~~~~~ Optimize ~~~~~~~~~~~~~~~~~~~~
model.optimize()
print(model.display())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(makespan)