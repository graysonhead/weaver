from netweaver.core_classes.config_object import ConfigObject
from netweaver.core_classes.utils import extrapolate_dict

class Fabric(ConfigObject):

	def __init__(self, name, config):
		self.name = name
		self.config = config
		self.appliances = []
		self.is_fabric = True
		self.extrapolate_vlan_config()

	def extrapolate_vlan_config(self):
		self.config['vlans'] = extrapolate_dict(self.config['vlans'])

	def __repr__(self):
		return '<Fabric: {}>'.format(self.name)
