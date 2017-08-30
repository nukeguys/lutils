# -*- coding: utf-8 -*-
from jira.config import get_jira
import os
import sys
try:
    import configparser
except ImportError:
    from six.moves import configparser

class LuJira:
	def __init__(self, profile):
		self.jira = get_jira(profile)

	def profile_from_url(self, url):
		def findfile(path):
			paths = ['.', os.path.expanduser('~')]
			paths.extend(sys.path)
			for dirname in paths:
				possible = os.path.abspath(os.path.join(dirname, path))
				if os.path.isfile(possible):
					return possible
			return None
		
		if not url.startswith('http://') and not url.startswith('https://'):
			raise EnvironmentError('url must be started "http://" or "https://"')

		config = configparser.ConfigParser(defaults={'user':None, 'pass': None, 'appid': None, 'autofix': False, 'verify': 'yes'})
		config_file = findfile('config.ini')
		profile = None
		if config_file:
			config.read(config_file)
			for section in config.sections():
				if url.startswith(config.get(section, 'url')):
					profile=section
					break
		return profile