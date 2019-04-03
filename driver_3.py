
from collections import deque
import time
from collections import defaultdict
import sys
import heapq
import math
import psutil
import os


#Four Direction
Four_Direction = ['Up', 'Down', 'Left', 'Right']

#initial state
Board = []

neighbors = defaultdict(dict)

Goal_state = [0,1,2,3,4,5,6,7,8]

#BFS, DFS, ast Algorithm Implementation
path_to_goal = []
cost_path = 0
nodes_expanded = 0
search_depth = 0
max_search_depth = 0

arg_V = []
#######################################################
		#Python CMD
#iterate list
def chains(*iterables):
	for it in iterables:
		return it
#save board
check_ = chains(sys.argv[2:])
#remove quote
new_chek= check_[0].split(',')
#create new list to store board as integer 
Board = []
for i in new_chek:
	Board.append(int(i))

############################################# Direction
def move_up(initial_state):	
	before_play = initial_state[:]	
	track_zero_id = initial_state.index(0)	
	keep_zero_value = initial_state[track_zero_id]
	
	#Check if Up is zero before swap
	if(keep_zero_value == 0):
		if track_zero_id not in [0,1,2]:
			temp1 = before_play[track_zero_id]
			before_play[track_zero_id] = before_play[track_zero_id - 3]
			before_play[track_zero_id - 3] = temp1

			initial_state.clear()	
			initial_state.extend(before_play)
			
		else:
			return None

	else:
		return None
	
	return initial_state
		
def move_down(initial_state):
	before_play = initial_state[:]	
	track_zero_id = initial_state.index(0)	
	keep_zero_value = initial_state[track_zero_id]
	
	#Check if Up is zero before swap
	if(keep_zero_value == 0):
		if track_zero_id not in [6,7,8]:
			temp1 = before_play[track_zero_id]
			before_play[track_zero_id] = before_play[track_zero_id + 3]
			before_play[track_zero_id + 3] = temp1

			initial_state.clear()
			initial_state.extend(before_play)
			
		else:
			return None

	else:
		return None
	
	return initial_state

def move_left(initial_state):
	before_play = initial_state[:]	
	track_zero_id = initial_state.index(0)	
	keep_zero_value = initial_state[track_zero_id]
	
	#Check if Up is zero before swap
	if(keep_zero_value == 0):
		if track_zero_id not in [0,3,6]:
			temp1 = before_play[track_zero_id]
			before_play[track_zero_id] = before_play[track_zero_id - 1]
			before_play[track_zero_id - 1] = temp1

			initial_state.clear()	
			initial_state.extend(before_play)

		else:
			return None

	else:
		return None

	return initial_state

def move_right(initial_state):
	before_play = initial_state[:]	
	track_zero_id = initial_state.index(0)	
	keep_zero_value = initial_state[track_zero_id]
	
	#Check if Up is zero before swap
	if(keep_zero_value == 0):
		if track_zero_id not in [2,5,8]:
			temp1 = before_play[track_zero_id]
			before_play[track_zero_id] = before_play[track_zero_id +1]
			before_play[track_zero_id + 1] = temp1

			initial_state.clear()	
			initial_state.extend(before_play)

		else:
			return None

	else:
		return None

	return initial_state

def graph(successor_node):
	#DRAW GRAPH ON SUCCESSOR NODE
	pos_U = successor_node[:]
	pos_D = successor_node[:]
	pos_L = successor_node[:]
	pos_R = successor_node[:]	
	#counter = 0
	possible_Moves = []
	
	while len(successor_node) > 0:

		hold_state_UP= move_up(pos_U)
		hold_state_DOWN = move_down(pos_D)				
		hold_state_LEFT= move_left(pos_L)
		hold_state_RIGHT = move_right(pos_R)
		possible_Moves = [hold_state_UP, hold_state_DOWN, hold_state_LEFT, hold_state_RIGHT]

		#create key add possible Moves
		neighbors[tuple(successor_node)] = possible_Moves
		return neighbors		
		
		
#convert list to generator
def check_list(incoming_list):
    single__ = tuple(c for c in incoming_list)
    yield single__
	

#helps if solution found
def goalTested(state_):

    return state_

def Manhattan_distance_(prev_state, curr_state):
    cost = 0
    row = 0
    col = 0

    for x in prev_state:
        pos_diff = abs(curr_state.index(x) - prev_state.index(x))

        if x != 0:
            row =  pos_diff % 3
            col =  pos_diff / 3
            
            cost += row + int(math.floor(col))
            if abs(curr_state.index(x) % 3 - prev_state.index(x) % 3) == 2 and pos_diff % 3 == 1:
                cost += 2               
    return cost # previous state or parent and neighbour or Goal state

