import random
import time
import math
import glob
import os
import linecache
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as tkFileDialog

import gui
from System import System
from Crew import Crew
from Planet import Planet
from Ship import Ship
from Part import Part

game_folder = os.getcwd()

picked_part = ''
picked_crew = ''
picked_fleet = []
picked_ships = []
deconstruct = False

main_content = []
galaxy_size = ['Tiny', 0]
galaxy_time = 0
players_count = 1
part_list = []
system_list = []
planet_list = []
crew_list = []
ship_list = []
tmp_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
########################		FUNCTIONS
def saveAll(save_name):
	global system_list
	global planet_list
	global ship_list
	global crew_list
	global game_folder

	system_text = ''
	planet_text = ''
	ship_text = ''
	crew_text = ''

	for system in system_list:
		system_text = system.save(system_text)
	for planet in planet_list:
		planet_text = planet.save(planet_text)
	for ship in ship_list:
		ship_text = ship.save(ship_text)
	for crew in crew_list:
		crew_text = crew.save(crew_text)

	path_to_save = game_folder + '/' + 'Save' + '/' + str(save_name)
	if not os.path.exists(path_to_save):
		os.makedirs(path_to_save)

	file_to_write = open(path_to_save + '/' + 'system', 'w')
	file_to_write.write(system_text)
	file_to_write.close()

	file_to_write = open(path_to_save + '/' + 'planet', 'w')
	file_to_write.write(planet_text)
	file_to_write.close()

	file_to_write = open(path_to_save + '/' + 'ship', 'w')
	file_to_write.write(ship_text)
	file_to_write.close()

	file_to_write = open(path_to_save + '/' + 'crew', 'w')
	file_to_write.write(crew_text)
	file_to_write.close()

	gui.paintWindowMenu()

def loadAll(load_name):
	global system_list
	global planet_list
	global ship_list
	global crew_list
	global game_folder

	makePartsList()
	path_to_load = game_folder + '/' + 'Save' + '/' + str(load_name)

	file_to_read = open(path_to_load + '/' + 'system', 'r')
	tmp = []
	for line in file_to_read:
		tmp.append(line.split(':')[1])
		if line.split(':')[0] == 'state':
			system = System()
			system.load(tmp)
			system_list.append(system)
			tmp = []
	file_to_read.close()

	file_to_read = open(path_to_load + '/' + 'planet', 'r')
	tmp = []
	for line in file_to_read:
		tmp.append(line.split(':')[1])
		if line.split(':')[0] == 'resourse':
			planet = Planet()
			planet.load(tmp)
			planet_list.append(planet)
			tmp = []
	file_to_read.close()

	file_to_read = open(path_to_load + '/' + 'ship', 'r')
	tmp = []
	for line in file_to_read:
		tmp.append(line.split(':')[1])
		if line.split(':')[0] == 'spot':
			ship = Ship()
			ship.load(tmp)
			ship_list.append(ship)
			tmp = []
	file_to_read.close()

	file_to_read = open(path_to_load + '/' + 'crew', 'r')
	tmp = []
	for line in file_to_read:
		tmp.append(line.split(':')[1])
		if line.split(':')[0] == 'weapon':
			crew = Crew()
			crew.load(tmp)
			crew_list.append(crew)
			tmp = []
	file_to_read.close()

	gui.paintWindowGalaxy()

