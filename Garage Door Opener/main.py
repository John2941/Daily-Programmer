"""
@Project Name - main.py
@author - Johnathan
@date - 4/3/2016
@time - 11:00 AM


"""

hard_coded_actions = ['button_clicked',
						'cycle_complete',
						'button_clicked',
						'button_clicked',
						'button_clicked',
						'button_clicked',
						'button_clicked',
						'cycle_complete']
hard_coded_actions2 = ['button_clicked',
						'cycle_complete',
						'button_clicked',
						'block_detected',
						'button_clicked',
						'cycle_complete',
						'button_clicked',
						'block_cleared',
						'button_clicked',
						'cycle_complete']
hard_coded_actions3 = ['button_clicked',
						'cycle_complete',
						'button_clicked',
						'block_detected',
						'button_clicked',
						'cycle_complete',
						'button_clicked',
						'block_cleared',
						'button_clicked',
					    'block_detected',
					    'button_clicked',
					    'block_cleared',
						'button_clicked',
					   	'button_clicked',
					    'button_clicked',
					    'button_clicked',
						'cycle_complete']
class GarageDoor():
	def __init__(self, action=None):
		self.door_state = None
		self.door_action = action
		self.process_actions(self.door_action)

	def process_actions(self, action):
		self.door_action = action
		if not self.door_action:
			self.door_state = 'CLOSED'
		if self.door_action == 'block_detected':
			print '> Block detected!'
			if self.door_state == 'CLOSING':
				self.door_state = 'EMERGENCY_OPENING'
		elif self.door_action == 'block_cleared':
			print '> Block cleared'
			if self.door_state == 'OPEN_BLOCKED':
				self.door_state = 'OPEN'
			elif self.door_state == 'EMERGENCY_OPENING':
				self.door_state = 'OPENING'
		elif self.door_action == "button_clicked":
			print '> Button clicked'
			if self.door_state[-3:] == 'ING':
				# Stop the door from fully opening or closing
				if self.door_state == 'EMERGENCY_OPENING':
					self.door_state = 'EMERGENCY_OPENING' # Rather explicitly state this
				elif self.door_state == 'OPEN_BLOCKED':
					self.door_state = 'OPEN_BLOCKED'
				elif self.door_state == 'CLOSING':
					self.door_state = 'STOPPED_WHILE_CLOSING'
				elif self.door_state == 'OPENING':
					self.door_state = 'STOPPED_WHILE_OPENING'
				elif self.door_state == 'STOPPED_WHILE_CLOSING':
					self.door_state = 'OPENING'
				elif self.door_state == 'STOPPED_WHILE_OPENING':
					self.door_state = 'CLOSING'
			if self.door_state == 'OPEN' or self.door_state == 'CLOSED':
				if self.door_state == 'OPEN':
					self.door_state = 'CLOSING'
				elif self.door_state == 'CLOSED':
					self.door_state = 'OPENING'
		elif self.door_action == 'cycle_complete':
			print '> Cycle complete'
			if self.door_state == 'EMERGENCY_OPENING':
				self.door_state = 'OPEN_BLOCKED'
			elif self.door_state == 'CLOSING':
				self.door_state = 'CLOSED'
			elif self.door_state == 'OPENING':
				self.door_state = 'OPEN'
		print "Door: %s" % self.door_state


def main():
	door = GarageDoor()
	for x in hard_coded_actions3:
		door.process_actions(x)



if __name__ == '__main__':
	main()