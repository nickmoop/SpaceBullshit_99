from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from System import System
from Crew import Crew
from Planet import Planet
from Ship import Ship
from Part import Part

import SpaceBullshit99
from SpaceBullshit99 import newTravel
from SpaceBullshit99 import calculateFreeSpace
from SpaceBullshit99 import calculateStat
from SpaceBullshit99 import saveAll
from SpaceBullshit99 import loadAll

from SpaceBullshit99 import generateGalaxy

main_content = []
field_fleet_mini_lines = [[0 for y in range(0,3)] for x in range(0,2)]

main_window = Tk()
main_window.resizable(False, False)
geometry_x = 1280
geometry_y = 1024
main_window.geometry(str(geometry_x) + 'x' + str(geometry_y) + '+0+0')
#################################################################
def turnFight():
	print('turn')

def paintWindowSave():
	global main_window
	global main_content

	deleteMainContent()
	main_window.title('Save')

	save_name = StringVar()
	save_name.set('save_name')
	field_save_name = Entry(main_window, textvariable = save_name)
	field_save_name.place(x = 120,y = 80, width = 100, height = 20)
	main_content.append(field_save_name)

	button_back = Button(main_window, text = 'Back to menu', command = backFromGenerateGalaxy)
	button_back.place(x = 20, y = 100, width = 100, height = 20)
	main_content.append(button_back)

	button_save = Button(main_window, text = 'save', command = lambda:saveAll(field_save_name.get()))
	button_save.place(x = 20, y = 80, width = 100, height = 20)
	main_content.append(button_save)

def paintWindowload():
	global main_window
	global main_content

	deleteMainContent()
	main_window.title('Load')

	load_name = StringVar()
	load_name.set('save_name')
	field_load_name = Entry(main_window, textvariable = load_name)
	field_load_name.place(x = 120,y = 80, width = 100, height = 20)
	main_content.append(field_load_name)

	button_back = Button(main_window, text = 'Back to menu', command = backFromGenerateGalaxy)
	button_back.place(x = 20, y = 100, width = 100, height = 20)
	main_content.append(button_back)

	button_load = Button(main_window, text = 'load', command = lambda:loadAll(field_load_name.get()))
	button_load.place(x = 20, y = 80, width = 100, height = 20)
	main_content.append(button_load)

def fieldCrewIdClick(event, arg):
	SpaceBullshit99.picked_part = ''
	i = int(event.y / 15) + 1
	current_ship_crew = arg[0]
	field_crew_info = arg[1]
	field_part_id = arg[2]
	field_part_id.coords(1, (0, 0))
	field_part_id.itemconfig(1, text = '')
	for value in current_ship_crew:
		if value[0] == i:
			crew = value[1]
			SpaceBullshit99.picked_crew = crew
			field_crew_info.coords(1, (0, 0))
			field_crew_info.itemconfig(1, text = '')
			field_crew_info.itemconfig(1, text = crew.info())
			break
		else:
			SpaceBullshit99.picked_crew = ''
			field_crew_info.coords(1, (0, 0))
			field_crew_info.itemconfig(1, text = '')
			break

def quit():
	pass

def fieldFleetMiniClick(event, arg):
	global field_fleet_mini_lines

	field_fleet_mini = arg[0]
	x = int((event.x - 10) / 130)
	y = int((event.y - 10) / 130)
	i = y * 2 + x
	if i <= (len(SpaceBullshit99.picked_fleet) - 1):
		ship = SpaceBullshit99.picked_fleet[i]
		if not (ship in SpaceBullshit99.picked_ships):
			paint4Lines([x, y], field_fleet_mini, field_fleet_mini_lines)
			SpaceBullshit99.picked_ships.append(ship)
		elif ship in SpaceBullshit99.picked_ships:
			erase4Lines([x, y], field_fleet_mini, field_fleet_mini_lines)
			SpaceBullshit99.picked_ships.remove(ship)	

def erase4Lines(coords, field, list_of_lines):
	x = coords[0]
	y = coords[1]
	field_fleet_mini = field
	field_fleet_mini_lines = list_of_lines

	for item in field_fleet_mini_lines[x][y]:
		field_fleet_mini.delete(item)
	field_fleet_mini_lines[x][y] = 0

def paint4Lines(coords, field, list_of_lines):	
	x = coords[0]
	y = coords[1]
	field_fleet_mini = field
	field_fleet_mini_lines = list_of_lines

	x1 = x * 130 + 7
	y1 = y * 130 + 8
	x2 = x * 130 + 13 + 120
	y2 = y * 130 + 8
	item_0 = field_fleet_mini.create_line(x1, y1, x2, y2, width = 3.0, fill = 'red')
	x1 = x * 130 + 12 + 120
	y1 = y * 130 + 7
	x2 = x * 130 + 12 + 120
	y2 = y * 130 + 14 + 120
	item_1 = field_fleet_mini.create_line(x1, y1, x2, y2, width = 3.0, fill = 'red')
	x1 = x * 130 + 14 + 120
	y1 = y * 130 + 12 + 120
	x2 = x * 130 + 7
	y2 = y * 130 + 12 + 120
	item_2 = field_fleet_mini.create_line(x1, y1, x2, y2, width = 3.0, fill = 'red')
	x1 = x * 130 + 8
	y1 = y * 130 + 13 + 120
	x2 = x * 130 + 8
	y2 = y * 130 + 7
	item_3 = field_fleet_mini.create_line(x1, y1, x2, y2, width = 3.0, fill = 'red')
	field_fleet_mini_lines[x][y] = [item_0, item_1, item_2, item_3]