def makePartsList():
	global part_list
	global game_folder

	part_list = []
	part_groups = ['console', 'door', 'engine', 'floor', 'reactor', 'shield', 'turret', 'wall']
	for group in part_groups:
		file_to_read = open(game_folder + '/Ship' + '/Part' + '/' + group, 'r')
		for line in file_to_read:
			if 'id' in line:
				part = Part()
				part.group = group
				part.id = int(line.split()[1])
				part_list.append(part)
			if 'name' in line:
				part_list[-1].name = line.split()[1]
			elif 'condition' in line:
				part_list[-1].condition = int(line.split()[1])
			elif 'skill_type' in line:
				part_list[-1].skill_type = line.split()[1]
			elif 'skill_upgrade' in line:
				part_list[-1].skill_upgrade = int(line.split()[1])
			elif 'energy_consumption' in line:
				part_list[-1].energy_consumption = int(line.split()[1])
			elif 'speed_galaxy' in line:
				part_list[-1].speed_galaxy = int(line.split()[1])
			elif 'speed_battle' in line:
				part_list[-1].speed_battle = int(line.split()[1])
			elif 'maneuverability' in line:
				part_list[-1].maneuverability = int(line.split()[1])
			elif 'protection' in line:
				part_list[-1].protection = int(line.split()[1])
			elif 'recovery' in line:
				part_list[-1].recovery = line.split()[1]
			elif 'damage_form' in line:
				part_list[-1].damage_form = line.split()[1]
			elif 'damage' in line:
				part_list[-1].damage = int(line.split()[1])
			elif 'distance' in line:
				part_list[-1].distance = int(line.split()[1])
		file_to_read.close()

def newTravel():
	makePartsList()
	gui.paintWindowGenerateGalaxy()

def calculateStat(ship,field_info):
	global part_list
	global crew_list
	energy = 0
	protection = 0
	speed_galaxy = 0
	speed_battle = 0
	maneuverability = 0
	missile_count = 0
	beam_count = 0
	energy_count = 0
	free_spot = ship.size
	current_ship_crew = []
	for crew in crew_list:
		if crew.id in ship.crew:
			current_ship_crew.append(crew)
	for spot in ship.spot:
		if spot[4] == 'reactor':
			for part in part_list:
				if part.group == 'reactor' and part.id == spot[5]:
					energy = energy - part.energy_consumption
					free_spot = free_spot - 1
					break
		elif spot[4] == 'engine':
			for part in part_list:
				if part.group == 'engine' and part.id == spot[5]:
					energy = energy - part.energy_consumption
					speed_galaxy = speed_galaxy + part.speed_galaxy
					speed_battle = speed_battle + part.speed_battle
					maneuverability = maneuverability + part.maneuverability
					break
		elif spot[4] == 'shield':
			for part in part_list:
				if part.group == 'shield' and part.id == spot[5]:
					energy = energy - part.energy_consumption
					protection = protection + part.protection
					free_spot = free_spot - 1
					break
		elif spot[4] == 'turret':
			for part in part_list:
				if part.group == 'turret' and part.id == spot[5]:
					energy = energy - part.energy_consumption
					if part.damage_form == 'missile':
						missile_count = missile_count + 1
					if part.damage_form == 'beam':
						beam_count = beam_count + 1
					if part.damage_form == 'energy':
						energy_count = energy_count + 1
					break
		elif spot[4] == 'floor':
			free_spot = free_spot - 1
		elif spot[4] == 'console':
			free_spot = free_spot - 1
			for crew in current_ship_crew:
				if crew.position == [spot[0], spot[1]]:
					for part in part_list:
						if part.group == 'console' and part.id == spot[5]:
							#######	MAKE ME!!!!
							energy = energy - part.energy_consumption
							skill_type = part.skill_type
							skill_upgrade = part.skill_upgrade
							#######
							break
	info = 'energy:' + str(energy) + '\n' + 'speed_galaxy:' + str(speed_galaxy) + '\n' + 'speed_battle:' + str(speed_battle) + '\n' + 'maneuverability:' + str(maneuverability) + '\n' + 'protection:' + str(protection) + '\n' + 'missile:' + str(missile_count) + '\n' + 'beam:' + str(beam_count) + '\n' + 'energy:' + str(energy_count) + '\n' + 'free_space:' + str(calculateFreeSpace(ship))
	if field_info != 'return':
		field_info.itemconfig(1, text = info)
	else:
		return(energy)

def calculateFreeSpace(ship):
	free_space = ship.size
	for spot in ship.spot:
		if spot[4] == 'reactor':
			free_space = free_space - 1
		elif spot[4] == 'shield':
			free_space = free_space - 1
		elif spot[4] == 'floor':
			free_space = free_space - 1
		elif spot[4] == 'console':
			free_space = free_space - 1
	return(free_space)

