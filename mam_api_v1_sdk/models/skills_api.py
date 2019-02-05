"""
	Mark and Maven API
	Contact: systems@markandmaven.com
"""

import re
import six
from mam_api_v1_sdk.api_client import ApiClient

class SkillsApi(object):
	def __init__(self, api_client=None):
		if api_client is None:
			api_client = ApiClient()
		self.api_client = api_client

	def get_skills(self, **kwargs):
		# This method makes a synchronous HTTP request by default. To make an
		# asynchronous HTTP request, please pass async=True
		kwargs['_return_http_data_only'] = True
		if kwargs.get('async'):
			return self.get_skills(**kwargs)
		else:
			(data) = self.get_skills(**kwargs)
			return data

	def get_skills_with_http_info(self, **kwargs):
		all_params = []
		all_params.append('async')
		all_params.append('_return_http_data_only')
		all_params.append('_preload_content')
		all_params.append('_request_timeout')
		params = locals()
		for key, val in six.iteritems(params['kwargs']):
			if key not in all_params:
				raise TypeError(
					"Got an unexpected keyword argument '%s'"
					" to method get_skills" % key
				)
			params[key] = val
		del params['kwargs']

		collection_formats = {}
		path_params = {}
		query_params = []
		header_params = {}
		form_params = []
		local_var_files = {}
		body_params = None

		# HTTP header `Accept`
		header_params['Accept'] = self.api_client.select_header_accept(
			['application/json'])

		# HTTP header `Content-Type`
		header_params['Content-Type'] = self.api_client.select_header_content_type(
			['application/json'])

		# Authentication setting
		auth_settings = ['api-key']

		return self.api_client.call_api(
			'/resumes/skills', 'GET',
			path_params,
			query_params,
			header_params,
			body=body_params,
			post_params=form_params,
			files=local_var_files,
			response_type='GetSkills',
			auth_settings=auth_settings,
			async=params.get('async'),
			_return_http_data_only=params.get('_return_http_data_only'),
			_preload_content=params.get('_preload_content', True),
			_request_timeout=params.get('_request_timeout'),
			collection_formats=collection_formats
		)