def erase4LinesMiniMap(field, list_of_lines):
	for item in list_of_lines:
		field.delete(item)
	list_of_lines = [0, 0, 0, 0]

def paint4LinesMiniMap(list_of_coords, field, list_of_lines):	
	for i in range(0, 4):
		if i == 3:
			x1 = list_of_coords[i][0]
			y1 = list_of_coords[i][1]
			x2 = list_of_coords[0][0]
			y2 = list_of_coords[0][1]
		else:
			x1 = list_of_coords[i][0]
			y1 = list_of_coords[i][1]
			x2 = list_of_coords[i + 1][0]
			y2 = list_of_coords[i + 1][1]
		item = field.create_line(x1, y1, x2, y2, fill = 'red')
		list_of_lines.append(item)

def tmpButtonOkTime(field_time):
	SpaceBullshit99.galaxy_time = int(field_time.get())

def pressEscButton(event):
	paintWindowMenu()

def showTechTree():
	messagebox.showinfo('Oops', 'This tech tree.')

def turnGalaxy():
	messagebox.showinfo('Oops', 'Turn galaxy')

def applyDesignedShip(ship):
	if calculateFreeSpace(ship) < 0:
		messagebox.showinfo('Oops', 'Your ship havent so much space.')
	elif calculateFreeSpace(ship) > 0:
		messagebox.showinfo('Oops', 'Your ship have free space.')
	elif calculateFreeSpace(ship) == 0:
		if calculateStat(ship,'return') < 0:
			messagebox.showinfo('Oops', 'Your ship havent so much energy.')
		else:
			ship.correctSpots()
			paintWindowGalaxy()

def applyProfile(arg_list):
	if (len(arg_list[0]) > 1) and (len(arg_list[1]) > 1):
		SpaceBullshit99.generateCrew(arg_list[0], arg_list[1], arg_list[2])
		SpaceBullshit99.generateShip(arg_list[2], arg_list[3])
		SpaceBullshit99.ship_list[-1].crew.append(SpaceBullshit99.crew_list[-1].id)
		paintWindowDesignShip(SpaceBullshit99.ship_list[-1])
	else:
		messagebox.showinfo('Oops', 'Wrong name.')

def applyGalaxy():
	if len(SpaceBullshit99.system_list) > 1:
		paintWindowDestiny()
	else:
		messagebox.showinfo('Oops', 'Generate galaxy first.')

def fieldPartIdClick(event, arg):
	picked_part = SpaceBullshit99.picked_part
	part_list = SpaceBullshit99.part_list
	SpaceBullshit99.picked_crew = ''

	field_crew_info = arg[0]
	field_crew_info.coords(1, (0, 0))
	field_crew_info.itemconfig(1, text = '')
	i = int(event.y / 15) + 1
	for part in part_list:
		if not picked_part:
			break
		if part.group == picked_part.group:
			if part.id == i:
				SpaceBullshit99.picked_part = part
				break

def deconstructPart(arg):
	SpaceBullshit99.picked_part = ''
	SpaceBullshit99.picked_crew = ''
	SpaceBullshit99.deconstruct = True

	field_part_id = arg[0]
	field_crew_info = arg[1]
	field_part_id.coords(1)
	field_part_id.itemconfig(1, text = ' ')
	field_crew_info.coords(1)
	field_crew_info.itemconfig(1, text = ' ')

def showPart(part_group, field):
	picked_part = SpaceBullshit99.picked_part
	part_list = SpaceBullshit99.part_list

	SpaceBullshit99.deconstruct = False
	picked_part = ''
	field.coords(1, (0, 0))
	field.itemconfig(1, text = '')
	names_to_show = ''
	for part in part_list:
		if part.group == part_group:
			names_to_show = names_to_show+part.name + '\n'
			SpaceBullshit99.picked_part = part
	field.itemconfig(1, text = names_to_show)

def fieldSystemClick(event, system):
	planet_list = SpaceBullshit99.planet_list
	x = event.x
	y = event.y
	for planet in planet_list:
		if planet.id in system.planets:
			for position in planet.position:
				if (abs(position[0] - x) <= 5) and (abs(position[1] - y) <= 5):
					print(planet.name)
					break

def fieldSystemMotion(event, arg):
	planet_list = SpaceBullshit99.planet_list
	system = arg[0]
	field = arg[1]
	window = arg[2]
	x = event.x
	y = event.y
	field.coords(1, (0, 0))
	field.itemconfig(1, text = '')
	if (abs(400 - x) <= 10) and (abs(400 - y) <= 10):
		message = str(system.name) + '\n' + str(system.intensity[1]) + ' rad' + '\n' + str(system.state)
		field.coords(1, (400 + 20, 400 + 20))
		field.itemconfig(1, text = message)
	for planet in planet_list:
		for position in planet.position:
			if (abs(position[0] - x) <= 5) and (abs(position[1] - y) <= 5):
				if planet.id in system.planets:
					message = str(planet.name) + '\n' + str(planet.usability) + '\n' + str(planet.gravity) + ' G' + '\n' + str(planet.radiation) + ' rad' + '\n' + str(planet.atmosphere)
					field.coords(1, (position[0] + 20, position[1] + 20))
					field.itemconfig(1, text = message)
					break

def paintPickedFleetMini(picked_fleet, field_fleet_mini):
	x = 0
	y = 0
	if picked_fleet:
		for ship in picked_fleet:
			ship.paintShipMini(field_fleet_mini, [x, y])
