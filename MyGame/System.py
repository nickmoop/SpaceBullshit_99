class System():

	def __init__(	self,
					id_new = 0,
					name_new = '',
					position_new = [0, 0],
					planets_new = [0],
					size_new = 0,
					intensity_new = [0, 0],
					state_new = 0,
					item_new = ''
				):
		self.id = id_new
		self.name = name_new
		self.position = position_new
		self.planets = planets_new
		self.size = size_new
		self.intensity = intensity_new
		self.state = state_new
		self.item = item_new

	def setColor(self):
		if (self.intensity[1] >= 0) and (self.intensity[1] < 0.25):
			self.intensity[0] = 'red'
		elif (self.intensity[1] >= 0.25) and (self.intensity[1] < 0.50):
			self.intensity[0] = 'yellow'
		elif (self.intensity[1] >= 0.50) and (self.intensity[1] < 0.75):
			self.intensity[0] = 'blue'
		elif (self.intensity[1] >= 0.75):
			self.intensity[0] = 'white'

	def paint(self,field):
		x = (self.position[0] + 1) * 15 - 7
		y = (self.position[1] + 1) * 15 - 7
		color = self.intensity[0]
		item = field.create_oval(x - 4, y - 4, x + 4, y + 4, fill = color, outline = color)
		self.item = item

	def erase(self, field):
		field.delete(self.item)

	def save(self, system_text):		
		system_text = system_text + 'id:' + str(self.id) + '\n'
		system_text = system_text + 'name:' + str(self.name) + '\n'
		system_text = system_text + 'position:' + str(self.position[0]) + ',' + str(self.position[1]) + '\n'
		system_text = system_text + 'planets:'
		for planet_id in self.planets:
			system_text = system_text + str(planet_id) + ','
		system_text = system_text + '\n' + 'size:' + str(self.size)+ '\n'
		system_text = system_text + 'intensity:' + str(self.intensity[0]) + ',' + str(self.intensity[1]) + '\n'
		system_text = system_text + 'state:' + str(self.state)+ '\n'
		return(system_text)

	def load(self,system_text):
		self.id = int(system_text[0])
		self.name = system_text[1].replace('\n','')
		position = system_text[2].replace('\n','').split(',')
		self.position = [int(position[0]), int(position[1])]
		self.planets = system_text[3].replace('\n','').split(',')[:-1]
		self.size = int(system_text[4])
		self.intensity = system_text[5].replace('\n','').split(',')
		self.state = int(system_text[6])

	def info(self):
		planets_id = ''
		for planet in self.planets:
			planets_id = planets_id + str(planet) + ', '
		message = 'id:' + str(self.id) + '\n' + 'name:' + self.name + '\n' + 'position:' + str(self.position[0]) + ', ' + str(self.position[1]) + '\n' + 'planets:' + planets_id + '\n' + 'size:' + str(self.size) + '\n' + 'intensity:' + self.intensity[0] + ', ' + str(self.intensity[1]) + '\n' + 'state:' + str(self.state) + '\n'
		print(message)

if __name__=='__main__':
	pass
