class Ship():

	def __init__(	self,
					id_new = 0,
					name_new = '',
					race_new = '',
					model_new = '',
					size_new = 0,
					crew_new = [],
					position_on_galaxy_new = [0, 0],
					position_on_battle_new = [0, 0],
					course_on_galaxy_new = [0, 0],
					course_on_battle_new = [0, 0],
					spot_new = [[0, 0, 0, 0, 0, 0, 0]],
					item_new = ''
				):
		self.id = id_new
		self.name = name_new
		self.race = race_new
		self.model = model_new
		self.size = size_new
		self.crew = crew_new
		self.position_on_galaxy = position_on_galaxy_new
		self.position_on_battle = position_on_battle_new
		self.course_on_galaxy = course_on_galaxy_new
		self.course_on_battle = course_on_battle_new
		self.spot = spot_new
		self.item = item_new

	def eraseOnGalaxyMap(self, field):
		field.delete(self.item)

	def paintOnGalaxyMap(self, field):
		x = (self.position_on_galaxy[0] + 1) * 15 - 3
		y = (self.position_on_galaxy[1] + 1) * 15 - 12
		color = 'green'
		item = field.create_oval(x - 2, y - 2, x + 2, y + 2, fill = color, outline = color)
		self.item = item

	def eraseSpot(self, coords, field):
		x = coords[0]
		y = coords[1]
		for value in self.spot:
			if value[0] == x and value[1] == y:
				self.spot.remove(value)
				item = field.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill = 'black', outline = 'gray')
				self.spot.append([x, y, 0, 0, 0, 0, 0])
				break

	def paintSpot(self, coords, field, fill):
		x = coords[0]
		y = coords[1]
		text = ' '
		if fill == 'crew':
			text = 'c'
		for value in self.spot:
			if value[0] == x and value[1] == y:
				if value[4] == 'wall':
					color = 'gray27'
				elif value[4] == 'door':
					color = 'gray66'
				elif value[4] == 'reactor':
					color = 'green'
				elif value[4] == 'engine':
					color = 'blue'
				elif value[4] == 'turret':
					color = 'red'
				elif value[4] == 'shield':
					color = 'yellow'
				elif value[4] == 'console':
					color = 'brown'
				elif value[4] == 'floor':
					color = 'white'
				elif value[4] == 0:
					color = 'black'
				item = field.create_rectangle(x * 20, y * 20, x * 20 + 20, y * 20 + 20, fill = color, outline = 'gray')
				item = field.create_text(x * 20 + 9, y * 20 + 9, text = text, font = 12)
				break

	def eraseSpotMini(self, coords, field, delta):
		x = coords[0]
		y = coords[1]
		for value in self.spot:
			if value[0] == x and value[1] == y:
				self.spot.remove(value)
				item = field.create_rectangle(x * 3, y * 3, x * 3 + 3, y * 3 + 3, fill = 'black')
				self.spot.append([x, y, 0, 0, 0, 0, 0])
				break

	def correctSpots(self):
		x_min = 100
		y_min = 100
		x_max = 0
		y_max = 0
		spot_corrected_list = []
		for spot in self.spot:
			if spot[4] != 0:
				if spot[0] < x_min:
					x_min = spot[0]
				if spot[0] > x_max:
					x_max = spot[0]
				if spot[1] < y_min:
					y_min = spot[1]
				if spot[1] > y_max:
					y_max = spot[1]

		for spot in self.spot:
			if (spot[0] < x_min) or (spot[0] > x_max) or (spot[1] < y_min) or (spot[1] > y_max):
				continue
			else:
				spot_corrected_list.append(spot)

		i = 2
		while (x_max - x_min) != (y_max - y_min):
			if (x_max - x_min) > (y_max - y_min):
				if i % 2 != 0:
					y_min = y_min - 1
					for x in range(x_min, x_max + 1):
						spot_corrected_list.append([x, y_min, 0, 0, 0, 0, 0])
				else:
					y_max = y_max + 1
					for x in range(x_min, x_max + 1):
						spot_corrected_list.append([x, y_max, 0, 0, 0, 0, 0])
			else:
				if i % 2 != 0:
					x_min = x_min - 1
					for y in range(y_min, y_max + 1):
						spot_corrected_list.append([x_min, y, 0, 0, 0, 0, 0])
				else:
					x_max = x_max + 1
					for y in range(y_min, y_max + 1):
						spot_corrected_list.append([x_max, y, 0, 0, 0, 0, 0])
			i = i + 1

		self.spot = []
		for spot in spot_corrected_list:
			spot[0] = spot[0] - x_min
			spot[1] = spot[1] - y_min
			self.spot.append(spot)

	def paintShipMini(self, field, position, size = 0):
		size = size + int(120 / ((len(self.spot) - 1) ** (1.0/2.0)))
		for spot in self.spot:
			self.paintSpotMini([spot[0], spot[1]], field, position, size)

	def paintSpotMini(self, coords, field, position, size):
		x = coords[0]
		y = coords[1]
		dx = position[0]
		dy = position[1]
		for value in self.spot:
			if value[0] == x and value[1] == y:
				if value[4] == 'wall':
					color = 'gray27'
				elif value[4] == 'door':
					color = 'gray66'
				elif value[4] == 'reactor':
					color = 'green'
				elif value[4] == 'engine':
					color = 'blue'
				elif value[4] == 'turret':
					color = 'red'
				elif value[4] == 'shield':
					color = 'yellow'
				elif value[4] == 'console':
					color = 'brown'
				elif value[4] == 'floor':
					color = 'white'
				elif value[4] == 0:
					color = 'black'
				item = field.create_rectangle(x * size + 130 * dx + 10, y * size + 130 * dy + 10, x * size + 130 * dx + size + 10, y * size + 130 * dy + size + 10, fill = color)
				break

	def save(self, ship_text):
		ship_text = ship_text + 'id:' + str(self.id) + '\n'
		ship_text = ship_text + 'name:' + str(self.name) + '\n'
		ship_text = ship_text + 'race:' + str(self.race) + '\n'
		ship_text = ship_text + 'model:' + str(self.model)+ '\n'
		ship_text = ship_text + 'size:' + str(self.size)+ '\n'
		ship_text = ship_text + 'crew:'
		for crew_id in self.crew:
			ship_text = ship_text + str(crew_id) + ','
		ship_text = ship_text + '\n' + 'position:' + str(self.position_on_galaxy[0]) + ',' + str(self.position_on_galaxy[1]) + '\n'
		ship_text = ship_text + 'course:' + str(self.course_on_galaxy[0]) + ',' + str(self.course_on_galaxy[1]) + '\n'
		ship_text = ship_text + 'spot:'
		for spot_current in self.spot:
			ship_text = ship_text + str(spot_current[0]) + ';' + str(spot_current[1]) + ';' + str(spot_current[2]) + ';' + str(spot_current[3]) + ';' + str(spot_current[4]) + ';' + str(spot_current[5]) + ';' + str(spot_current[6]) + ','
		return(ship_text)

	def load(self,ship_text):
		self.id = int(ship_text[0])
		self.name = ship_text[1].replace('\n','')
		self.race = ship_text[2].replace('\n','')
		self.model = ship_text[3].replace('\n','')
		self.size = int(ship_text[4])
		self.crew = ship_text[5].replace('\n','').split(',')[:-1]
		position = ship_text[6].replace('\n','').split(',')
		self.position_on_galaxy = [int(position[0]), int(position[1])]
		course = ship_text[7].replace('\n','').split(',')
		self.course_on_galaxy = [int(course[0]), int(course[1])]
		list_of_spots = ship_text[8].replace('\n','').split(',')[:-1]
		self.spot = [[0, 0, 0, 0, 0, 0, 0]]
		for spot in list_of_spots:
			tmp = []
			for value in spot.split(';'):
				try:
					tmp.append(int(value))
				except:
					tmp.append(value)
			self.spot.append(tmp)

	def info(self):
		crew_id = ''
		for crew in self.crew:
			crew_id = crew_id + str(crew) + ', '

		spots = ''
		for spot in self.spot:
			for value in spot:
				spots = spots + str(value) + ';'
			spots = spots + ','

		message = 'id:' + str(self.id) + '\n' + 'name:' + self.name + '\n' + 'race:' + self.race + '\n' + 'model:' + self.model + '\n' + 'size:' + str(self.size) + '\n' + 'crew:' + crew_id + '\n' + 'position:' + str(self.position_on_galaxy[0]) + ', ' + str(self.position_on_galaxy[1]) + '\n' + 'course:' + str(self.course_on_galaxy[0]) + ', ' + str(self.course_on_galaxy[1]) + '\n' + spots
		print(message)

	def infoBattle(self):
		info = 'id:' + str(self.id) + '\n' + 'name:' + self.name + '\n' + 'race:' + self.race + '\n' + 'model:' + self.model + '\n' + 'size:' + str(self.size) + '\n' + 'position:' + str(self.position_on_battle[0]) + ', ' + str(self.position_on_battle[1])
		return(info)

if __name__=='__main__':
	pass