#				ship.paintSpotMini([spot[0], spot[1]], field_fleet_mini, [x, y])
			if x == 0:
				x = 1
			elif x == 1:
				y = y + 1
				x = 0
	elif field_fleet_mini:
		field_fleet_mini.delete('all')
	else:
		pass

def fieldGalaxyClick(event, arg):
	x = int(event.x / 15)
	y = int(event.y / 15)
	field_fleet_mini = arg[0]
	SpaceBullshit99.picked_fleet = []

	for ship in SpaceBullshit99.ship_list:
		if ship.position_on_galaxy == [x, y]:
			SpaceBullshit99.picked_fleet.append(ship)
	have_course = False

	if SpaceBullshit99.picked_ships:
		for system in SpaceBullshit99.system_list:
			if system.position == [x, y]:
				have_course = True
				if SpaceBullshit99.picked_ships[0].position_on_galaxy == [x, y]:
					paintPickedFleetMini(0, field_fleet_mini)
					SpaceBullshit99.picked_ships = []
					paintWindowSystem(system)
					break
				messagebox.showinfo('Oops', 'Fleet travel to:\n' + str(system.name))
				for ship in SpaceBullshit99.picked_ships:
					ship.course_on_galaxy = [x, y]
				paintPickedFleetMini(0, field_fleet_mini)
				break
		if not have_course:
			paintPickedFleetMini(0, field_fleet_mini)
			messagebox.showinfo('Oops', 'Can flee to star only.')
	SpaceBullshit99.picked_ships = []
	if len(SpaceBullshit99.picked_fleet) != 0:
		paintPickedFleetMini(SpaceBullshit99.picked_fleet, field_fleet_mini)
	elif not have_course:
		paintPickedFleetMini(0, field_fleet_mini)

def fieldShipSpotsClick(event, arg):
	picked_part = SpaceBullshit99.picked_part

	field_ship_spots = arg[0]
	ship = arg[1]
	field_ship_info = arg[2]
	current_ship_crew = arg[3]
	field_crew_info = arg[4]
	x = int(event.x / 20)
	y = int(event.y / 20)

	if SpaceBullshit99.deconstruct:
		for spot in ship.spot:
			if spot[0] == x and spot[1] == y:
				SpaceBullshit99.picked_crew = ''
				for value in current_ship_crew:
					crew = value[1]
					if crew.position == [x, y]:
						crew.position = [0, 0]
				ship.eraseSpot([x, y], field_ship_spots)
				calculateStat(ship, field_ship_info)
				break

	if picked_part:
		for spot in ship.spot:
			if spot[0] == x and spot[1] == y:
				if (spot[4] == 'floor') and ((picked_part.group != 'turret') or (picked_part.group != 'engine')):
					spot[2] = 1
					spot[3] = 1
					spot[4] = picked_part.group
					spot[5] = picked_part.id
					spot[6] = 1
					ship.paintSpot([x, y], field_ship_spots, '')
				elif picked_part.group == 'floor':
					spot[2] = 1
					spot[3] = 1
					spot[4] = picked_part.group
					spot[5] = picked_part.id
					spot[6] = 1
					ship.paintSpot([x, y], field_ship_spots, '')
				elif picked_part.group == 'wall':
					spot[2] = 1
					spot[3] = 0
					spot[4] = picked_part.group
					spot[5] = picked_part.id
					spot[6] = 1
					ship.paintSpot([x, y], field_ship_spots, '')
				elif picked_part.group == 'door':
					spot[2] = 1
					spot[3] = 0
					spot[4] = picked_part.group
					spot[5] = picked_part.id
					spot[6] = 1
					ship.paintSpot([x, y], field_ship_spots, '')
				elif (picked_part.group == 'turret') and ((spot[4] == 'wall') or (spot[4] == 0)):
					spot[2] = 1
					spot[3] = 0
					spot[4] = picked_part.group
					spot[5] = picked_part.id
					spot[6] = 1
					ship.paintSpot([x, y], field_ship_spots, '')
				elif (picked_part.group == 'engine') and ((spot[4] == 'wall') or (spot[4] == 0)):
					spot[2] = 1
					spot[3] = 0
					spot[4] = picked_part.group
					spot[5] = picked_part.id
					spot[6] = 1
					ship.paintSpot([x, y], field_ship_spots, '')
				else:
					messagebox.showinfo('Oops', 'Place floor first.')
				for value in current_ship_crew:
					crew = value[1]
					if crew.position == [x, y]:
						crew.position = [0, 0]
				calculateStat(ship, field_ship_info)
				break
	elif (not SpaceBullshit99.deconstruct) and (not SpaceBullshit99.picked_crew):
		messagebox.showinfo('Oops', 'Choose part or crew first.')
	flag = True
	if SpaceBullshit99.picked_crew:
		for value in current_ship_crew:
			crew = value[1]
			if crew.position == [x, y]:
				messagebox.showinfo('Oops', 'This spot is full.')
				flag = False
				break
	else:
		flag = False
		for value in current_ship_crew:
			crew = value[1]
			if crew.position == [x, y]:
				SpaceBullshit99.picked_crew = crew
				field_crew_info.coords(1, (0, 0))
				field_crew_info.itemconfig(1, text = '')
				field_crew_info.itemconfig(1, text = crew.info())
				break
	if flag:
		for spot in ship.spot:
			if spot[0] == x and spot[1] == y:
				if spot[4] == 0:
					messagebox.showinfo('Oops', 'Cant place crew in space.')
				elif spot[4] == 'wall':
					messagebox.showinfo('Oops', 'Cant place crew in wall.')
				elif spot[4] == 'turret':
					messagebox.showinfo('Oops', 'Cant place crew in turret.')
				elif spot[4] == 'engine':
					messagebox.showinfo('Oops', 'Cant place crew in engine.')
				else:
					ship.paintSpot(SpaceBullshit99.picked_crew.position, field_ship_spots, '')
					SpaceBullshit99.picked_crew.position = [x, y]
					ship.paintSpot([x, y], field_ship_spots, 'crew')
					break

