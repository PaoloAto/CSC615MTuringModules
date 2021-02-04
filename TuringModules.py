import csv
import time

# def insert_hashtag(string, index):
# 	return string[:index] + '#' + string[index:]

#Simulates the TWA machine 
class TURING:
	def __init__(self, states):
		self.states = states

	def simulateMachine(self):
		# Starts at module 1
		self.currPosition = 1
		self.currState = 1
		self.hashtagMarker = 0
		self.actual = 0
		self.moveCounter = 0
		self.valid = True

		# Initializing the tape with #
		tape = ['#']*100
		str = ' '
		print("==========================================")
		print('Initializing Tape.......')
		print('Tape: /' + str.join(tape[:20]) + '/' ) #shows only n number of values to be printed
		print(f'Current # Marker at position: {self.hashtagMarker} ')

		#while loop runs as long as the 'Halt' state has not been reached
		while self.states[self.currState].getMove() != 'Halt' and self.valid == True:
			self.moveCounter += 1
			# time.sleep(1)
			print("==========================================")
			print(f"Module Number: {self.currState}")
			print(f"Currently at Turing Module: {self.states[self.currState].getMove()}")
			print(f"Action/Value/Transition: {self.states[self.currState].getTransition()} ")
			
			if(self.states[self.currState].getMove() == 'shR'):
				self.hashtagMarker += int(self.states[self.currState].getTransition())
				self.actual = self.actual + int(self.states[self.currState].getTransition()) + int(self.states[self.currState].getTransition())
				self.currState += 1

			elif(self.states[self.currState].getMove() == 'shL' ):
				self.hashtagMarker -= int(self.states[self.currState].getTransition())
				self.actual = self.actual - int(self.states[self.currState].getTransition()) - int(self.states[self.currState].getTransition())
				self.currState += 1

			elif(self.states[self.currState].getMove() == 'const'):
				#valid since there is still no value on the next # marker
				if(tape[self.actual+1] == '#'):
					value = ''
					value = self.states[self.currState].getTransition()
					tape.insert(self.actual+1, value)
				else:
					print("Invalid Statement (There is already a value in the next # marker) \nTerminating Program......")
					self.valid = False

				self.currState += 1

			elif(self.states[self.currState].getMove() == 'copy'):
				copy = (int(self.states[self.currState].getTransition()) * 2) - 1
				tape.insert(self.actual+1, tape[self.actual-copy])
				self.hashtagMarker += 1
				self.actual +=  2
				self.currState += 1	

			elif(self.states[self.currState].getMove() == 'move'):
				#Getting the j and k of the move module
				txt = self.states[self.currState].getTransition()
				move = txt.split("-")
				j = int(move[0])
				k = int(move[1])
				#Performing move
				for x in range(j):
					tape.pop(self.actual)
					self.actual =  self.actual - 1
					tape.pop(self.actual)
					self.hashtagMarker = self.hashtagMarker - 1
					self.actual =  self.actual - 1
					tape.append('#')
					tape.append('#')

				self.currState += 1	

			elif(self.states[self.currState].getMove() == 'swap'):
				temp = ''
				temp = tape[self.actual+1]
				tape[self.actual+1] = tape[self.actual+3]
				tape[self.actual+3] = temp
				self.currState += 1	

			elif(self.states[self.currState].getMove() == 'add'):
				if(tape[self.actual+1] == '#'):
					n1 = 0
				else:
					n1 = len(tape[self.actual+1])

				if(tape[self.actual+3] == '#'):
					n2 = 0
				else:
					n2 = len(tape[self.actual+3])

				tape[self.actual+3] = '#'
				addition = 0
				addition = n1 + n2
				if(addition > 0):
					answer = ''
					for x in range(addition):
						answer += '1'
					tape[self.actual+1] = answer
				else:
					print("No numbers were added the stape is still unchanged")
					tape[self.actual+1] = '#'

				self.currState += 1

			elif(self.states[self.currState].getMove() == 'monus'):
				if(tape[self.actual+1] == '#'):
					n1 = 0
				else:
					n1 = len(tape[self.actual+1])

				if(tape[self.actual+3] == '#'):
					n2 = 0
				else:
					n2 = len(tape[self.actual+3])

				tape[self.actual+3] = '#'
				subtract = 0
				subtract = n1 - n2
				if (subtract > 0):
					answer = ''
					for x in range(subtract):
  						answer += '1'
					tape[self.actual+1] = answer
				else:
					tape[self.actual+1] = '#'

				self.currState += 1

			elif(self.states[self.currState].getMove() == 'mult'):
				if(tape[self.actual+1] == '#'):
					n1 = 0
				else:
					n1 = len(tape[self.actual+1])

				if(tape[self.actual+3] == '#'):
					n2 = 0
				else:
					n2 = len(tape[self.actual+3])

				tape[self.actual+3] = '#'
				mult = 0
				mult = n1 * n2
				if(mult > 0):
					answer = ''
					for x in range(mult):
						answer += '1'
					tape[self.actual+1] = answer
				else:
					tape[self.actual+1] = '#'

				self.currState += 1

			elif(self.states[self.currState].getMove() == 'divide'):
				if(tape[self.actual+1] == '#'):
					n1 = 0
				else:
					n1 = len(tape[self.actual+1])

				if(tape[self.actual+3] == '#'):
					n2 = 0
				else:
					n2 = len(tape[self.actual+3])

				div = 0
				div = n1 // n2
				#check if n1 is equal to zero/represented only by a #
				if(n1 == 0):
					tape[self.actual+1] = '#'

				#check if n2 is equal to zero/represented only by a #
				if(n2 == 0):
					if(n1 == 0):
						tape[self.actual+1] = '#'	
					else:
						print("Invalid Statement (Undefined answer [dividing by 0]) \nTerminating Program......")
						self.valid = False		

				#Check answer if n1 or n2 is not equal to zero/a hashtag
				if (n1 > n2):
					answer = ''
					for x in range(div):
  						answer += '1'
					tape[self.actual+1] = answer
				else:
					tape[self.actual+1] = '#'				

				self.currState += 1

			elif(self.states[self.currState].getMove() == 'ifEQ'):
				n1 = len(tape[self.actual+1])
				n2 = len(tape[self.actual+3])
				tape[self.actual+1] = '#'
				tape[self.actual+3] = '#'
				if(n1 == n2):
					self.currState = int(self.states[self.currState].getTransition())
				else:
					self.currState += 1

			elif(self.states[self.currState].getMove() == 'ifGT'):
				n1 = len(tape[self.actual+1])
				n2 = len(tape[self.actual+3])
				tape[self.actual+1] = '#'
				tape[self.actual+3] = '#'
				if(n1 > n2):
					self.currState = int(self.states[self.currState].getTransition())
				else:
					self.currState += 1		

			elif(self.states[self.currState].getMove() == 'ifLT'):
				n1 = len(tape[self.actual+1])
				n2 = len(tape[self.actual+3])
				tape[self.actual+1] = '#'
				tape[self.actual+3] = '#'
				if(n1 < n2):
					self.currState = int(self.states[self.currState].getTransition())
				else:
					self.currState += 1

			elif(self.states[self.currState].getMove() == 'goto'):
				self.currState = int(self.states[self.currState].getTransition())

			else:
				print("Invalid Statement \nTerminating Program......")
				self.valid = False
	
			print('Tape: /' + str.join(tape[:20]) + '/' ) 
			print(f'Current # Marker at position: {self.hashtagMarker} ')
			#Testing stuff remove later 
			print(f'<<<Actual # Marker at position (For testing the tape only): {self.actual}>>>')
			print(f'<<<Number of moves taken (For testing the tape only): {self.moveCounter}>>>')
		
		


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
test3 = "Exam-T(3).csv"
#(64,40,26) total steps taken

#Open CSV Files
with open(test2) as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	state_count = 0
	states = {}
	print ("======= Turing Modules SIMULATION ======")
	print(f"Loading Turing Modules File: {test2}")

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


