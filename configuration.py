"""
	Mark and Maven API
	Contact: systems@markandmaven.com
"""

import copy
import logging
import multiprocessing
import sys
import urllib3
import six
from six.moves import http_client as httplib

class TypeWithDefault(type):

	def __init__(cls, name, bases, dct):
		super(TypeWithDefault, cls).__init__(name, bases, dct)
		cls._default = None

	def __call__(cls):
		if cls._default is None:
			cls._default = type.__call__(cls)
		return copy.copy(cls._default)

	def set_default(cls, default):
		cls._default = copy.copy(default)

class Configuration(six.with_metaclass(TypeWithDefault, object)):

	# constructor
	def __init__(self):
		self.host = "https://api.markandmaven.com/v1" # default base URL
		self.temp_folder_path = None # temp file folder for downloading files

	# authentication settings
	self.api_key = {} # dict to store API key(s)
	self.api_key_prefix = {} # dict to store API prefix
	self.username = "" # username for HTTP basic authentication
	self.password = "" # password for HTTP basic authentication

	self.logger = {} # logging settings 
	self.logger["package_logger"] = logging.getLogger("mam_api_v1_sdk") # logging settings 
	self.logger["urllib3_logger"] = logging.getLogger("urllib3") # logging settings 
	self.logger_format = '%(asctime)s %(levelname)s %(message)s' # log format
	self.logger_stream_handler = None # log file handler
	self.logger_file = None # debug file location
	self.debug = False # debug switch

	# SSL/TLS verification
	# Set to false to skip verifying SSL certificate when calling API
	# from https server.
	self.verify_ssl = True
	self.ssl_ca_cert = None # set this to customise the certificate file to verify the peer
	self.cert_file = None # client certificate file
	self.key_file = None # client key file
	self.assert_hostname = None # set this to t/f to enable/disable SSL hostname verification

	# urllib3 connection pool's maximum number of connections saved
	# per pool. urllib3 uses 1 connection as default value, but this is
	# not the best value when you are making a lot of possibly parallel
	# requests to the same host, which is often the case here.
	# cpu_count * 5 is used as default value to increase performance.
	self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
	self.proxy = None # proxy URL
	self.safe_chars_for_path_param = '' # safe chars for path_param

	@property
	def logger_file(self):
		return self.__logger_file
	
	@logger_file.setter
	def logger_file(self, value):
		self.__logger_file = value
		if self.__logger_file:
			# If set logging file,
			# then add file handler and remove stream handler.
			self.logger_file_handler = logging.FileHandler(self.__logger_file)
			self.logger_file_handler.setFormatter(self.logger_formatter)
			for _, logger in six.iteritems(self.logger):
				logger.addHandler(self.logger_file_handler)
				if self.logger_stream_handler:
					logger.removeHandler(self.logger_stream_handler)
		else:
			self.logger_stream_handler = logging.StreamHandler()
			self.logger_stream_handler.setFormatter(self.logger_formatter)
			for _, logger in six.iteritems(self.logger):
				logger.addHandler(self.logger_stream_handler)
				if self.logger_file_handler:
					logger.removeHandler(self.logger_file_handler)

	@property
	def debug(self):
		return self.__debug

	@debug.setter
	def debug(self, value):
		self.__debug = value
		if self.__debug:
			for _, logger in six.iteritems(self.logger):
				logger.setLevel(logging.DEBUG)
				httplib.HTTPConnection.debuglevel = 1 # turn on httplib debug
		else:
			for _, logger in six.iteritems(self.logger):
				logger.setLevel(logging.WARNING)
				httplib.HTTPConnection.debuglevel = 0 # turn off httplib debug

	@property
	def logger_format(self):
		return self.__logger_format
	
	@logger_format.setter
	def logger_format(self, value):
		self.__logger_format = value
		self.logger_formatter = logging.Formatter(self.__logger_format)

	def get_api_key_with_prefix(self, identifier):
		if (self.api_key.get(identifier) and self.api_key_prefix.get(identifier)):
			return self.api_key_prefix[identifier] + ' ' + self.api_key[identifier]
		elif self.api_key.get(identifier):
			return self.api_key[identifier]

	def get_basic_auth_token(self):
		return urllib3.util.make_headers(basic_auth=self.username + ' ' + self.password).get('authorization')

	def auth_settings(self):
		return {
			'api-key': {
				'type': 'api_key',
				'in': 'header',
				'key': 'api-key',
				'value': self.get_api_key_with_prefix('api-key')
			},
		}

	def to_debug_report(self):
		return  "Python SDK Debug Report:\n"\
				"OS: {env}\n"\
				"Python Version: {pyversion}\n"\
				"Version of the API: 1.0.0\n"\
				"SDK Package Version: 1.0.0".\
				format(env=sys.platform, pyversion=sys.version)