def fieldShipSpotsMotion(event, arg):
	part_list = SpaceBullshit99.part_list
	field = arg[0]
	ship = arg[1]
	x = event.x
	y = event.y
	field.coords(2, (0, 400))
	field.itemconfig(2, text = '')
	for spot in ship.spot:
		if (spot[0] == int(x / 20)) and (spot[1] == int(y / 20)) and (spot[4] != 0):
			for part in part_list:
				if (part.group == spot[4]) and (part.id == spot[5]):
					message = part.info() + 'part_durabiliry:' + str(spot[6]) + '\n' + 'hull:' + str(spot[2]) + '\n' + 'gas:' + str(spot[3]) + '\n'
					field.coords(2, (0, 400))
					field.itemconfig(2, text = message)
					break

def fieldPartIdMotion(event, field):
	part_list = SpaceBullshit99.part_list
	picked_part = SpaceBullshit99.picked_part
	message = ''
	x = event.x
	y = event.y
	i = int(y / 15) + 1
	field.coords(2, (0, 0))
	field.itemconfig(2, text = '')
	for part in part_list:
		if not picked_part:
			break
		if part.group == picked_part.group:
			if part.id == i:
				field.coords(2, (x + 20, y + 20))
				field.itemconfig(2, text = part.info())
				break

def onSelectSize(event):
	SpaceBullshit99.galaxy_size[0] = event.widget.get(ACTIVE)
	SpaceBullshit99.galaxy_size[1] = int(event.widget.curselection()[0])

def onSelectPlayersCount(event):
	SpaceBullshit99.players_count = event.widget.get(ACTIVE)

def deleteMainContent():
	global main_content

	for value in main_content:
		value.destroy()
	main_content = []

def options():
	chooseFolder()

def chooseFolder():
	SpaceBullshit99.game_folder = filedialog.askdirectory(parent = main_window, title = 'Select a game folder')

def backFromGenerateGalaxy():
	global galaxy_size
	global players_count
	galaxy_size = ['Tiny', 0]
	players_count = 1
	paintWindowMenu()

def backFromDesignShip():
	paintWindowDestiny()

def paintWindowMenu():
	global main_window
	global main_content

	deleteMainContent()
	main_window.title('Menu')

	button_new_travel = Button(main_window, text = 'New travel', command = newTravel)
	button_new_travel.place(x = 0, y = 60, width = 100, height = 20)
	main_content.append(button_new_travel)

	button_load = Button(main_window, text = 'Load', command = paintWindowload)
	button_load.place(x = 0, y = 80, width = 100, height = 20)
	main_content.append(button_load)

	button_save = Button(main_window, text = 'Save', command = paintWindowSave)
	button_save.place(x = 0, y = 100, width = 100, height = 20)
	main_content.append(button_save)

	button_options = Button(main_window, text = 'Options', command = options)
	button_options.place(x = 0, y = 120, width = 100, height = 20)
	main_content.append(button_options)

	button_quit = Button(main_window, text = 'Quit', command = quit)
	button_quit.place(x = 0, y = 140, width = 100, height = 20)
	main_content.append(button_quit)

def paintWindowGenerateGalaxy():
	global main_window
	global main_content

	deleteMainContent()
	main_window.title('Generate galaxy')

	field_galaxy = Canvas(main_window)
	field_galaxy.place(x = 0, y = 0, width = 0, height = 0)
	main_content.append(field_galaxy)

	button_back = Button(main_window, text = 'Back to menu', command = backFromGenerateGalaxy)
	button_back.place(x = 20, y = 80, width = 100, height = 20)
	main_content.append(button_back)

	button_generate = Button(main_window, text = 'Generate', command = generateGalaxy)
	button_generate.place(x = 20, y = 100, width = 100, height = 20)
	main_content.append(button_generate)

	button_apply = Button(main_window, text = 'Apply', command = applyGalaxy)
	button_apply.place(x = 20, y = 120, width = 100, height = 20)
	main_content.append(button_apply)

	label_galaxy_size = Label(main_window, text = 'Size of galaxy')
	label_galaxy_size.place(x = 20, y = 20, width = 100, height = 20)
	main_content.append(label_galaxy_size)

	label_players_count = Label(main_window, text = 'Max. Players')
	label_players_count.place(x = 20, y = 40, width = 100, height = 20)
	main_content.append(label_players_count)

	listbox_galaxy_size = Listbox(main_window)
	listbox_galaxy_size.place(x = 120, y = 20, width = 100, height = 20)
	listbox_galaxy_size.insert(1, 'Tiny')
	listbox_galaxy_size.insert(2, 'Small')
	listbox_galaxy_size.insert(3, 'Medium')
	listbox_galaxy_size.insert(4, 'Large')
	listbox_galaxy_size.insert(5, 'Huge')
	main_content.append(listbox_galaxy_size)

	listbox_players_count = Listbox(main_window)
	listbox_players_count.place(x = 120, y = 40, width = 100, height = 20)
	listbox_players_count.insert(1, '1')
	listbox_players_count.insert(2, '2')
	listbox_players_count.insert(3, '3')
	listbox_players_count.insert(4, '4')
	listbox_players_count.insert(5, '5')
	main_content.append(listbox_players_count)

	listbox_galaxy_size.bind('<<ListboxSelect>>', onSelectSize)
	listbox_players_count.bind('<<ListboxSelect>>', onSelectPlayersCount)
	field_galaxy.bind('<ButtonPress-1>', lambda event, arg = [0]:fieldGalaxyClick(event, arg))

