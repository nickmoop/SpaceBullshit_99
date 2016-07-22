import random
import math

class Planet():

	def __init__(	self,
					id_new=0,
					name_new='',
					orbit_new=0,
					position_new=[],
					size_new=0,
					gravity_new=0,
					radiation_new=0,
					atmosphere_new='',#carbon,oxygen,xenon
					usability_new='',
					buildings_new=[0],
					resourse_new=[0],
					item_new=[0]
				):
		self.id=id_new
		self.name=name_new
		self.orbit=orbit_new
		self.position=position_new
		self.size=size_new
		self.gravity=gravity_new
		self.radiation=radiation_new
		self.atmosphere=atmosphere_new
		self.usability=usability_new
		self.buildings=buildings_new
		self.resourse=resourse_new
		self.item=item_new

	def setGravity(self):
		if self.size=='small':
			self.gravity=(random.random()+0.5)*0.5
		elif self.size=='medium':
			self.gravity=(random.random()+0.5)
		elif self.size=='giant':
			self.gravity=(random.random()+0.5)*2.0

	def setRadiation(self,system_intensity):
		if system_intensity=='red':
			self.radiation=random.random()*0.1
		elif system_intensity=='yellow':
			self.radiation=random.random()*0.3
		elif system_intensity=='blue':
			self.radiation=random.random()*0.5
		elif system_intensity=='white':
			self.radiation=random.random()*0.8

	def setUsability(self):
		if self.orbit<3:
			self.usability=random.choice(['suitable','asteroid'])
		elif self.orbit==3:
			self.usability='suitable'
		elif self.orbit>3:
			self.usability=random.choice(['suitable','gas giant'])

	def setAtmosphere(self):
		self.atmosphere=random.choice(['carbon','oxygen','xenon'])

	def paint(self,field,time):
		item=[]
		size=0
		color=''
		i=self.orbit+1
		if self.size=='small':
			size=5
		elif self.size=='medium':
			size=7
		elif self.size=='giant':
			size=9
		if self.usability=='suitable':
			if self.atmosphere=='carbon':
				color='grey'
			elif self.atmosphere=='oxygen':
				color='deep sky blue'
			elif self.atmosphere=='xenon':
				color='purple'
		if self.usability=='gas giant':
			color='orange red'
			size=11
		if self.usability=='asteroid':
			color='green'
			size=5
		if self.usability!='asteroid':
			orbit=field.create_arc(420-i*50,390-i*10,440+i*70,410+i*10,  outline='white',style='arc',extent=359,dash=3)
			item.append(orbit)
			fx=(10+i*60)*math.cos(math.radians(time+i*15-1))+i*10+430
			fy=(10+i*10)*math.sin(math.radians(time+i*15-1))+400
			planet=field.create_oval(fx-size,fy-size,fx+size,fy+size, fill=color)
			item.append(planet)
			self.position.append([fx,fy])
		else:
			for j in range(0,360,int(10/i)):
				fx=(10+i*60)*math.cos(math.radians(j))+i*10+430
				fy=(10+i*10)*math.sin(math.radians(j))+400
				self.position.append([fx,fy])
				color=random.choice(['tan','sienna','brown','snow','coral'])
				planet=field.create_line(fx+2,fy+2,fx+2,fy+3,fill=color)
				item.append(planet)
				color=random.choice(['tan','sienna','red','snow','coral'])
				planet=field.create_line(fx-2,fy-2,fx-2,fy-3,fill=color)
				item.append(planet)
				color=random.choice(['tan','sienna','peru','snow','coral'])
				planet=field.create_line(fx+2,fy-2,fx+2,fy-3,fill=color)
				item.append(planet)
				color=random.choice(['tan','sienna','yellow','snow','coral'])
				planet=field.create_line(fx-2,fy+2,fx-2,fy+3,fill=color)
				item.append(planet)
				color=random.choice(['tan','sienna','magenta','snow','coral'])
				planet=field.create_line(fx,fy,fx-1,fy,fill=color)
				item.append(planet)
		self.item=item

	def erase(self,field):
		item=self.item
		for value in item:
			field.delete(value)
		self.item=[0]

	def save(self, planet_text):
		planet_text = planet_text + 'id:' + str(self.id) + '\n'
		planet_text = planet_text + 'name:' + str(self.name) + '\n'
		planet_text = planet_text + 'orbit:' + str(self.orbit) + '\n'
		planet_text = planet_text + 'position:' + str(self.position)+ '\n'#?
		planet_text = planet_text + 'size:' + str(self.size)+ '\n'
		planet_text = planet_text + 'gravity:' + str(self.gravity) + '\n'
		planet_text = planet_text + 'radiation:' + str(self.radiation)+ '\n'
		planet_text = planet_text + 'atmosphere:' + str(self.atmosphere) + '\n'
		planet_text = planet_text + 'usability:' + str(self.usability)+ '\n'
		planet_text = planet_text + 'buildings:'#?
		for building_id in self.buildings:
			planet_text = planet_text + str(building_id)+ ','
		planet_text = planet_text + '\n' + 'resourse:'#?
		for resourse_id in self.resourse:
			planet_text = planet_text + str(resourse_id)+ ','
		planet_text = planet_text + '\n'
		return(planet_text)

	def load(self,planet_text):
		self.id = int(planet_text[0])
		self.name = planet_text[1].replace('\n','')
		self.orbit = int(planet_text[2])
		self.position = planet_text[3].replace('\n','').split(',')
		self.size = planet_text[4].replace('\n','')
		self.gravity = float(planet_text[5])
		self.radiation = float(planet_text[6])
		self.atmosphere = planet_text[7].replace('\n','')
		self.usability = planet_text[8].replace('\n','')
		self.buildings = planet_text[9].replace('\n','').split(',')[:-1]
		self.resourse = planet_text[10].replace('\n','').split(',')[:-1]

	def info(self):
		buildings_id = ''
		for building in self.buildings:
			buildings_id = buildings_id + str(building) + ', '
		resourses_id = ''
		for resourse in self.resourse:
			resourses_id = resourses_id + str(resourse) + ', '

		message = 'id:' + str(self.id) + '\n' + 'name:' + self.name + '\n' + 'orbit:' + str(self.orbit) + '\n' + 'position:' + str(self.position[0]) + '\n' + 'size:' + str(self.size) + '\n' + 'gravity:' + str(self.gravity) + '\n' + 'radiation:' + str(self.radiation) + '\n' + 'atmosphere:' + self.atmosphere + '\n' + 'usability:' + self.usability + '\n' + 'buildings:' + buildings_id + '\n' + 'resourses:' + resourses_id + '\n'
		print(message)

if __name__=='__main__':
	pass
