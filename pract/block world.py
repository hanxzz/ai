class Strips(object):
 def __init__(self, name, preconds, effects, cost=1):
 self.name = name
 self.preconds = preconds
 self.effects = effects
 self.cost = cost
def __repr__(self):
 return self.name
class STRIPS_domain(object):
 def __init__(self, feats_vals, actions):
 self.feats_vals = feats_vals
 self.actions = actions
class Planning_problem(object):
 def __init__(self, prob_domain, initial_state, goal):
 self.prob_domain = prob_domain
 self.initial_state = initial_state
 self.goal = goal
boolean = {True, False}
### blocks world
def move(x,y,z):
 """string for the 'move' action"""
 return 'move_'+x+'_from_'+y+'_to_'+z
def on(x):
 """string for the 'on' feature"""
 return x+'_is_on'
def clear(x):
 """string for the 'clear' feature"""
 return 'clear_'+x
def create_blocks_world(blocks = {'a','b','c','d'}):
 blocks_and_table = blocks | {'table'}
 stmap = {Strips(move(x,y,z),{on(x):y, clear(x):True, clear(z):True},
 {on(x):z, clear(y):True, clear(z):False})}
 for x in blocks:
 for y in blocks_and_table:
 for z in blocks:
 if x!=y and y!=z and z!=x:
 stmap.update({Strips(move(x,y,'table'), {on(x):y, clear(x):True},
33 | Page {on(x):'table', clear(y):True})})
 for x in blocks:
 for y in blocks:
 for z in blocks:
 if x!=y:
 feats_vals = {on(x):blocks_and_table-{x} for x in blocks}
 feats_vals.update({clear(x):boolean for x in blocks_and_table})
 return STRIPS_domain(feats_vals, stmap)
 blocks1dom = create_blocks_world({'a','b','c'})
 blocks1 = Planning_problem(blocks1dom,
 {on('a'):'table', clear('a'):True,
 on('b'):'c', clear('b'):True,
 on('c'):'table', clear('c'):False}, # initial state
 {on('a'):'b', on('c'):'a'}) #goal
 blocks2dom = create_blocks_world({'a','b','c','d'})
 tower4 = {clear('a'):True, on('a'):'b',
 clear('b'):False, on('b'):'c',
 clear('c'):False, on('c'):'d',
 clear('d'):False, on('d'):'table'}
 blocks2 = Planning_problem(blocks2dom,
 tower4, # initial state
 {on('d'):'c',on('c'):'b',on('b'):'a'}) #goal
 blocks3 = Planning_problem(blocks2dom,
 tower4, # initial state
 {on('d'):'a', on('a'):'b', on('b'):'c'}) #goal