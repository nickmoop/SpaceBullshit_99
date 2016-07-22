class Part():

	def __init__(	self,
					group_new='',
					id_new=0,
					name_new='',
					condition_new=0,
					skill_type_new='',
					skill_upgrade_new=0,
					energy_consumption_new=0,
					speed_galaxy_new=0,
					speed_battle_new=0,
					maneuverability_new=0,
					protection_new=0,
					recovery_new=0,
					damage_form_new='',
					damage_new=0,
					distance_new=0
				):
		self.group=group_new
		self.id=id_new
		self.name=name_new
		self.condition=condition_new
		self.skill_type=skill_type_new
		self.skill_upgrade=skill_upgrade_new
		self.energy_consumption=energy_consumption_new
		self.speed_galaxy=speed_galaxy_new
		self.speed_battle=speed_battle_new
		self.maneuverability=maneuverability_new
		self.protection=protection_new
		self.recovery=recovery_new
		self.damage_form=damage_form_new
		self.damage=damage_new
		self.distance=distance_new

	def info(self):
		info_message='id:'+str(self.id)+'\n'+'name:'+self.name+'\n'
		if self.condition!=0:
			info_message=info_message+'condition:'+str(self.condition)+'\n'
		if self.skill_type!='':
			info_message=info_message+'skill_type:'+self.skill_type+'\n'
		if self.skill_upgrade!=0:
			info_message=info_message+'skill_upgrade:'+str(self.skill_upgrade)+'\n'
		if self.energy_consumption!=0:
			info_message=info_message+'energy_consumption:'+str(self.energy_consumption)+'\n'
		if self.speed_galaxy!=0:
			info_message=info_message+'speed_galaxy:'+str(self.speed_galaxy)+'\n'
		if self.speed_battle!=0:
			info_message=info_message+'speed_battle:'+str(self.speed_battle)+'\n'
		if self.maneuverability!=0:
			info_message=info_message+'maneuverability:'+str(self.maneuverability)+'\n'
		if self.protection!=0:
			info_message=info_message+'protection:'+str(self.protection)+'\n'
		if self.recovery!=0:
			info_message=info_message+'recovery:'+str(self.recovery)+'\n'
		if self.damage_form!='':
			info_message=info_message+'damage_form:'+self.damage_form+'\n'
		if self.damage!=0:
			info_message=info_message+'damage:'+str(self.damage)+'\n'
		if self.distance!=0:
			info_message=info_message+'distance:'+str(self.distance)+'\n'
		return(info_message)
