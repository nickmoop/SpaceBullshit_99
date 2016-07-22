class Crew():

	def __init__(	self,
					id_new=0,
					first_name_new='',
					second_name_new='',
					race_new='',
					position_new=[0,0],
					health_new=0,
					attack_new=0,
					speed_new=0,
					breath_gas_new='',
					pilot_new=0,
					turret_new=0,
					engine_new=0,
					shield_new=0,
					reactor_new=0,
					repair_new=0,
					inventory_head_new=0,
					inventory_suit_new=0,
					inventory_weapon_new=0,
					item_new=''
				):
		self.id=id_new
		self.first_name=first_name_new
		self.second_name=second_name_new
		self.race=race_new
		self.position=position_new
		self.health=health_new
		self.attack=attack_new
		self.speed=speed_new
		self.breath_gas=breath_gas_new
		self.pilot=pilot_new
		self.turret=turret_new
		self.engine=engine_new
		self.shield=shield_new
		self.reactor=reactor_new
		self.repair=repair_new
		self.inventory_head=inventory_head_new
		self.inventory_suit=inventory_suit_new
		self.inventory_weapon=inventory_weapon_new
		self.item=item_new
		
	def paint(self,field):
		x=self.position[0]
		y=self.position[1]
		color='green'#gradient?
		item=field.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill=color,outline='black')#coords?
		self.item=item

	def erase(self,field):
		field.delete(self.item)

	def save(self, crew_text):
		crew_text = crew_text + 'id:' + str(self.id) + '\n'
		crew_text = crew_text + 'name:' + str(self.first_name) + ',' + str(self.second_name) + '\n'
		crew_text = crew_text + 'race:' + str(self.race) + '\n'
		crew_text = crew_text + 'position:' + str(self.position[0]) + ',' + str(self.position[1]) + '\n'
		crew_text = crew_text + 'health:' + str(self.health)+ '\n'
		crew_text = crew_text + 'attack:' + str(self.attack)+ '\n'
		crew_text = crew_text + 'speed:' + str(self.speed)+ '\n'
		crew_text = crew_text + 'breath_gas:' + str(self.breath_gas)+ '\n'
		crew_text = crew_text + 'pilot:' + str(self.pilot)+ '\n'
		crew_text = crew_text + 'turret:' + str(self.turret)+ '\n'
		crew_text = crew_text + 'engine:' + str(self.engine)+ '\n'
		crew_text = crew_text + 'shield:' + str(self.shield)+ '\n'
		crew_text = crew_text + 'reactor:' + str(self.reactor)+ '\n'
		crew_text = crew_text + 'repair:' + str(self.repair)+ '\n'
		crew_text = crew_text + 'head:' + str(self.inventory_head)+ '\n'
		crew_text = crew_text + 'suit:' + str(self.inventory_suit)+ '\n'
		crew_text = crew_text + 'weapon:' + str(self.inventory_weapon)
		return(crew_text)

	def load(self,crew_text):
		self.id = int(crew_text[0])
		self.first_name = crew_text[1].replace('\n','').split(',')[0]
		self.second_name = crew_text[1].replace('\n','').split(',')[1]
		self.race = crew_text[2].replace('\n','')
		self.position = crew_text[3].replace('\n','').split(',')[:-1]
		self.health = int(crew_text[4])
		self.attack = int(crew_text[5])
		self.speed = int(crew_text[6])
		self.breath_gas = int(crew_text[7])
		self.pilot = int(crew_text[8])
		self.turret = int(crew_text[9])
		self.engine = int(crew_text[10])
		self.shield = int(crew_text[11])
		self.reactor = int(crew_text[12])
		self.repair = int(crew_text[13])
		self.inventory_head = int(crew_text[14])
		self.inventory_suit = int(crew_text[15])
		self.inventory_weapon = int(crew_text[16])

	def info(self):
		message = 'id: ' + str(self.id) + '\n' + 'First name: ' + self.first_name + '\n' + 'Second name: ' + self.second_name + '\n' + 'Race: '+ self.race + '\n' + 'Health: ' + str(self.health) + '\n' + 'Attack: ' + str(self.attack) + '\n' + 'Speed: ' + str(self.speed) + '\n' + 'Breath gas: ' + str(self.breath_gas) + '\n' + 'Pilot: ' + str(self.pilot) + '\n' + 'Turret: ' + str(self.turret) + '\n' + 'Engine: ' + str(self.engine) + '\n' + 'Shield: ' + str(self.shield) + '\n' + 'Reactor: ' + str(self.reactor) + '\n' + 'Repair: ' + str(self.repair) + '\n'
		print(message)
		return(message)

if __name__=='__main__':
	pass