def construct_path(state, meta):
	#print(meta)
	global	path_to_goal
	states = tuple(state)
	local_path = []

	while meta[states][0] is not None:	#backtrack return list of path in node
			states, action = meta[states]
			path_to_goal.append(action)
	path_to_goal.reverse()

	for path in path_to_goal:	# return path in UDRL order
		local_path.append(dict_frontier[path])
	path_to_goal = local_path 
	return path_to_goal	 #return Path direction in UDRL


dict_state 	  = {}	#store state as key
dict_frontier = {}	#store as key and direction as value

def bfs(initialState, goalTest):
	frontier = deque()
	explored = set()

	##########################################
	#path finding and store in meta dictionary
	meta =defaultdict(dict)
	root = tuple(initialState)
	meta[root] = (None, None)
	##########################################
	frontier.append(initialState)
	global nodes_expanded
	global max_search_depth
	max_depth = 0
	depth = deque()
	depth.append(0)

	while not frontier == 0:
		state = frontier.popleft()
		dict_state[tuple(state)] = state
		explored.add(tuple(state))

		############## Max_depth
		dep = depth.popleft()
		##############

		#check the state against the goal
		if goalTested(state) == Goal_state:
			#print(dict_frontier)
			return construct_path(state, meta)
		
		neigbhors = graph(state)
		nodes_expanded += 1

		for neighbor in neigbhors[tuple(state)]:
			if neighbor is not None:
				if  tuple(neighbor) not in dict_frontier:
					if tuple(neighbor) not in explored:
													
						####	Path to goal
						test_dir = neigbhors[tuple(state)]						
						map_path = test_dir.index(neighbor)
						path_dir = Four_Direction[map_path]						
						###
						#################### backtrack in dictionary
						child_ = tuple(neighbor)
						neigh_ = tuple(neighbor)
						meta[child_] = (tuple(state), neigh_)					
						####################

						frontier.append(neighbor)
						dict_frontier[tuple(neighbor)] = path_dir
						################### max depth
						depth.append(dep+1)
			if dep+1 > max_depth:
				max_depth = dep +1
				max_search_depth = max_depth	
						###################
	return 'FAILURE'

def dfs(initialState, goalTest):
	stack = []	
	frontier = stack
	explored = set()
	frontier.append(initialState)
	##########################################
	#path finding and store in meta dictionary
	meta =defaultdict(dict)
	root = tuple(initialState)
	meta[root] = (None, None)
	##########################################
	max_depth = 0
	depth = deque()
	depth.append(0)
	global max_search_depth
	global nodes_expanded

	while not frontier == 0:	
		state = frontier.pop()
		dict_state[tuple(state)] = state
		explored.add(tuple(state))

		############## Max_depth
		dep = depth.pop()
		##############

		if goalTested(state) == Goal_state:
			
			return construct_path(state, meta)		

		NEIGHBORS_ = graph(state)
		nodes_expanded += 1
		count = 0
		for neighbor in list(reversed(NEIGHBORS_[tuple(state)])):

			if neighbor is not None:
				if tuple(neighbor) not in dict_frontier:
					if tuple(neighbor) not in explored:
						####	Path to goal
						test_dir = NEIGHBORS_[tuple(state)]
						map_path = test_dir.index(neighbor)
						path_dir = Four_Direction[map_path]						
						###

						#################### backtrack path
						child_ = tuple(neighbor)
						neigh_ = tuple(neighbor)
						meta[child_] = (tuple(state), neigh_)
						####################
						frontier.append(neighbor)						
						dict_frontier[tuple(neighbor)] = path_dir

						################### max depth
						depth.append(dep+1)
						count +=1						

		if count > 0: 	
			if dep+1 > max_depth:
				max_depth = dep +1
				max_search_depth = max_depth	
						###################
	return 'FAILURE'