def paintWindowDestiny():
	global main_window
	global main_content

	arg_list = []

	deleteMainContent()
	main_window.title('Choose your destiny')

	first_name = StringVar()
	first_name.set('First name')
	field_first_name = Entry(main_window, textvariable = first_name)
	field_first_name.place(x = 120,y = 20, width = 100, height = 20)
	main_content.append(field_first_name)

	second_name = StringVar()
	second_name.set('Second name')
	field_second_name = Entry(main_window, textvariable = second_name)
	field_second_name.place(x = 120, y = 40, width = 100, height = 20)
	main_content.append(field_second_name)

	label_first_name = Label(main_window, text = 'First name:')
	label_first_name.place(x = 20, y = 20, width = 100, height = 20)
	main_content.append(label_first_name)

	label_second_name = Label(main_window, text = 'Second name:')
	label_second_name.place(x = 20, y = 40, width = 100, height = 20)
	main_content.append(label_second_name)

	label_race = Label(main_window, text = 'Your race:')
	label_race.place(x = 20, y = 60, width = 100, height = 20)
	main_content.append(label_race)

	label_role = Label(main_window, text = 'Your role:')
	label_role.place(x = 20, y = 80, width = 100, height = 20)
	main_content.append(label_role)
	
	label_difficulty = Label(main_window, text = 'Difficulty:')
	label_difficulty.place(x = 20, y = 100, width = 100, height = 20)
	main_content.append(label_difficulty)

	listbox_race = Listbox(main_window)
	listbox_race.place(x = 120, y = 60, width = 100, height = 20)
	listbox_race.insert(1, 'RACE 1')
	listbox_race.insert(2, 'RACE 2')
	listbox_race.insert(3, 'RACE 3')
	listbox_race.insert(4, 'RACE 4')
	listbox_race.insert(5, 'RACE 5')
	main_content.append(listbox_race)

	listbox_role = Listbox(main_window)
	listbox_role.place(x = 120, y = 80, width = 100, height = 20)
	listbox_role.insert(1, 'Guardian')
	listbox_role.insert(2, 'Scout')
	listbox_role.insert(3, 'Trader')
	main_content.append(listbox_role)

	listbox_difficulty = Listbox(main_window)
	listbox_difficulty.place(x = 120, y = 100, width = 100, height = 20)
	listbox_difficulty.insert(1, 'Easy')
	listbox_difficulty.insert(2, 'Medium')
	listbox_difficulty.insert(3, 'Hard')
	listbox_difficulty.insert(4, 'Insane')
	main_content.append(listbox_difficulty)

	button_apply = Button(main_window, text = 'Apply', command = lambda:applyProfile([first_name.get(), second_name.get(), listbox_race.get(ACTIVE), listbox_role.get(ACTIVE), listbox_difficulty.get(ACTIVE)]))
	button_apply.place(x = 20, y = 120, width = 100, height = 20)
	main_content.append(button_apply)
	
def paintWindowSystem(system):
	planet_list = SpaceBullshit99.planet_list
	galaxy_time = SpaceBullshit99.galaxy_time

	planets = []
	system_window = Tk()
	system_window.resizable(False, False)
	geometry_x = 1000
	geometry_y = 820
	system_window.geometry(str(geometry_x) + 'x' + str(geometry_y) + '+100+100')
	system_window.title('System : ' + system.name)

	field_system = Canvas(system_window, bg = 'black')
	field_system.place(x = 10, y = 10, width = 800, height = 800)

	text_info = field_system.create_text(0, 0, anchor = 'nw', text = '', fill = 'white')

	star = field_system.create_oval(390, 390, 410, 410, fill = system.intensity[0])	
	for planet in planet_list:
		if planet.id in system.planets:
			planets.append(planet)
			planet.paint(field_system, galaxy_time)

	field_system.bind('<ButtonPress-1>', lambda event, arg = system:fieldSystemClick(event, arg))
	field_system.bind('<Motion>', lambda event, arg=[system, field_system, system_window]:fieldSystemMotion(event, arg))

	system_window.mainloop()

