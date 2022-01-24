from z3 import *
disks = 3
towers = 3
iterations = 99
print('Parameters are:')
print(disks, 'disks,', towers, 'towers,', iterations, 'iterations')
# ~~~~~~~~~~~~~~~~~~~~~Vars~~~~~~~~~~~~~~~~~~~~~
on = [[[Bool("on_%s_%s_%s" % (i, j, k)) for k in range(iterations+1)] for j in range(towers)] for i in range(disks)]
obj = [[Bool("obj_%s_%s" % (i,k)) for k in range(iterations+1)] for i in range(disks)]
frm = [[Bool("frm_%s_%s" % (i,k)) for k in range(iterations+1)] for i in range(towers)]
to = [[Bool("to_%s_%s" % (i,k)) for k in range(iterations+1)] for i in range(towers)]
s = Optimize()
# ~~~~~~~~~~~~~~~~~~~~~Constraints~~~~~~~~~~~~~~~~~~~~~
# If a disk is on a tower and a smaller disk is on the same tower, then the disk cannot be moved
cond3 = [
    Implies(And([on[i][j][k], Or([on[disk][j][k] for disk in range(i)])]), Not(obj[i][k]))
    for i in range(disks) if i != 0 for j in range(towers) for k in range(iterations+1)
]
# We cannot move a disk to a tower where there already is a smaller disk
cond4 = [
    Implies(And([on[i][j][k], Or([on[disk][j2][k] for disk in range(i)])]), Not(And([obj[i][k],to[j2][k]])))
    for i in range(disks) if i != 0 for j in range(towers) for j2 in range(towers) if j2 != j for k in range(iterations+1)
]
# If we move a disk from a certain tower then variable frm will only be true for that tower
cond5 = [
    Implies(And([on[i][j][k],obj[i][k]]), And([frm[j][k], And([Not(frm[tw][k]) for tw in range(towers) if tw != j])]))
    for i in range(disks) for j in range(towers) for k in range(iterations+1)
]
# Only one variable to being true for each time-step
cond6 = [
    to[j][k] == And([Not(to[tw][k]) for tw in range(towers) if tw != j])
    for j in range(towers) for k in range(iterations+1)
]
# We can only move one disk at each time-step
cond7 = [
    obj[i][k] == And([Not(obj[disk][k]) for disk in range(disks) if disk != i])
    for i in range(disks) for k in range(iterations+1)
]
# If a disk is not moving at a certain time-step it will be on the same tower and nowhere else on the following step
cond8 = [
    Implies(And([Not(obj[i][k]),on[i][j][k]]), And([on[i][j][k+1], And([Not(on[i][tw][k+1]) for tw in range(towers) if tw!=j])]))
    for i in range(disks) for j in range(towers) for k in range(iterations)
]
# It is not allowed to move a disk from a tower to the same one
cond9 = [
    Implies(frm[j][k], Not(to[j][k]))
    for j in range(towers) for k in range(iterations+1)
]
# If we move a disk from a tower to another one, then the disk will be on the latter and nowhere else on the following step
cond10 = [
    Implies(And([obj[i][k], frm[j][k], to[j2][k]]), And([on[i][j2][k+1], And([Not(on[i][tw][k+1]) for tw in range(towers) if tw!=j2])]))
    for i in range(disks) for j in range(towers) for j2 in range(towers) if j2 != j for k in range(iterations)
]
# The disks are on the first tower at the first time step and on the last one at the step ts
cond11 = [
    And([on[i][0][0], on[i][towers-1][iterations]])
    for i in range(disks)
]
s.add(cond3)
s.add(cond4)
s.add(cond5)
s.add(cond6)
s.add(cond7)
s.add(cond8)
s.add(cond9)
s.add(cond10)
s.add(cond11)

s.check()
#pp(cond10)

#print(s.model())
#pp(on[2][towers-1][iterations])
m = s.model()
#print("first tower disk1: ", m[on[0][0][iterations]])
#print("first tower disk2: ", m[on[1][0][iterations]])
#print("first tower disk3: ", m[on[2][0][iterations]])
#print("target tower disk1: ", m[on[0][towers-1][iterations]])
#print("target tower disk2: ", m[on[1][towers-1][iterations]])
#print("target tower disk3: ", m[on[2][towers-1][iterations]])
fr = 0
dest = 0

for t in range(iterations+1):
    for d in range(disks):
        for tw in range(towers):
            if m[obj[d][t]]:
                if m[frm[tw][t]] == True:
                    fr = tw
                if m[to[tw][t]] == True:
                    dest = tw
        if m[obj[d][t]]:
            if t < iterations:
                print('moving disk', d, 'at timestep', t+1, ' from ', fr,'to',dest)
if(m[on[0][towers-1][iterations]] and m[on[1][towers-1][iterations]] and m[on[2][towers-1][iterations]]):
    print('solved puzzle in ', iterations, 'timesteps')
else:
    print('could not solve puzzle!')