def ast(initialState, goalTest):
	
	global max_search_depth
	global nodes_expanded
	depth = []
	max_depth = 0
	#depth.append(0)
	

	heap 	 = []
	frontier = heap
	counter = 0
	priority_Queue = []
	explored = set()


	##########################################
	#path finding and store in meta dictionary
	meta =defaultdict(dict)
	root = tuple(initialState)
	meta[root] = (None, None)
	##########################################	
	
	heapq.heappush(frontier,[0,0, initialState])	

	while not frontier == 0:
		state = heapq.heappop(frontier)

		explored.add(tuple(state[2]))

		if goalTested(state[2]) == goalTest:
			return construct_path(state[2],meta)

		NEIGHBORS_ = graph(list(state[2]))
		counter += 1
		nodes_expanded +=1

		for neighbor in NEIGHBORS_[tuple(state[2])]:
			if neighbor is not None:
				if  tuple(neighbor) not in dict_frontier:
					if tuple(neighbor) not in explored:
						
						####	Path to goal
						test_dir = NEIGHBORS_[tuple(state[2])]
						map_path = test_dir.index(neighbor)
						path_dir = Four_Direction[map_path]						
						###

						#################### backtrack in dictionary
						child_ = tuple(neighbor)
						neigh_ = tuple(neighbor)
						meta[child_] = (tuple(state[2]), neigh_)					
						####################


						heapq.heappush(frontier, [(Manhattan_distance_(state[2], neighbor)+Manhattan_distance_(neighbor, goalTest)), counter, neighbor])
						dict_frontier[tuple(neighbor)] = path_dir



				elif tuple(neighbor) in dict_frontier:	#Decrease key in frontier				
					temp_relax = Manhattan_distance_(state[2], neighbor)+Manhattan_distance_(neighbor, goalTest)
					decrease_key = [temp_relax, counter, neighbor]
					
					for neig in frontier:						
						if neig[2] == decrease_key[2]:
							if neig[0] > decrease_key[0]:
								frontier.remove(neig)
								heapq.heapify(frontier)
								heapq.heappush(heappush,decrease_key)
								dict_frontier[tuple(neighbor)] = True
		
			if state[1] + 1> max_depth:
				max_depth = state[1] + 1
				max_search_depth = max_depth
		#print(met)


	return 'FAILURE'
#Output
if type(sys.argv[1]) == str and sys.argv[1] == 'bfs':
	
	time_start = time.clock()
	bfs(Board, Goal_state)
	me = psutil.Process(os.getpid())
	mem_inf = me.memory_info().rss
	time_end = time.clock()
	
	with open("output.txt", "w") as f:

		f.write("path_to_goal: {0}".format(path_to_goal))
		f.write("\n")
		f.write("cost_of_path: {0}".format(len(path_to_goal)))
		f.write("\n")
		f.write("nodes_expanded: {0}".format(nodes_expanded))
		f.write("\n")
		f.write("search_depth: {0}".format(len(path_to_goal)))
		f.write("\n")
		f.write("max_search_depth: {0}".format(max_search_depth))
		f.write("\n")
		f.write("running_time: {0}".format(round(time_end - time_start, 8)))
		f.write("\n")
		f.write("max_ram_usage: {0}".format(mem_inf / 1024/ 1024))		
	
elif type(sys.argv[1]) == str and sys.argv[1] == 'dfs':
	time_start = time.clock()
	dfs(Board, Goal_state)
	me = psutil.Process(os.getpid())
	#mem_inf = me.memory_info()[0]
	mem_inf = me.memory_info().rss
	time_end = time.clock()
	
	with open("output.txt", "w") as f:

		f.write("path_to_goal: {0}".format(path_to_goal))
		f.write("\n")
		f.write("cost_of_path: {0}".format(len(path_to_goal)))
		f.write("\n")
		f.write("nodes_expanded: {0}".format(nodes_expanded))
		f.write("\n")
		f.write("search_depth: {0}".format(len(path_to_goal)))
		f.write("\n")
		f.write("max_search_depth: {0}".format(max_search_depth))
		f.write("\n")
		f.write("running_time:	{0}".format(round(time_end - time_start, 8)))
		f.write("\n")
		f.write("max_ram_usage: {0}".format(mem_inf / 1024/ 1024))

elif type(sys.argv[1]) == str and sys.argv[1] == 'ast':
	
	time_start = time.clock()
	ast(Board, Goal_state)
	me = psutil.Process(os.getpid())
	#mem_inf = me.memory_info()[0]
	mem_inf = me.memory_info().rss
	time_end = time.clock()
	
	with open("output.txt", "w") as f:

		f.write("path_to_goal: {0}".format(path_to_goal))
		f.write("\n")
		f.write("cost_of_path: {0}".format(len(path_to_goal)))
		f.write("\n")
		f.write("nodes_expanded: {0}".format(nodes_expanded))
		f.write("\n")
		f.write("search_depth: {0}".format(len(path_to_goal)))
		f.write("\n")
		f.write("max_search_depth: {0}".format(max_search_depth))
		f.write("\n")
		f.write("running_time:	{0}".format(round(time_end - time_start, 8)))
		f.write("\n")
		f.write("max_ram_usage: {0}".format(mem_inf / 1024/ 1024))				
else:

	print('wrong Method')