def paintWindowDesignShip(ship):
	global main_window
	global main_content

	crew_list = SpaceBullshit99.crew_list

	deleteMainContent()
	main_window.title('Design your ship')

	field_part_id = Canvas(main_window, bg = 'white')
	field_part_id.place(x = 10, y = 40, width = 200, height = 400)
	main_content.append(field_part_id)

	name_part_id = field_part_id.create_text(0, 0, anchor = 'nw', fill = 'black', activefill = 'lavender')

	info_part_id = field_part_id.create_text(0, 0, anchor = 'nw', fill = 'black')

	field_crew_id = Canvas(main_window, bg = 'white')
	field_crew_id.place(x = 10, y = 450, width = 200, height = 350)
	main_content.append(field_crew_id)

	name_crew = field_crew_id.create_text(0, 0, anchor = 'nw', fill = 'black')

	field_ship_spots = Canvas(main_window, bg = 'black')
	field_ship_spots.place(x = 220, y = 40, width = 800, height = 800)
	main_content.append(field_ship_spots)

	field_ship_info = Canvas(main_window, bg = 'white')
	field_ship_info.place(x = 1030, y = 40, width = 240, height = 400)
	main_content.append(field_ship_info)

	info_ship = field_ship_info.create_text(0, 0, anchor = 'nw', fill = 'black')

	info_ship_spot = field_ship_info.create_text(0, 200, anchor = 'nw', fill = 'black')

	field_crew_info = Canvas(main_window, bg = 'white')
	field_crew_info.place(x = 1030, y = 450, width = 240, height = 400)
	main_content.append(field_crew_info)

	info_crew = field_crew_info.create_text(0, 0, anchor = 'nw', fill = 'black')

	for i in range(0, 40):
		for j in range(0, 40):
			item = field_ship_spots.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill = 'black', outline = 'gray')

	for i in range(0, 40):
		for j in range(0, 40):
			ship.paintSpot([i, j], field_ship_spots, '')

	field_crew_id.coords(1, (0, 0))
	field_crew_id.itemconfig(1, text = '')
	current_ship_crew = []
	names_to_show = ''
	i = 1
	for crew in crew_list:
		if crew.id in ship.crew:
			current_ship_crew.append([i, crew])
			names_to_show = names_to_show + str(i) + '. ' + crew.first_name + ' ' + crew.second_name + ' id:' + str(crew.id) + '\n'
			i = i + 1
	field_crew_id.itemconfig(1, text = names_to_show)

	button_show_wall = Button(main_window, text = 'Wall', command = lambda:showPart('wall', field_part_id))
	button_show_wall.place(x = 10, y = 10, width = 100, height = 20)
	main_content.append(button_show_wall)

	button_show_door = Button(main_window, text = 'Door', command = lambda:showPart('door', field_part_id))
	button_show_door.place(x = 110, y = 10, width = 100, height = 20)
	main_content.append(button_show_door)

	button_show_reactor = Button(main_window, text = 'Reactor', command = lambda:showPart('reactor', field_part_id))
	button_show_reactor.place(x = 210, y = 10, width = 100, height = 20)
	main_content.append(button_show_reactor)

	button_show_engine=Button(main_window, text = 'Engine', command = lambda:showPart('engine', field_part_id))
	button_show_engine.place(x = 310, y = 10, width = 100, height = 20)
	main_content.append(button_show_engine)

	button_show_turret = Button(main_window, text = 'Turret', command = lambda:showPart('turret', field_part_id))
	button_show_turret.place(x = 410, y = 10, width = 100, height = 20)
	main_content.append(button_show_turret)

	button_show_shield = Button(main_window, text = 'Shield', command = lambda:showPart('shield', field_part_id))
	button_show_shield.place(x = 510, y = 10, width = 100, height = 20)
	main_content.append(button_show_shield)

	button_show_console = Button(main_window, text = 'Console', command = lambda:showPart('console', field_part_id))
	button_show_console.place(x = 610, y = 10, width = 100, height = 20)
	main_content.append(button_show_console)

	button_show_floor = Button(main_window, text = 'Floor', command = lambda:showPart('floor', field_part_id))
	button_show_floor.place(x = 710, y = 10, width = 100, height = 20)
	main_content.append(button_show_floor)

	button_show_deconstruct = Button(main_window, text = 'Deconstruct', command = lambda arg = [field_part_id, field_crew_info]:deconstructPart(arg))
	button_show_deconstruct.place(x = 810, y = 10, width = 100, height = 20)
	main_content.append(button_show_deconstruct)

	button_back = Button(main_window, text = 'Back', command = backFromDesignShip)
	button_back.place(x = 10, y = 850, width = 100, height = 20)
	main_content.append(button_back)

	button_apply = Button(main_window, text = 'Apply', command = lambda:applyDesignedShip(ship))
	button_apply.place(x = 1030, y = 850, width = 100, height = 20)
	main_content.append(button_apply)

	label_ship_name = Label(main_window, text = 'Ship name:')
	label_ship_name.place(x = 120, y = 850, width = 100, height = 20)
	main_content.append(label_ship_name)

	label_ship_race = Label(main_window, text = 'Ship race: ' + str(ship.race))
	label_ship_race.place(x = 320, y = 850, width = 200, height = 20)
	main_content.append(label_ship_race)

	label_ship_model = Label(main_window, text = 'Ship model: ' + str(ship.model))
	label_ship_model.place(x = 520, y = 850, width = 200, height = 20)
	main_content.append(label_ship_model)

	label_ship_size = Label(main_window, text = 'Ship size: ' + str(ship.size))
	label_ship_size.place(x = 720, y = 850, width = 200, height = 20)
	main_content.append(label_ship_size)

	ship_name = StringVar()
	ship_name.set('Ship name')
	field_ship_name = Entry(main_window, textvariable = ship_name)
	field_ship_name.place(x = 220, y = 850, width = 100, height = 20)
	main_content.append(field_ship_name)

	field_part_id.bind('<ButtonPress-1>', lambda event, arg = [field_crew_info]:fieldPartIdClick(event, arg))
	field_part_id.bind('<Motion>', lambda event, arg = field_part_id:fieldPartIdMotion(event, arg))

	field_ship_spots.bind('<ButtonPress-1>', lambda event, arg = [field_ship_spots, ship, field_ship_info, current_ship_crew, field_crew_info]:fieldShipSpotsClick(event, arg))
	field_ship_spots.bind('<Motion>', lambda event, arg = [field_ship_info,ship]: fieldShipSpotsMotion(event, arg))

	field_crew_id.bind('<ButtonPress-1>', lambda event, arg = [current_ship_crew, field_crew_info, field_part_id]: fieldCrewIdClick(event, arg))