def generateGalaxy():
	global galaxy_size
	global players_count
	global main_window
	global system_list
	global main_content
	global planet_list

	star_count = (galaxy_size[1] + 1) * 10
	empty_spot_list = []
	spot_size = 15
	field_size = star_count * spot_size

	field_galaxy = gui.main_content[0]
	field_galaxy.place(x = 220, y = 20, width = field_size, height = field_size)

	for i in range(0, star_count):
		for j in range(0, star_count):
			item = field_galaxy.create_rectangle(i * spot_size, j * spot_size, i * spot_size + spot_size, j * spot_size + spot_size, fill = 'black')
			empty_spot_list.append([i, j, item])
	if len(system_list) > 0:
		for system in system_list:
			system.erase(field_galaxy)
		system_list = []
		planet_list = []
	generateSystems(star_count)
	for system in system_list:
		system.paint(field_galaxy)
			
def generateSystems(star_count):
	global system_list
	position_list = []
	for i in range(0, star_count):
		system = System()
		system.id = i * 10 + 100
		system.name = 'SYSTEM NAME ' + str(i)
		while True:
			x = random.randint(0, star_count - 1)
			y = random.randint(0, star_count - 1)
			flag = False
			if [x, y] not in position_list:
				system.position = [x, y]
				position_list.append([x, y])
				break
		system.intensity = [0, random.random()]
		system.setColor()
		system.size = random.randint(1, 5)
		system.planets = []
		for j in range(0, system.size):
			system.planets.append(system.id + j)
			generatePlanet(system.intensity[0], system.id, j)
		system_list.append(system)

def generatePlanet(system_intensity, system_id, i):
	global planet_list
	planet = Planet()
	planet.id = system_id + i
	planet.name = 'PLANET NAME ' + str(system_id + i)
	planet.orbit = i
	planet.position = []
	planet.size = random.choice(['small', 'medium', 'giant'])
	planet.setGravity()
	planet.setRadiation(system_intensity)
	planet.setAtmosphere()
	planet.setUsability()
	planet_list.append(planet)

def generateShip(race,model):
	global ship_list
	global system_list
	ship = Ship()
	ship.id = len(ship_list) + 100
	ship.name = 'SHIP NAME ' + str(ship.id)
	ship.race = race
	ship.model = model
	ship.size = 10
	start_system = random.choice(system_list)
	ship.position_on_galaxy = start_system.position
	ship.coures_on_galaxy = ship.position_on_galaxy
	for i in range(0, 40):
		for j in range(0, 40):
			ship.spot.append([i, j, 0, 0, 0, 0, 0])
	ship_list.append(ship)

def generateCrew(first_name, second_name, race):
	global crew_list
	crew = Crew()
	crew.id = len(crew_list)
	crew.first_name = first_name
	crew.second_name = second_name
	crew.race = race
	crew.health = 100
	crew.attack = 0
	crew.speed = 0
	crew.breath_gas = 0
	crew.inventory_head = 0
	crew.inventory_suit = 0
	crew.inventory_weapon = 0
	crew_list.append(crew)

def showCrew(part_group, field):#WTF???
	global picked_part
	global deconstruct
	global part_list
	deconstruct = False
	picked_part = ''
	field.coords(1, (0, 0))
	field.itemconfig(1, text = '')
	names_to_show = ''
	for part in part_list:
		if part.group == part_group:
			names_to_show = names_to_show+part.name + '\n'
			picked_part = part
	field.itemconfig(1, text = names_to_show)
########################################	TMP
### 			MAKE ME!!!
def releaseGas(ship):
	for spot in ship.spot:
		if (spot[5] != 0) and (spot[2] == 0):
			spot[3] = spot[3] * 0.9
### 			MAKE ME!!!
########################################	TMP
########################		START
if __name__ == '__main__':
	gui.paintWindowMenu()
	gui.main_window.mainloop()
