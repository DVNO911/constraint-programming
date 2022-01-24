from z3 import *
blocks = 3
platforms = 4
iterations = 4
block1_goal = 1
block2_goal = 2
block3_goal = 0
print('Parameters are:')
print(blocks, 'blocks,', platforms, 'platforms,', iterations, 'iterations')
# ~~~~~~~~~~~~~~~~~~~~~Vars~~~~~~~~~~~~~~~~~~~~~
on = [[[Bool("on_%s_%s_%s" % (i, j, k)) for k in range(iterations+1)] for j in range(platforms)] for i in range(blocks)]
obj = [[Bool("obj_%s_%s" % (i,k)) for k in range(iterations+1)] for i in range(blocks)]
frm = [[Bool("frm_%s_%s" % (i,k)) for k in range(iterations+1)] for i in range(platforms)]
to = [[Bool("to_%s_%s" % (i,k)) for k in range(iterations+1)] for i in range(platforms)]
s = Optimize()
# ~~~~~~~~~~~~~~~~~~~~~Constraints~~~~~~~~~~~~~~~~~~~~~
# Not more than one block in the same place
cond3 = [
    Implies(on[i][j][k], And([Not(on[block][j][k]) for block in range(blocks) if block != i])
           ) for i in range(blocks) for j in range(platforms) for k in range(iterations+1)
]
# We cannot move a block to a tower where there already is a block
cond4 = [
    Implies(And([on[i][j][k], Or([on[block][j2][k] for block in range(blocks) if block!=i])]), Not(And([obj[i][k],to[j2][k]])))
    for i in range(blocks) for j in range(platforms) for j2 in range(platforms) if j2 != j for k in range(iterations+1)
]
# If we move a block from a certain platform then variable frm will only be true for that platform
cond5 = [
    Implies(And([on[i][j][k],obj[i][k]]), And([frm[j][k], And([Not(frm[tw][k]) for tw in range(platforms) if tw != j])]))
    for i in range(blocks) for j in range(platforms) for k in range(iterations+1)
]
# Only one variable to being true for each time-step
cond6 = [
    to[j][k] == And([Not(to[tw][k]) for tw in range(platforms) if tw != j])
    for j in range(platforms) for k in range(iterations+1)
]
# We can only move one block at each time-step
cond7 = [
    obj[i][k] == And([Not(obj[disk][k]) for disk in range(blocks) if disk != i])
    for i in range(blocks) for k in range(iterations+1)
]
# If a block is not moving at a certain time-step it will be on the same platform and nowhere else on the following step
cond8 = [
    Implies(And([Not(obj[i][k]),on[i][j][k]]), And([on[i][j][k+1], And([Not(on[i][tw][k+1]) for tw in range(platforms) if tw!=j])]))
    for i in range(blocks) for j in range(platforms) for k in range(iterations)
]
# It is not allowed to move a block from a platform to the same one
cond9 = [
    Implies(frm[j][k], Not(to[j][k]))
    for j in range(platforms) for k in range(iterations+1)
]
# If we move a block from a platform to another one, then the block will be on the latter and nowhere else on the following step
cond10 = [
    Implies(And([obj[i][k], frm[j][k], to[j2][k]]), And([on[i][j2][k+1], And([Not(on[i][tw][k+1]) for tw in range(platforms) if tw!=j2])]))
    for i in range(blocks) for j in range(platforms) for j2 in range(platforms) if j2 != j for k in range(iterations)
]
goal_cond1 = [
    And([on[0][0][0], on[0][block1_goal][iterations]])
]
goal_cond2 = [
    And([on[1][1][0], on[1][block2_goal][iterations]])
]
goal_cond3 = [
    And([on[2][2][0], on[2][block3_goal][iterations]])
]
s.add(cond3)
s.add(cond4)
s.add(cond5)
s.add(cond6)
s.add(cond7)
s.add(cond8)
s.add(cond9)
s.add(cond10)
s.add(goal_cond1)
s.add(goal_cond2)
s.add(goal_cond3)
s.check()
pp(cond4)

#print(s.model())
m = s.model()
print("first platform block1: ", m[on[0][0][iterations]])
print("first platform block2: ", m[on[1][0][iterations]])
print("first platform block3: ", m[on[2][0][iterations]])
print("target platform block1: ", m[on[0][block1_goal][iterations]])
print("target platform block2: ", m[on[1][block2_goal][iterations]])
print("target platform block3: ", m[on[2][block3_goal][iterations]])
fr = 0
dest = 0

for t in range(iterations+1):
    for d in range(blocks):
        for tw in range(platforms):
            if m[obj[d][t]]:
                if m[frm[tw][t]] == True:
                    fr = tw
                if m[to[tw][t]] == True:
                    dest = tw
        if m[obj[d][t]]:
            if t < iterations:
                print('moving block', d, 'at timestep', t+1, ' from ', fr,'to',dest)
if(m[on[0][block1_goal][iterations]] and m[on[1][block2_goal][iterations]] and m[on[2][block3_goal][iterations]]):
    print('solved puzzle in ', iterations, 'timesteps')
else:
    print('could not solve puzzle!')
