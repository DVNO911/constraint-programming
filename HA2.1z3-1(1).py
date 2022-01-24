from z3 import *
import csv
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
jobs = num_machines
tasks = num_tasks

#######################
# Model
s = Optimize()

# Variables
t = [[Int("t_%s_%s" % (i+1, j+1)) for j in range(jobs)] for i in range(tasks)]

y = [[[Int("y_%s_%s_%s" % (i+1, j+1, k+1)) for j in range(jobs)] for i in range(jobs)] for k in range(tasks)]
makespan = Int('makespan')

# Constraints

# BINARY
for i in range(jobs):
    for j in range(jobs):
        for k in range(tasks):
            s.add(
                y[i][j][k] >= 0
            )
for i in range(jobs):
    for j in range(jobs):
        for k in range(tasks):
            s.add(
            y[i][j][k] <= 1
            )

# BOUNDS
for j in range(jobs):
    for m in range(tasks):
        s.add(
            t[j][m] >= 0
        )

for j in range(jobs):
    for m in range(tasks):
        s.add(
            t[j][m]+Problem[j][m][1] <= makespan
        )

# No task can be started before previous task is complete
for j in range(jobs):
    for m in range(tasks-1):
        s.add(
            t[j][m]+Problem[j][m][1] <= t[j][m+1]
        )

# Mutex Constraint
#for job1 in range(jobs):
#    for job2 in range(jobs):
#        for m in range(tasks):
#            if job1 != job2:
#                s.add(
#                    Or(t[job1][m] >= t[job2][m] + Problem[job2][m][1], t[job2][m] >= t[job1][m] + Problem[job1][m][1])
#                )
mutex = [
        Or(
            t[job1][t1] >= t[job2][t2] + Problem[job2][t2][1],
            t[job2][t2] >= t[job1][t1] + Problem[job1][t1][1]
        )
            for job1 in range(jobs)
                for job2 in range(jobs)
                    for t1 in range(tasks)
                        for t2 in range(tasks)
                        if job1 != job2
                           if Problem[job1][t1][0] == Problem[job2][t2][0]
]
s.add(mutex)
# OBJECTIVE FN
s.minimize(makespan)

#Solve
s.check()
print(s.model())
m = s.model()
print("makespan: ", m[makespan])