###		MAKE ME!!
def paintWindowGalaxy():
	global main_window
	global main_content
	ship_list = SpaceBullshit99.ship_list
	system_list = SpaceBullshit99.system_list
	galaxy_size = SpaceBullshit99.galaxy_size
	galaxy_time = SpaceBullshit99.galaxy_time

	deleteMainContent()
	main_window.title('Galaxy')

	star_count = (galaxy_size[1] + 1) * 10
	spot_size = 15
	field_size = star_count * spot_size

	label_time = Label(main_window, text = 'time:')
	label_time.place(x = 20, y = 20, width = 100, height = 20)
	main_content.append(label_time)

	time = IntVar()
	time.set(galaxy_time)
	field_time = Entry(main_window, textvariable = time)
	field_time.place(x = 20, y = 40, width = 100, height = 20)
	main_content.append(field_time)

	tmp_button_ok_time = Button(main_window, text = 'Ok', command = lambda:tmpButtonOkTime(field_time))
	tmp_button_ok_time.place(x = 120, y = 40, width = 100, height = 20)
	main_content.append(tmp_button_ok_time)

	field_galaxy_map = Canvas(main_window, bg = 'white')
	field_galaxy_map.place(x = 220, y = 20, width = field_size, height= field_size)
	main_content.append(field_galaxy_map)

	field_fleet_mini = Canvas(main_window, bg = 'white')
	field_fleet_mini.place(x = 980, y = 20, width = 270, height = 400)
	main_content.append(field_fleet_mini)

	button_show_tech = Button(main_window, text = 'Tech tree', command = showTechTree)
	button_show_tech.place(x = 20, y = 260, width = 100, height = 20)
	main_content.append(button_show_tech)

	button_turn_galaxy = Button(main_window, text = 'Turn', command = turnGalaxy)
	button_turn_galaxy.place(x = 20, y = 280, width = 100, height = 20)
	main_content.append(button_turn_galaxy)

	button_fight = Button(main_window, text = 'fight', command = paintWindowFight)
	button_fight.place(x = 20, y = 300, width = 100, height = 20)
	main_content.append(button_fight)

	for i in range(0, star_count):
		for j in range(0, star_count):
			item = field_galaxy_map.create_rectangle(i * spot_size, j * spot_size, i * spot_size + spot_size, j * spot_size + spot_size, fill = 'black')
	for system in system_list:
		system.paint(field_galaxy_map)
	for ship in ship_list:
		ship.paintOnGalaxyMap(field_galaxy_map)

	field_galaxy_map.bind('<ButtonPress-1>', lambda event, arg = [field_fleet_mini]:fieldGalaxyClick(event, arg))
	field_fleet_mini.bind('<ButtonPress-1>', lambda event, arg = [field_fleet_mini]:fieldFleetMiniClick(event, arg))
	main_window.bind('<KeyPress-Escape>', pressEscButton)
###		MAKE ME!!
def paintWindowFight():
	global main_window
	global main_content
	ship_list = SpaceBullshit99.ship_list
#	system_list = SpaceBullshit99.system_list
#	galaxy_size = SpaceBullshit99.galaxy_size
#	galaxy_time = SpaceBullshit99.galaxy_time

	deleteMainContent()
	main_window.title('Fight title')

	label_mini_map = Label(main_window, text = 'mini_map:')
	label_mini_map.place(x = 20, y = 730, width = 100, height = 20)
	main_content.append(label_mini_map)

	label_ship_weapon = Label(main_window, text = 'ship_weapon:')
	label_ship_weapon.place(x = 240, y = 730, width = 100, height = 20)
	main_content.append(label_ship_weapon)

	label_ship_info = Label(main_window, text = 'ship_info:')
	label_ship_info.place(x = 840, y = 730, width = 100, height = 20)
	main_content.append(label_ship_info)

	label_mini_ship = Label(main_window, text = 'mini_ship:')
	label_mini_ship.place(x = 1060, y = 730, width = 100, height = 20)
	main_content.append(label_mini_ship)

	field_fight_map = Canvas(main_window, bg = 'black')
	field_fight_map.place(x = 20, y = 20, width = 1240, height = 700)
	main_content.append(field_fight_map)

	field_mini_map = Canvas(main_window, bg = 'black')
	field_mini_map.place(x = 20, y = 750, width = 200, height = 200)
	main_content.append(field_mini_map)

	field_ship_weapon = Canvas(main_window, bg = 'white')
	field_ship_weapon.place(x = 240, y = 750, width = 200, height = 200)
	main_content.append(field_ship_weapon)

	ship_weapon = field_ship_weapon.create_text(0, 0, anchor = 'nw', text = '', fill = 'black', activefill = 'lavender')
