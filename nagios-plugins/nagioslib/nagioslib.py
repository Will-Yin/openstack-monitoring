"""
**  Copyright (C) 2014  Koffi Nogbe at gmail dot com

**  This program is free software: you can redistribute it and/or modify
**  it under the terms of the GNU General Public License as published by
**  the Free Software Foundation, either version 3 of the License, or
**  (at your option) any later version.

**  This program is distributed in the hope that it will be useful,
**  but WITHOUT ANY WARRANTY; without even the implied warranty of
**  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
**  GNU General Public License for more details.

**  You should have received a copy of the GNU General Public License
**  along with this program.  If not, see <http://www.gnu.org/licenses/>.

**  ***********************************
**  This program allow you to monitor openstack keystone service
**  This is a content base monitor as oppose to just port check
**  It pull user from keystone database and poll the time it takes to
**  to retrieve the user. It use a config file openrc.cfg
"""

import sys
import ConfigParser

class credential:
	def __init__(self,configFile):
		self.configFile = configFile

	def __retrieveCred__(self):
		cfg = ConfigParser.ConfigParser()
		try:
			cfg.read(self.configFile)
		except: 
			print "Unable to read the config file"
			sys.exit(2)
		username = cfg.get("credential","OS_USERNAME") 
		password = cfg.get("credential","OS_PASSWORD")
		url = cfg.get("credential","OS_AUTH_URL")
		tenant = cfg.get("credential","OS_TENANT_NAME")
		return username,password,tenant,url

	def getKeystone(self):
		cred = {}
		cred['username'] = self.__retrieveCred__()[0]
		cred['password'] = self.__retrieveCred__()[1]
		cred['auth_url'] = self.__retrieveCred__()[3]
		cred['tenant_name'] = self.__retrieveCred__()[2]
		return cred
