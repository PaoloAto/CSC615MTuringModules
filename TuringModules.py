import csv
import time

# def insert_hashtag(string, index):
# 	return string[:index] + '#' + string[index:]

#Simulates the TWA machine 
class TURING:
	def __init__(self, states):
		self.states = states

	def simulateMachine(self):
		# Starts at state 1
		self.currPosition = 1
		self.currState = 1

		#while loop runs as long as the 'Halt' state has not been reached
		while self.states[self.currState].getMove() != 'Halt':
			# time.sleep(1.5)
			print("==========================================")
			print(f"Module # {self.states[self.currState].getIndex()} ")
			print(f"Currently at Turing Module: {self.states[self.currState].getMove()}")
			print(f"Action/Value/Transition: {self.states[self.currState].getTransition()} ")
			if(self.states[self.currState].getMove() == 'shR' or self.states[self.currState].getMove() == 'shL' 
			or self.states[self.currState].getMove() == 'const' or self.states[self.currState].getMove() == 'copy'
			or self.states[self.currState].getMove() == 'move' or self.states[self.currState].getMove() == 'swap'
			or self.states[self.currState].getMove() == 'add' or self.states[self.currState].getMove() == 'monus'
			or self.states[self.currState].getMove() == 'mult'):

				self.currState += 1

			else:
				self.currState = self.states[self.currState].getTransition()


#Object that holds the information of each state from the CSV File
class State:
	def __init__(self, stateNo, move, transition):
		self.stateNo = stateNo
		self.move = move
		self.transition = transition

	def getIndex(self):
		return self.stateNo

	def getMove(self):
		return self.move

	def getTransition(self):
		return self.transition

#Turing Modules CSV Files 
test1 = "GCD-6-8.csv"
test2 = "SQRT-9.csv"
test3 = "Exam-3.csv"

#Open CSV Files
with open(test1) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	state_count = 0
	states = {}
	print ("======= Turing Modules SIMULATION ======")
	print(f"Loading Turing Modules File: {test1}")

	# CSV FORMAT: row[0] = module number, row[1] = turing module, row [2] = action/value/transition
	for row in csv_reader:
		stateNo = int(row[0])
		move = row[1]
		action = row[2]
		if stateNo not in states:
			states[stateNo] = State(stateNo, move, action)

		state_count += 1

	print(f'Finished loading {state_count} number of modules for simulation.')

#<<<<<Main Program>>>>>
tm = TURING(states)
tm.simulateMachine()