#	name_part_id = field_part_id.create_text(0, 0, anchor = 'nw', activefill = 'lavender')
	info_part_id = field_ship_weapon.create_text(0, 0, anchor = 'nw', fill = 'black')

	field_ship_info = Canvas(main_window, bg = 'white')
	field_ship_info.place(x = 840, y = 750, width = 200, height = 200)
	main_content.append(field_ship_info)

	ship_info = field_ship_info.create_text(0, 0, anchor = 'nw', text = '')

	field_mini_ship = Canvas(main_window, bg = 'white')
	field_mini_ship.place(x = 1060, y = 750, width = 200, height = 200)
	main_content.append(field_mini_ship)

	button_turn_fight = Button(main_window, text = 'Turn', command = turnFight)
	button_turn_fight.place(x = 520, y = 800, width = 100, height = 20)
	main_content.append(button_turn_fight)

	spot_size = 20
	list_of_spots = [['empty' for y in range(0, 200)] for x in range(0, 200)]
	field_mini_map_lines = [0, 0, 0, 0]
	i = 1
	for ship in ship_list:
		ship.position_on_battle = [10 * i,10 * i]
		list_of_spots[10 * i][10 * i] = 'ship'
		paintCurrentMiniMap([10 * i,10 * i], 'ship', 2, field_mini_map)
		i = i + 1

	TMP = [32, 18]
	paintFrameMiniMap(TMP, field_mini_map_lines, field_mini_map)
	paintCurrentFightMap(TMP, field_fight_map, list_of_spots)

	field_mini_map.bind('<ButtonPress-1>', lambda event, arg = [field_mini_map, field_fight_map, list_of_spots, field_mini_map_lines]:fieldMiniMapClick(event, arg))

	field_fight_map.bind('<ButtonPress-1>', lambda event, arg = [ship_list, field_mini_map, field_fight_map, list_of_spots, field_ship_info, field_mini_ship, field_ship_weapon]:fieldFightMapClick(event, arg))

	field_ship_weapon.bind('<ButtonPress-1>', lambda event, arg = [field_ship_weapon, field_mini_map, field_fight_map]:fieldShipWeaponClick(event, arg))
	field_ship_weapon.bind('<Motion>', lambda event, arg = field_ship_weapon:fieldShipWeaponMotion(event, arg))
#	main_window.bind('<KeyPress-Escape>', pressEscButton)

def fieldShipWeaponClick(event, arg):
	field = arg[0]
	field_mini_map = arg[1]
	field_fight_map = arg[2]
	part_list = SpaceBullshit99.part_list
	x = event.x
	y = event.y
	i = int(y / 15)

	message = field.itemconfig(1, 'text')[4].split()
	field.itemconfig(1, text = message_tmp)

def fieldShipWeaponMotion(event, field):
	part_list = SpaceBullshit99.part_list
	x = event.x
	y = event.y
	i = int(y / 15)
	field.coords(2, (0, 0))
	field.itemconfig(2, text = '')
	if i <= len(field.itemconfig(1, 'text')[4].split()) - 1:
		turret_name = field.itemconfig(1, 'text')[4].split()[i]
	else:
		turret_name = ''
		field.coords(2, (20, 20))
		field.itemconfig(2, text = '')
	for part in part_list:
		if (part.group == 'turret') and (part.name == turret_name):
			field.coords(2, (x + 20, y + 20))
			field.itemconfig(2, text = part.info())
			break

def fieldFightMapClick(event, arg):
	x = int(event.x / 20) + 1
	y = int(event.y / 20) + 1
	ship_list = arg[0]
	field_fight_map = arg[1]
	field_fight_map = arg[2]
	list_of_spots = arg[3]
	field_ship_info = arg[4]
	field_mini_ship = arg[5]
	field_ship_weapon = arg[6]

	if list_of_spots[x][y] == 'ship':
		for ship in ship_list:
			if ship.position_on_battle == [x, y]:
				field_ship_info.itemconfig(1, text = ship.infoBattle())
				weapon_text = ''
				ship.paintShipMini(field_mini_ship, [0, 0], 10)
				for spot in ship.spot:
#					ship.paintSpotMini([spot[0], spot[1]], field_mini_ship, [0, 0])
					if spot[4] == 'turret':
						for part in SpaceBullshit99.part_list:
							if (part.group == 'turret') and (part.id == spot[5]):
								weapon_text = weapon_text + part.name + '\n'
				field_ship_weapon.itemconfig(1, text = weapon_text)
	if list_of_spots[x][y] == 'empty':
		field_mini_ship.delete('all')
		field_ship_info.itemconfig(1, text = '')
		field_ship_weapon.itemconfig(1, text = '')

def fieldMiniMapClick(event, arg):
	x = event.x
	y = event.y
	field_mini_map = arg[0]
	field_fight_map = arg[1]
	list_of_spots = arg[2]
	field_mini_map_lines = arg[3]
	if x < 32:
		x = 32
	if y < 18:
		y = 18
	if x > 200 - 31:
		x = 200 - 31
	if y > 200 - 18:
		y = 200 - 18
	paintFrameMiniMap([x, y], field_mini_map_lines, field_mini_map)
	paintCurrentFightMap([x, y], field_fight_map, list_of_spots)
	

def paintCurrentFightMap(coords_of_center, field_fight_map, list_of_spots):
	x = coords_of_center[0]
	y = coords_of_center[1]
	dx = 31
	dy = 17

	for i in range(0, 62):
		for j in range(0, 35):
			if list_of_spots[x - dx + i][y - dy + j] == 'empty':
				color = 'black'
			if list_of_spots[x - dx + i][y - dy + j] == 'ship':
				color = 'green'
			item = field_fight_map.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill = color, outline = 'white')

def paintCurrentMiniMap(coords, object_type, size, field_mini_map):
	x = coords[0]
	y = coords[1]
	if object_type == 'empty':
		color = 'black'
	if object_type == 'ship':
		color = 'green'
	field_mini_map.create_rectangle(x, y, x + size, y + size, fill = color, outline = color)

def paintFrameMiniMap(coords_of_center, field_mini_map_lines, field_mini_map):
	x = coords_of_center[0]
	y = coords_of_center[1]
	erase4LinesMiniMap(field_mini_map, field_mini_map_lines)
	list_of_coords = [[x - 31, y - 17], [x + 31, y - 17], [x + 31, y + 17], [x - 31, y + 17]]
	paint4LinesMiniMap(list_of_coords, field_mini_map, field_mini_map_lines)
###		MAKE ME!!
#################################################################
